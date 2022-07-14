
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

import os
import json
import argparse
from datetime import datetime
import shutil
from pathlib import Path
from lib.lean_configurations import *
from config import *

#################################################################################################
# main
#################################################################################################
# command line arguments
# FIXME: default values should be in a configuration
parser = argparse.ArgumentParser("lean runner")
parser.add_argument('--main',type=str,default='main.py')
args = parser.parse_args()

# useful values
cwd = os.getcwd()
lean = "QuantConnect.Lean.Launcher.exe"
reportexe = "QuantConnect.Report.exe"

# useful methods
def getclassname(fn):
    """
    returns the name of the first class name in the file
    """
    with open(fn,"r") as f:
        for line in f:
            if "class" in line: 
                cn = line.split()[1].split("(")[0]
                return cn

def getparams(fn):
    with open(fn,"r") as f:
        d = json.load(f)
    return d

print("ENVIRONMENT:")
print(f"\tDATDIR={DATADIR}")
print(f"\tLEANDIR={LEANDIR}\n")
print(f"\tLEANOPTIMIZE={LEANOPTIMIZE}\n")

# prepare a backtest
wdir = str(Path(args.main).resolve())
basedir = str(Path(os.path.dirname(wdir)))
# the project parameters
configfile = str(Path(basedir+"/config.json"))

# create results folder
btfolder = str(Path(basedir+"/backtests"))
exedir = f"{LEANDIR}/Launcher/bin/{LEANOPTIMIZE}"
if not os.path.exists(btfolder):
  os.mkdir(btfolder)
# prepare a report folder
fdrname = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
btfldr = str(Path(btfolder+"/"+fdrname))
os.mkdir(btfldr)
# get the class name
cn = getclassname(args.main)
configd = getparams(configfile)
#define the lean backtest config
config = f"{btfldr}/{cn}_config.json"
config = str(Path(config).resolve())
# add the config to the config
launcher_template["algorithm-type-name"]=cn
launcher_template["algorithm-location"]=wdir
launcher_template["data-directory"]=str(Path(DATADIR))
launcher_template["cache-location"]=str(Path(DATADIR))
launcher_template[ "data-folder"]=str(Path(DATADIR))
launcher_template["close-automatically"]=True
launcher_template["results-destination-folder"]=btfldr
launcher_template = {**launcher_template,**configd}
# write the config
with open(config,"w") as outfile:
    json.dump(launcher_template,outfile,indent=4)

# run the program
os.chdir(str(Path(exedir)))
cmd = f"{lean} --config {config}"
os.system(cmd)
# the results are the launcher file
orderfn = f"{cn}-order-events.json"
resultfn= f"{cn}.json"
#copy the code
shutil.copy(str(Path(f"{wdir}")),str(Path(f"{btfldr}/{os.path.basename(wdir)}")))

# generate a report
report_template["strategy-name"]=cn
report_template["strategy-version"]=fdrname
report_template["strategy-description"]=f"Created {fdrname}"
report_template["backtest-data-source-file"]=str(Path(f"{btfldr}/{resultfn}"))
report_template["report-destination"]=str(Path(f"{btfldr}/report.html"))
report_template["live-data-source-file"]=str(Path(f"{btfldr}/{resultfn}"))
report_template["data-folder"]=str(Path(DATADIR))

exedir = f"{LEANDIR}/Report/bin/{LEANOPTIMIZE}"
# lean requires the configuration file in the exe dir. yep.
config = f"{exedir}/config.json"
with open(config,"w") as f:
  json.dump(report_template,f)
os.chdir(exedir)
cmd = f"{reportexe}"
os.system(cmd)

print("Fini")
