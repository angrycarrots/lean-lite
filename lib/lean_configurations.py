
#####################################################################################
#
# QuantConnect Lean hack to enable backtesting against an installed version of Lean
# instead of docker.  
#
# The motivation: 1) lean-cli option data generation is broken, 2) generated data
# are not readable with the docker framework, 3) a way to debug Lean to get a better
# understanding how it works.
#
# Author: athanas@vastscientific.com
#
# Copyright 2022 Michael Athanas, Ph.D.
#
# Permission is hereby granted, free of charge, to any person obtaining a 
# copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
#  Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR 
# THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#########################################################################################
# Lean Launcher configuration
launcher_template={
"environment": "backtesting",
  "algorithm-type-name": "BasicTemplateFrameworkAlgorithm",
  "algorithm-language": "python",
  "algorithm-location": "../../../Algorithm.Python/BasicTemplateFrameworkAlgorithm.py",
  "data-folder": "../../../Data/",
  "debugging": False,
  "debugging-method": "PTVSD",
  "log-handler": "QuantConnect.Logging.CompositeLogHandler",
  "messaging-handler": "QuantConnect.Messaging.Messaging",
  "job-queue-handler": "QuantConnect.Queues.JobQueue",
  "api-handler": "QuantConnect.Api.Api",
  "map-file-provider": "QuantConnect.Data.Auxiliary.LocalDiskMapFileProvider",
  "factor-file-provider": "QuantConnect.Data.Auxiliary.LocalDiskFactorFileProvider",
  "data-provider": "QuantConnect.Lean.Engine.DataFeeds.DefaultDataProvider",
  "alpha-handler": "QuantConnect.Lean.Engine.Alphas.DefaultAlphaHandler",
  "data-channel-provider": "DataChannelProvider",
  "object-store": "QuantConnect.Lean.Engine.Storage.LocalObjectStore",
  "data-aggregator": "QuantConnect.Lean.Engine.DataFeeds.AggregationManager",


  "symbol-minute-limit": 10000,
  "symbol-second-limit": 10000,
  "symbol-tick-limit": 10000,


  "maximum-data-points-per-chart-series": 4000,



  "force-exchange-always-open": False,


  "transaction-log": "",


  "job-user-id": "0",
  "api-access-token": "",
  "job-organization-id": "",



  "live-data-port": 8020,


  "live-cash-balance": "",
  "live-holdings": "[]",


  "ib-account": "",
  "ib-user-name": "",
  "ib-password": "",
  "ib-host": "127.0.0.1",
  "ib-port": "4002",  
  "ib-agent-description": "Individual",
  "ib-tws-dir": "C/Jts",
  "ib-trading-mode": "paper",
  "ib-enable-delayed-streaming-data": False,
  "ib-version": "974",


  "tradier-environment": "paper",
  "tradier-account-id": "",
  "tradier-access-token": "",


  "oanda-environment": "Practice",
  "oanda-access-token": "",
  "oanda-account-id": "",




  "fxcm-user-name": "",
  "fxcm-password": "",
  "fxcm-account-id": "",


  "iqfeed-host": "127.0.0.1",
  "iqfeed-username": "",
  "iqfeed-password": "",
  "iqfeed-productName": "",
  "iqfeed-version": "1.0",


  "gdax-api-secret": "",
  "gdax-api-key": "",
  "gdax-passphrase": "",


  "bitfinex-api-secret": "",
  "bitfinex-api-key": "",


  "binance-api-secret": "",
  "binance-api-key": "",




  "binanceus-api-secret": "",
  "binanceus-api-key": "",




  "kraken-api-secret": "",
  "kraken-api-key": "",



  "atreyu-host": "",
  "atreyu-req-port": "",
  "atreyu-sub-port": "",
  "atreyu-username": "",
  "atreyu-password": "",
  "atreyu-client-id": "",
  "atreyu-broker-mpid": "",
  "atreyu-locate-rqd": "",


  "tt-user-name": "",
  "tt-session-password": "",
  "tt-account-name": "",
  "tt-rest-app-key": "",
  "tt-rest-app-secret": "",
  "tt-rest-environment": "",
  "tt-market-data-sender-comp-id": "",
  "tt-market-data-target-comp-id": "",
  "tt-market-data-host": "",
  "tt-market-data-port": "",
  "tt-order-routing-sender-comp-id": "",
  "tt-order-routing-target-comp-id": "",
  "tt-order-routing-host": "",
  "tt-order-routing-port": "",
  "tt-log-fix-messages": False,




  "exante-client-id": "",
  "exante-application-id": "",
  "exante-shared-key": "",





  "nasdaq-auth-token": "",



  "tiingo-auth-token": "",



  "us-energy-information-auth-token": "",


  "iex-cloud-api-key": "",


  "coinapi-api-key": "",




  "polygon-api-key": "",


  "zerodha-access-token": "",
  "zerodha-api-key": "",





  "samco-client-id": "",
  "samco-client-password": "",
  "samco-year-of-birth": "",





  "ftx-api-secret": "",
  "ftx-api-key": "",



  "ftxus-api-secret": "",
  "ftxus-api-key": "",


  "parameters": {

    "intrinio-username": "",
    "intrinio-password": "",

    "ema-fast": 10,
    "ema-slow": 20
  },


  "regression-test-languages": [ "CSharp", "Python" ],

  "environments": {


    "backtesting": {
      "live-mode": False,

      "setup-handler": "QuantConnect.Lean.Engine.Setup.BacktestingSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.BacktestingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.FileSystemDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.BacktestingRealTimeHandler",
      "history-provider": [ "QuantConnect.Lean.Engine.HistoricalData.SubscriptionDataReaderHistoryProvider" ],
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BacktestingTransactionHandler"
    },


    "live-paper": {
      "live-mode": True,


      "live-mode-brokerage": "PaperBrokerage",

      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "data-queue-handler": [ "QuantConnect.Lean.Engine.DataFeeds.Queues.LiveDataQueue" ],
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BacktestingTransactionHandler"
    },


    "live-zerodha": {
      "live-mode": True,


      "live-mode-brokerage": "ZerodhaBrokerage",
      "data-queue-handler": [ "ZerodhaBrokerage" ],

      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-samco": {
      "live-mode": True,


      "live-mode-brokerage": "SamcoBrokerage",
      "data-queue-handler": [ "SamcoBrokerage" ],

      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-tradier": {
      "live-mode": True,



      "tradier-save-tokens": True,


      "live-mode-brokerage": "TradierBrokerage",
      "data-queue-handler": [ "TradierBrokerage" ],

      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler"
    },


    "live-interactive": {
      "live-mode": True,


      "live-mode-brokerage": "InteractiveBrokersBrokerage",
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "data-queue-handler": [ "QuantConnect.Brokerages.InteractiveBrokers.InteractiveBrokersBrokerage" ],
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-interactive-iqfeed": {
      "live-mode": True,


      "live-mode-brokerage": "InteractiveBrokersBrokerage",
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "data-queue-handler": [ "QuantConnect.ToolBox.IQFeed.IQFeedDataQueueHandler" ],
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "QuantConnect.ToolBox.IQFeed.IQFeedDataQueueHandler", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-fxcm": {
      "live-mode": True,


      "live-mode-brokerage": "FxcmBrokerage",
      "data-queue-handler": [ "FxcmBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-oanda": {
      "live-mode": True,


      "live-mode-brokerage": "OandaBrokerage",
      "data-queue-handler": [ "OandaBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },

    "live-gdax": {
      "live-mode": True,


      "live-mode-brokerage": "GDAXBrokerage",
      "data-queue-handler": [ "GDAXDataQueueHandler" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },

    "live-bitfinex": {
      "live-mode": True,


      "live-mode-brokerage": "BitfinexBrokerage",
      "data-queue-handler": [ "BitfinexBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },

    "live-binance": {
      "live-mode": True,


      "live-mode-brokerage": "QuantConnect.BinanceBrokerage.BinanceBrokerage",
      "data-queue-handler": [ "QuantConnect.BinanceBrokerage.BinanceBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },

    "live-binanceus": {
      "live-mode": True,


      "live-mode-brokerage": "QuantConnect.BinanceBrokerage.BinanceUSBrokerage",
      "data-queue-handler": [ "QuantConnect.BinanceBrokerage.BinanceUSBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-atreyu": {
      "live-mode": True,


      "live-mode-brokerage": "QuantConnect.Atreyu.AtreyuBrokerage",
      "data-queue-handler": [ "QuantConnect.Lean.Engine.DataFeeds.Queues.LiveDataQueue" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler"
    },


    "live-trading-technologies": {
      "live-mode": True,


      "live-mode-brokerage": "TradingTechnologiesBrokerage",
      "data-queue-handler": [ "TradingTechnologiesBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler"
    },


    "live-kraken": {
      "live-mode": True,


      "live-mode-brokerage": "KrakenBrokerage",
      "data-queue-handler": [ "KrakenBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },


    "live-ftx": {
      "live-mode": True,


      "live-mode-brokerage": "QuantConnect.FTXBrokerage.FTXBrokerage",
      "data-queue-handler": [ "QuantConnect.FTXBrokerage.FTXBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    },

    "live-exante": {
      "live-mode": True,


      "live-mode-brokerage": "QuantConnect.ExanteBrokerage.ExanteBrokerage",
      "data-queue-handler": [ "QuantConnect.ExanteBrokerage.ExanteBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": "BrokerageHistoryProvider"
    },


    "live-ftxus": {
      "live-mode": True,


      "live-mode-brokerage": "QuantConnect.FTXBrokerage.FTXUSBrokerage",
      "data-queue-handler": [ "QuantConnect.FTXBrokerage.FTXUSBrokerage" ],
      "setup-handler": "QuantConnect.Lean.Engine.Setup.BrokerageSetupHandler",
      "result-handler": "QuantConnect.Lean.Engine.Results.LiveTradingResultHandler",
      "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.LiveTradingDataFeed",
      "real-time-handler": "QuantConnect.Lean.Engine.RealTime.LiveTradingRealTimeHandler",
      "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BrokerageTransactionHandler",
      "history-provider": [ "BrokerageHistoryProvider", "SubscriptionDataReaderHistoryProvider" ]
    }
  }
}

# Lean Report configuration
report_template = {
    "data-folder": "/Lean/Data",
    # "strategy-name": strategy_name or "",
    # "strategy-version": strategy_version or "",
    # "strategy-description": strategy_description or "",
    "live-data-source-file": "live-data-source-file.json" if False is not None else "",
    "backtest-data-source-file": "backtest-data-source-file.json",
    "report-destination": "/tmp/report.html",

    "environment": "report",

    "log-handler": "QuantConnect.Logging.CompositeLogHandler",
    "messaging-handler": "QuantConnect.Messaging.Messaging",
    "job-queue-handler": "QuantConnect.Queues.JobQueue",
    "api-handler": "QuantConnect.Api.Api",
    "map-file-provider": "QuantConnect.Data.Auxiliary.LocalDiskMapFileProvider",
    "factor-file-provider": "QuantConnect.Data.Auxiliary.LocalDiskFactorFileProvider",
    "data-provider": "QuantConnect.Lean.Engine.DataFeeds.DefaultDataProvider",
    "alpha-handler": "QuantConnect.Lean.Engine.Alphas.DefaultAlphaHandler",
    "data-channel-provider": "DataChannelProvider",

    "environments": {
        "report": {
            "live-mode": False,

            "setup-handler": "QuantConnect.Lean.Engine.Setup.ConsoleSetupHandler",
            "result-handler": "QuantConnect.Lean.Engine.Results.BacktestingResultHandler",
            "data-feed-handler": "QuantConnect.Lean.Engine.DataFeeds.FileSystemDataFeed",
            "real-time-handler": "QuantConnect.Lean.Engine.RealTime.BacktestingRealTimeHandler",
            "history-provider": "QuantConnect.Lean.Engine.HistoricalData.SubscriptionDataReaderHistoryProvider",
            "transaction-handler": "QuantConnect.Lean.Engine.TransactionHandlers.BacktestingTransactionHandler"
        }
    }
}