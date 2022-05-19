# lean-lite
A hack to enable options data generation and backtesting in QuantConnect Lean (https://github.com/QuantConnect/Lean).
As of this release, there is no need to change/modify/hack the lean source code.

# Installation
Requirements
- Since much of lean is in C#, I found it convienent to work in windows.  There is no reason why this
will not work in linux.
## Prepare your environment
1. Install anaconda
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
execution in the lean environment. These scripts (lean-lite) is a replacement for 
lean-cli.*

4. Create an environment variable for python:
    ~~~
    set PYTHONNET_PYDLL=ANACONDA\envs\lean\python39.dll
    ~~~
where *ANACONDA* is the directory where anaconda is installed.

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
7. Pick a directory to put generated data.  lean-cli typically puts this in
the *data* subdirectory in a lean-cli project folder (after running *lean init*).

8. Set the configuration in config.py:

    ~~~
    # the directory where the generated data resides
    DATADIR="s:/data"

    # the directory where lean is cloned into:
    LEANDIR="s:/Lean"
    ~~~

## Generate data (options)
Option generation with lean-cli is *broken* [on purpose?]- especially, if you want options data. However,
lean works.
## Run a backtest
At this point, we need a project.  You can use *lean cloud pull* (after you *lean login*) to retrieve
project you have on QuantConnect.com.  Otherwise, use the sample project included with this distribution.


