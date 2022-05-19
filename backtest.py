
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
import re
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
# parser.add_argument('--datadir',type=str,default="s:/PROJECTS/Lean.Github/Data")
parser.add_argument('--datadir',type=str,default=DATADIR)
parser.add_argument('--leandir',type=str,default=LEANDIR+"/Launcher/bin/Debug")
parser.add_argument('--leanreportdir',type=str,default=LEANDIR+"/Report/bin/Debug")
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

# prepare a backtest
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
os.system(cmd)
# the results are the launcher file
orderfn = f"{cn}-order-events.json"
resultfn= f"{cn}.json"
# create results folder
btfolder = str(Path(basedir+"/backtests"))
if not os.path.exists(btfolder):
  os.mkdir(btfolder)

# prepare a report
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
