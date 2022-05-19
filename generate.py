
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
import sys

#################################################################################################
# main
#################################################################################################
# useful
toolbox="QuantConnect.Toolbox.exe"

print("ENVIRONMENT:")
print(f"\tDATDIR={DATADIR}")
print(f"\tLEANDIR={LEANDIR}\n")

exedir = f"{LEANDIR}/Toolbox/bin/debug"
if (len(sys.argv)==1) or ("help" in sys.argv[1]):
    os.system(f"{exedir}/{toolbox} --help")
    exit(0)

sys.argv.pop(0)
sargs = " ".join(sys.argv)

# push the configuration file
launcher_template["data-directory"]=str(Path(DATADIR))
launcher_template["cache-location"]=str(Path(DATADIR))
launcher_template[ "data-folder"]=str(Path(DATADIR))
with open(f"{exedir}/config.json","w") as outfile:
    json.dump(launcher_template,outfile,indent=4)
# run the generator
os.system(f"{exedir}/{toolbox} --app RDG "+sargs)

