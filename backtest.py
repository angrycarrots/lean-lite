# a hack to enable backtest processing of generated option data


core={
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

report_config = {
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



import os
import json
import argparse
from datetime import datetime
import re
import shutil
from pathlib import Path

parser = argparse.ArgumentParser("lean runner")
parser.add_argument('--main',type=str,default='main.py')
# parser.add_argument('--datadir',type=str,default="s:/PROJECTS/Lean.Github/Data")
parser.add_argument('--datadir',type=str,default="s:/Data")
parser.add_argument('--leandir',type=str,default="s:/PROJECTS/Lean.Github/Launcher/bin/Debug")
parser.add_argument('--leanreportdir',type=str,default="s:/PROJECTS/Lean.Github/Report/bin/Debug")
args = parser.parse_args()
cwd = os.getcwd()
lean = "QuantConnect.Lean.Launcher.exe"
reportexe = "QuantConnect.Report.exe"

def getclassname(fn):
    """
    returns the name of the first class name in the file
    """
    with open(fn,"r") as f:
        for line in f:
        
            # checking condition for string found or not
            if "class" in line: 
                # print(line)
                cn = line.split()[1].split("(")[0]
                # print(cn)
                return cn

def getparams(fn):
    with open(fn,"r") as f:
        # content = f.readlines()
        d = json.load(f)
    return d


wdir = str(Path(args.main).resolve())
basedir = str(Path(os.path.dirname(wdir)))
configfile = str(Path(basedir+"/config.json"))
cn = getclassname(args.main)
configd = getparams(configfile)
# add the config to the config
core = {**core,**configd}
core["algorithm-type-name"]=cn
core["algorithm-location"]=wdir
core["data-dir"]=str(Path(args.datadir))
core["data-directory"]=str(Path(args.datadir))
core["cache-location"]=str(Path(args.datadir))
core[ "data-folder"]=str(Path(args.datadir))
core["close-automatically"]=True
# core["results-destination-folder"]=wdir
# write the config
config = f"{cn}.json"
with open(config,"w") as outfile:
    json.dump(core,outfile,indent=4)

cdir = str(Path(config).resolve())
# run the program
os.chdir(args.leandir)
cmd = f"{lean} --config {cdir}"
print(cmd)
os.system(cmd)
# the results are the launcher file
orderfn = f"{cn}-order-events.json"
resultfn= f"{cn}.json"
# create results folder
btfolder = str(Path(basedir+"/backtests"))
if not os.path.exists(btfolder):
  os.mkdir(btfolder)



fdrname = datetime.now().strftime("%Y-%m-%d-%H-%M")
btfldr = str(Path(btfolder+"/"+fdrname))
os.mkdir(btfldr)
# copy
print("copy ",f"{args.leandir}/{orderfn}",f"{btfldr}/orders.json")
shutil.copy(str(Path(f"{args.leandir}/{resultfn}")),str(Path(f"{btfldr}/results.json")))
shutil.copy(str(Path(f"{args.leandir}/{orderfn}")),str(Path(f"{btfldr}/orders.json")))
shutil.copy(str(Path(f"{wdir}")),str(Path(f"{btfldr}/{os.path.basename(wdir)}")))
# generate a report
report_config["strategy-name"]=cn
report_config["strategy-version"]=fdrname
report_config["strategy-description"]=f"Created {fdrname}"
report_config["backtest-data-source-file"]=str(Path(f"{btfldr}/results.json"))
report_config["report-destination"]=str(Path(f"{btfldr}/report.html"))
report_config["live-data-source-file"]=str(Path(f"{btfldr}/results.json"))
report_config[ "data-folder"]=str(Path(args.datadir))

config = f"{args.leanreportdir}/config.json"
with open(config,"w") as f:
  json.dump(report_config,f)

os.chdir(args.leanreportdir)
cmd = f"{reportexe}"
os.system(cmd)
print("Fini")
