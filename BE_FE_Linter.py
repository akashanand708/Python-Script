#!/usr/bin/python
import os
import subprocess

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

def runLinter( ):
    os.environ['PATH']
    stream = os.popen(r'git status | grep "new file:\|modified:"')
    changedFileList = stream.readlines()
    prCyan("\nLinting process started for changed javascript and ruby files......\n\n")
    print(stream.read())

    '''
    i.e Let's say, from your root of the project, after doing git status, you see list of changed files
    client/app/parent/components/molecules/ComponentFolder/Component.js
    then you have check based on your codebase, for what file path yarn eslint works,

    Let's say, it works for
    yarn eslint client/app/parent/components/molecules/ComponentFolder/Component.js
    then 'parent/' will be the starting folder.

    '''
    startingFolder = r'app/' # Actual file path starting folder

    frontendStreamList = []
    backendStreamList = []
    for changedFile in changedFileList:
        startingFolderIndex = changedFile.find(startingFolder)
        if (startingFolderIndex > -1):
            actualFilePath = changedFile[startingFolderIndex:len(changedFile) - 1]
            fileType = actualFilePath.lower()
            if(fileType.endswith(".js") or fileType.endswith(".ts") or fileType.endswith(".tsx") ):
                feStreams = os.popen(r'cd client;yarn eslint ' + actualFilePath + r';cd ..;')# We can modify this command based on our requirement to lint frontend files.
                frontendStreamList.append(feStreams)
            elif (fileType.endswith('.rb')):
                beSreams = os.popen(r'rubocop --config .rubocop/test.yml ' + actualFilePath) # We can modify this command based on our requirement to lint backend files.
                backendStreamList.append(beSreams)

    prGreen("FRONTEND FILES PROCESS RESULTS:")
    prGreen("================================\n")
    count = 0
    if(len(frontendStreamList) > 0):
        for festream in frontendStreamList:
            count = int(count) + 1
            prGreen(str(count) + ': ')
            print(festream.read())
    else:
        prBlack("No frontend files to do linting process.")

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    prRed("BACKEND FILES PROCESS RESULTS:")
    prRed("================================\n")
    totalFeBeFileCount = count
    if(len(backendStreamList) > 0):
        count = 0
        for bestream in backendStreamList:
            count = int(count) + 1
            prRed(str(count) + ': ')
            print(bestream.read())
    else:
        prBlack("No backend files to do linting process.\n")
    totalFeBeFileCount += count
    prCyan("\nLinting process completed for total " + str(totalFeBeFileCount) + " javascript and ruby files.\n\n")
            
    return
runLinter()
