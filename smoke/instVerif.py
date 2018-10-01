#=================================================
#  Synopsys Inc. 2018
#  Authors:  Joel Sheppard
#  Purpose: basic OpsSight install smoke test
#=================================================

import os
import shutil
import subprocess
from sys import argv

# First install OpsSight; ask for a Black Duck key and version to install
#=================================================
####    Try to make the below into a func     ####
#=================================================
def keyver():
    print("Please type in your BlackDuck Key")
    key = input()
    print("What version of OpsSight would you like to install?")
    opsightVer = input()
    print(f"We're going to use the Key: {key} and will install OpsSight version: {opsightVer}.  Is this okay?")
    user_answer = input()

# print("Please type in your BlackDuck Key.")
# key = input()
# print("What version of OpsSight do you want to install?")
# opsightVer = input()
# print(f"We're going to use the BlackDuck key: {key}, and will install OpsSight version: {opsightVer}.  Is this okay?")
# user_answer = input()

# Check answer for Yes/No/Neither and do something based on users answer
    if user_answer == "Yes":
        subprocess.Popen(['/Users/shepp/workspace-opsight-2.1.x/opssight-connector/install/kube/install.sh', 'key', 'opsightVer'])
    elif user_answer == "No":
        #go back and start questioning over - how?
        print("Well, this means you'll have to start over.")
        keyver()
    else:
        print("ERROR! Acceptable answers are Yes or No only.")