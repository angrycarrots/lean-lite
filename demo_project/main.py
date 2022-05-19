#region imports
from AlgorithmImports import *
#endregion
# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from QuantConnect.Securities.Option import OptionPriceModels
from datetime import timedelta


class OptionWheelAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage,AccountType.Margin)
        self._no_K = 20       # no of strikes around ATM => for uni selection
        self.MIN_EXPIRY = 3  # min num of days to expiration => for uni selection
        self.MAX_EXPIRY = 12  # max num of days to expiration => for uni selection
        self.MAX_DELTA_PUT = 0.4
        self.MAX_DELTA_CALL = 0.4
        self.TAKE_PROFIT = float(self.GetParameter("TAKE_PROFIT"))
        self.MIN_PREMIUM  = 0.1
        
        self.ticker = self.GetParameter("ticker")
        self.benchmarkTicker =self.ticker
        self.SetStartDate(2022, 1, 1)
        self.SetEndDate(2022, 5, 1)
        self.SetCash(100000)
        self.OPTION_COUNT = 2
        self.expiry = None
        
        self.resolution = Resolution.Minute
        self.call, self.put, self.takeProfitTicket = None, None, None

        equity = self.AddEquity(self.ticker, self.resolution)
        option = self.AddOption(self.ticker, self.resolution)
        option.SetFilter(-4,4,timedelta(days=3),timedelta(days=20))
        self.symbol = option.Symbol

        # set our strike/expiry filter for this option chain
        option.SetFilter(self.UniverseFunc)

        # for greeks and pricer (needs some warmup) - https://github.com/QuantConnect/Lean/blob/21cd972e99f70f007ce689bdaeeafe3cb4ea9c77/Common/Securities/Option/OptionPriceModels.cs#L81
        # both European & American, automatically
        option.PriceModel = OptionPriceModels.BjerksundStensland()

        # this is needed for Greeks calcs
        self.SetWarmUp(TimeSpan.FromDays(60))    # timedelta(7)

        # use the underlying equity as the benchmark
        self.SetBenchmark(self.benchmarkTicker)


    def OnData(self, slice):
        if (self.IsWarmingUp):
            return

        option_invested = [
            x.Key for x in self.Portfolio if x.Value.Invested and x.Value.Type == SecurityType.Option]
            
        equity_invested = [
            x.Key for x in self.Portfolio if x.Value.Invested and x.Value.Type == SecurityType.Equity]

        invested = [
            x.Key for x in self.Portfolio if x.Value.Invested ]

        if len(option_invested) == 1:
            return

        # If we already have underlying - check if we need to sell covered call
        t=self.Portfolio[self.ticker]
        
        #self.Debug(self.Portfolio[self.ticker].ToString())
        if self.Portfolio[self.ticker].Quantity > 0:
            self.Debug("TradeCallOption "+str(t)+" "+str(invested)+" ")
            self.TradeCallOption(slice)
        else:
            self.Debug("TradePutOption "+str(t)+" "+str(invested)+" "+str(self.Portfolio.Cash))
            self.TradePutOption(slice)

        # self.Debug("Stock holdings: ",self.Portfolio.HoldStock)

    def TradePutOption(self, slice):
        for i in slice.OptionChains:
            if i.Key != self.symbol:
                continue

            chain = i.Value

            # filter the put options contracts
            puts = [x for x in chain if x.Right == OptionRight.Put and abs(x.Greeks.Delta) > 0 and abs(
                x.Greeks.Delta) < self.MAX_DELTA_PUT and x.BidPrice > self.MIN_PREMIUM]

            # sorted the contracts according to their expiration dates and choose the ATM options
            contracts = sorted(sorted(puts, key=lambda x: x.BidPrice, reverse=True),
                               key=lambda x: x.Expiry)

            if len(contracts) == 0:
                continue

            self.put = contracts[0].Symbol
            self.expiry = contracts[0].Expiry
            c=self.Portfolio.Cash
            u=self.Portfolio.UnsettledCash
            strike = contracts[0].Strike

            # can we afford this
            needed = strike*100*self.OPTION_COUNT
            if c < needed:
                return
            
            # self.OPTION_COUNT = int(c / 100 / strike)

            # short the put options
            ticket = self.MarketOrder(
                self.put, -self.OPTION_COUNT, asynchronous=False)

            # set Take Profit order
            self.takeProfitTicket = self.LimitOrder(
                self.put, self.OPTION_COUNT, round(ticket.AverageFillPrice * self.TAKE_PROFIT, 2))

    def TradeCallOption(self, slice):
        # if self.call is None:
        #     return
        for i in slice.OptionChains:
            if i.Key != self.symbol:
                continue

            chain = i.Value

            # filter the put options contracts
            calls = [x for x in chain if x.Right == OptionRight.Call and abs(x.Greeks.Delta) > 0 and abs(
                x.Greeks.Delta) < self.MAX_DELTA_CALL and x.BidPrice > self.MIN_PREMIUM]

            # sorted the contracts according to their expiration dates and choose the ATM options
            contracts = sorted(sorted(calls, key=lambda x: x.BidPrice, reverse=True),
                               key=lambda x: x.Expiry)

            if len(contracts) == 0:
                continue

            self.call = contracts[0].Symbol
            self.expiry = contracts[0].Expiry

            # short the call options
            ticket = self.MarketOrder(
                self.call, -self.OPTION_COUNT, asynchronous=False)

            # set Take Profit order
            self.takeProfitTicket = self.LimitOrder(
                self.call, self.OPTION_COUNT, round(ticket.AverageFillPrice * self.TAKE_PROFIT, 2))

    def OnOrderEvent(self, orderEvent):
        self.PortfolioStatus('OnOrderEvent')
        self.Log("OnOrderEvent "+str(self.Portfolio[self.ticker])+" "+str(orderEvent))

    def OnAssignmentOrderEvent(self, assignmentEvent):
        self.PortfolioStatus('OnAssignmentOrderEvent')
        self.Debug("OnAssignmentOrderEvent "+str(self.Portfolio[self.ticker])+" "+str(assignmentEvent))
        if self.takeProfitTicket != None:
            self.takeProfitTicket.cancel()
            self.takeProfitTicket = None

    def UniverseFunc(self, universe):
        return universe.IncludeWeeklys()\
            .Strikes(-self._no_K, self._no_K)\
            .Expiration(timedelta(self.MIN_EXPIRY), timedelta(self.MAX_EXPIRY))

    def OnFrameworkData(self):
        return

    def PortfolioStatus(self,msg):
        holdings="("+msg+")"
        for k in self.Portfolio.Keys:
            v = self.Portfolio[k]
            holdings += str(v.Symbol.Value)+"["+str(v.Quantity)+"];"
        self.Log(holdings)
