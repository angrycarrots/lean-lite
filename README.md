# lean-lite
This is a simple hack to complement QuantConnect Lean (https://github.com/QuantConnect/Lean) and QuantConnect lean-cli (https://github.com/QuantConnect/lean-cli) to:
- address some of the shortcomings with lean-cli
    - simulated data generation is broken - especially for options
    - processing simulated data does not currently work in the docker
- create the ability to backtest with the lean source code - no docker
    - great for running lean in debug which is useful if you want to understand the framework
    - running with lean source is easy - perhaps even faster than docker (lean-cli)
- make data available for local lean processing


As of this release, there is no need to change/modify/hack the lean source code - except for some 
configuration files (config.json). [Lean is very inconsistent in how it uses configuration files.  Furthermore, the requirement
that the configuration files reside in the execution directory is just wrong.]

Note: this distribution use **Python version 3.9** - not the official QuantConnect version.  Hey, it works.





# Installation
Requirements
- Since much of lean is in C#, I found it convienent to work in windows.  There is no reason why this
will not work in linux.
## Prepare your environment
1. Install anaconda https://www.anaconda.com/products/distribution
2. Create a virtual environment with python 3.9:
    ~~~
    conda create --name lean python=3.9
    ~~~
3. Clone/fork this repository.  This will be your project workspace. 
    ~~~
    git clone https://github.com/angrycarrots/lean-lite.git
    cd lean-lite
    ~~~
3. Activate and install lean-cli:
    ~~~
    conda activate lean
    pip install lean-cli
    ~~~

*Note: generally, we will not be using lean-cli. It
is merely a convenient way to install the necessary python libraries for
execution in the lean environment. These scripts (lean-lite) are a replacement/complement for 
lean-cli.  You can still use lean-cli with this project!*  

4. Create an environment variable for python (in windows):
    ~~~
    set PYTHONNET_PYDLL=ANACONDA\envs\lean\python39.dll
    ~~~
where *ANACONDA* is the directory where anaconda is installed.  For more information about this
see https://github.com/QuantConnect/Lean/tree/master/Algorithm.Python.  This setting needs to persist 
may be best set at the system environment variables panel.

4. Clone lean into a different directory, i.e. projects:
    ~~~
    cd projects
    git clone https://github.com/QuantConnect/Lean.git
    ~~~
5. Install dotnet. Follow the instructions: https://dotnet.microsoft.com/en-us/download

6. Build lean:
    ~~~
    cd Lean
    dotnet build QuantConnect.Lean.sln
    ~~~
    Optionally, create an optimized build of Lean using:
    ~~~
    cd Lean
    dotnet build -c Release QuantConnect.Lean.sln
    ~~~
7. Pick a directory to put generated data.  lean-cli typically puts this in
the *data* subdirectory in a lean-cli project folder (after running *lean init*).

8. Set the configuration in *config.py*:

    ~~~
    # the directory where the generated data resides
    DATADIR="s:/data"

    # the directory where lean is cloned into:
    LEANDIR="s:/PROJECTS/Lean.github"

    # use the Release optimized build of lean.
    # a release build of Lean must be constructed by:
    #   cd Lean
    #   dotnet build -c Release QuantConnect.Lean.sln
    # values: "Debug" or "Release"
    LEANOPTIMIZE="Debug"
    ~~~

## Yahoo Stock Data Downloader
Lean ToolBox has a utility for downloading data from yahoo.  This feature is hidden in lean-cli.  

The _yahoo_downloader.py script encapsulates the downloading process and stores the data in lean
data format.  You must follow the installation steps above.

For example, to run the data downloader:

~~~
python yahoo_downloader.py --tickers AAPL,MSFT,TSLA --fromdate 2018-01-01
~~~
For help with options:
~~~
python yahoo_downloader --help
~~~

## Random Options Data Generation
Option generation with lean-cli is *broken* [on purpose?]- especially, if you want options data. However,
lean works.

Problems with *lean data generate*:
- unable to generate multiple contracts because the *--chain-symbol-count* flag is hidden.
- generated data does not work in the current docker (why?)

The generate.py script encapsulates the QuantConnect.Toolbox for RandomDataGenerator. The options are different 
from *lean data generate*.

To see the options, use:
~~~
python generate.py --help
~~~
This will return the Toolbox help:
~~~
Lean Engine ToolBox

Usage: QuantConnect.ToolBox.exe [options]

Options:
  -?|-h|--help                         Show help information
  -V|--version                         Show version information
  --app                                [REQUIRED] Target tool, CASE INSENSITIVE: GDAXDownloader or
                                       GDAXDL/CryptoiqDownloader or CDL/DukascopyDownloader or DDL/IEXDownloader or
                                       IEXDL/FxcmDownloader or FDL/FxcmVolumeDownload or FVDL/GoogleDownloader or
                                       GDL/IBDownloader or IBDL/KrakenDownloader or KDL/OandaDownloader or
                                       ODL/QuandlBitfinexDownloader or QBDL/YahooDownloader or
                                       YDL/AlgoSeekFuturesConverter or ASFC/AlgoSeekOptionsConverter or
                                       ASOC/IVolatilityEquityConverter or IVEC/KaikoDataConverter or
                                       KDC/NseMarketDataConverter or NMDC/QuantQuoteConverter or
                                       QQC/CoarseUniverseGenerator or CUG/
                                       RandomDataGenerator or RDG
                                       Example 1: --app=DDL
                                       Example 2: --app=NseMarketDataConverter
                                       Example 3: --app=RDG
  --tickers                            [REQUIRED ALL downloaders (except QBDL)] --tickers=SPY,AAPL,etc
  --resolution                         [REQUIRED ALL downloaders (except QBDL, CDL) and IVolatilityEquityConverter,
                                       QuantQuoteConverter] *Not all downloaders support all resolutions. Send empty for
                                       more information.* CASE SENSITIVE: --resolution=Tick/Second/Minute/Hour/Daily/All
                                       [OPTIONAL for RandomDataGenerator - same format as downloaders, Options only
                                       support Minute
  --from-date                          [REQUIRED ALL downloaders] --from-date=yyyyMMdd-HH:mm:ss
  --to-date                            [OPTIONAL for downloaders] If not provided 'DateTime.UtcNow' will be used.
                                       --to-date=yyyyMMdd-HH:mm:ss
  --exchange                           [REQUIRED for CryptoiqDownloader] [Optional for KaikoDataConverter] The exchange
                                       to process, if not defined, all exchanges will be processed.
  --api-key                            [REQUIRED for QuandlBitfinexDownloader, IEXDownloader]
  --date                               [REQUIRED for AlgoSeekFuturesConverter, AlgoSeekOptionsConverter,
                                       KaikoDataConverter]Date for the option bz files: --date=yyyyMMdd
  --source-dir                         [REQUIRED for IVolatilityEquityConverter, KaikoDataConverter,
                                       CoinApiDataConverter, NseMarketDataConverter, QuantQuoteConverter]
  --destination-dir                    [REQUIRED for IVolatilityEquityConverter, NseMarketDataConverter,
                                       QuantQuoteConverter]
  --source-meta-dir                    [REQUIRED for IVolatilityEquityConverter]
  --start                              [REQUIRED for RandomDataGenerator. Format yyyyMMdd Example: --start=20010101]
  --end                                [REQUIRED for RandomDataGenerator. Format yyyyMMdd Example: --end=20020101]
  --market                             [OPTIONAL for RandomDataGenerator. Market of generated symbols. Defaults to
                                       default market for security type: Example: --market=usa]
  --symbol-count                       [REQUIRED for RandomDataGenerator. Number of symbols to generate data for:
                                       Example: --symbol-count=10]
  --security-type                      [OPTIONAL for RandomDataGenerator. Security type of generated symbols, defaults
                                       to Equity: Example: --security-type=Equity/Option/Forex/Future/Cfd/Crypto]
  --data-density                       [OPTIONAL for RandomDataGenerator. Defaults to Dense. Valid values:
                                       --data-density=Dense/Sparse/VerySparse ]
  --include-coarse                     [OPTIONAL for RandomDataGenerator. Only used for Equity, defaults to true:
                                       Example: --include-coarse=true]
  --quote-trade-ratio                  [OPTIONAL for RandomDataGenerator. Sets the ratio of generated quotes to
                                       generated trades. Values larger than 1 mean more quotes than trades. Only used
                                       for Option, Future and Crypto, defaults to 1: Example: --quote-trade-ratio=1.75 ]
  --random-seed                        [OPTIONAL for RandomDataGenerator. Sets the random number generator seed.
                                       Defaults to null (random seed). Example: --random-seed=11399 ]
  --ipo-percentage                     [OPTIONAL for RandomDataGenerator. Sets the probability each equity generated
                                       will have an IPO event. Note that this is not the total probability for all
                                       symbols generated. Only used for Equity. Defaults to 5.0: Example:
                                       --ipo-percentage=43.25 ]
  --rename-percentage                  [OPTIONAL for RandomDataGenerator. Sets the probability each equity generated
                                       will have a rename event. Note that this is not the total probability for all
                                       symbols generated. Only used for Equity. Defaults to 30.0: Example:
                                       --rename-percentage=20.0 ]
  --splits-percentage                  [OPTIONAL for RandomDataGenerator. Sets the probability each equity generated
                                       will have a stock split event. Note that this is not the total probability for
                                       all symbols generated. Only used for Equity. Defaults to 15.0: Example:
                                       --splits-percentage=10.0 ]
  --dividends-percentage               [OPTIONAL for RandomDataGenerator. Sets the probability each equity generated
                                       will have dividends. Note that this is not the probability for all symbols
                                       genearted. Only used for Equity. Defaults to 60.0: Example:
                                       --dividends-percentage=25.5 ]
  --dividend-every-quarter-percentage  [OPTIONAL for RandomDataGenerator. Sets the probability each equity generated
                                       will have a dividend event every quarter. Note that this is not the total
                                       probability for all symbols generated. Only used for Equity. Defaults to 30.0:
                                       Example: --dividend-every-quarter-percentage=15.0 ]
  --option-price-engine                [OPTIONAL for RandomDataGenerator. Sets the stochastic process, and returns new
                                       pricing engine to run calculations for that option. Defaults to
                                       BaroneAdesiWhaleyApproximationEngine: Example:
                                       --option-price-engine=BaroneAdesiWhaleyApproximationEngine ]
  --volatility-model-resolution        [OPTIONAL for RandomDataGenerator. Sets the volatility model period span.
                                       Defaults to Daily: Example: --volatility-model-resolution=Daily ]
  --chain-symbol-count                 [OPTIONAL for RandomDataGenerator. Sets the size of the option chain. Defaults to
                                       1 put and 1 call: Example: --chain-symbol-count=2 ]

The ToolBox is a wrapper of >15 tools. Each require a different set of parameters. Example: --app=YahooDownloader --tickers=SPY,AAPL --resolution=Daily --from-date=yyyyMMdd-HH:mm:ss --to-date=yyyyMMdd-HH:mm:ss
~~~
*Note: do not specify the --app flag!*

To generate options for one ticker with 10 strikes:
~~~
python generate.py --start 20220101 --end 20220501 --symbol-count 1 --security-type Option --resolution Minute --chain-symbol-count 10
~~~

## Run a backtest
At this point, we need a project.  You can use *lean cloud pull* (after you *lean login*) to retrieve
projects you have on QuantConnect.com.  Otherwise, use the *demo_project* included with this distribution.

With this demo, we will use the options generated in the Generate section above.  Look in the DATADIR/options/usa/minute to get the newly generated ticker symbol.

The demo project uses parameters for the ticker.  Edit demo_project/config.json and change the ticker:
~~~
{
    "algorithm-language": "Python",
    "parameters": {
        "TAKE_PROFIT": "0.5",
        "MAX_DELTA_PUT": "0.4",
        "MAX_DELTA_CALL": "0.4",
        "ticker": "NXJ"
    },
    "description": "exploring",
    "cloud-id": 11592212,
    "local-id": 840173305
}
~~~
**IF YOU DO NOT CHANGE THE TICKER, YOU WILL NOT GET ANY RESULTS**

To process a backtest and generate a report:
~~~
python backtest.py --main demo_project/main.py
~~~

The python class name for this demo_project is OptionWhelAlgorithm. This will generate files in the demo_project/backtests/[timestamp] directory:
- log.txt
- OptionWhelAlgorithm - financial analysis 
- OptionWhelAlgorithm_config.json - the Lean configuration file
- OptionWhelAlgorithm-log.txt - more logs
- OptionWhelAlgorithm-order-events.json - the trade transactions
- report.html - the tearsheet report
- report-backtesting-portfolio.json - portfolio stats
- report-live-portfolio.json - portfolio stats (repeat?)
- main.py - the code used in this backtest



## Known Issues
- Does not import Library or auxilary files (anyone know how to do this?).

## Summary
Lean is a great platform; however, it seems lean-cli has been neglected.  Perhaps, this
repository will become obsolete as lean-cli evolves and shortcomings are fixed.

Please:
- fork and improve
- report issues
- send comments / suggestions to athanas@vastscientific.com
- enjoy

Fini.



