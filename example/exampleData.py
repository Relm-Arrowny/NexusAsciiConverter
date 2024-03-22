'''
Created on 7 Jul 2023

@author: wvx67826
'''
from src.nexusAsciiConverter import nexusAsciiConverter
import time, os, re


#for single files------------------------------------------------------------------------
M = nexusAsciiConverter()

# input/output file name
filename = 727909   
inputFileName = "testData//i10-" +str(filename) +".nxs"

outPutFileName = str(filename) + ".dat"

#Do the conversion 
M.convert(inputFileName, outPutFileName)



#Same as above but for the entire folder ---------------------------------------------------------------
inPutFolder = "testData/"
outputFolder = "testData/"
for filename in sorted(os.listdir(inPutFolder)):
    if filename[-4:] == ".nxs": #only work on .nxs extension 
        tempFilename = "%s%s.dat" %(outputFolder,filename[4:-4])  
        exist = os.path.isfile(tempFilename)
        M.convert(inPutFolder+filename, tempFilename)
        

"""
# forever loop----------------

inPutFolder =  "testData/"
outputFolder = ""
newScanNo = 818041
lastScanNo = 817547
timeOut = 0
retryFlag = False
while timeOut < 24*3600:
    if retryFlag:
        time.sleep(88)
        inputFile = inPutFolder+"i10-"+ str(newScanNo) + ".nxs"
        outputFile = outputFolder + "i10-" + str(newScanNo) + ".dat"
        try:
            M.convert(inputFile, outputFile)
            retryFlag = False
        except OSError:
            print("scan running: %i" %newScanNo)
            retryFlag = True
        
        
    elif newScanNo == lastScanNo:
        if retryFlag:
            lastScanNo -= 1
            retryFlag = False
        print (lastScanNo)
        time.sleep(88)
        timeOut = timeOut+88
        newScanNo = int(re.split("-|.nxs" ,sorted(os.listdir(inPutFolder))[-5])[1])
       
    else:
        for filename in range(newScanNo,lastScanNo-1,-1):
            inputFile = inPutFolder+"i10-"+ str(filename) + ".nxs"
            outputFile = outputFolder + "i10-" + str(filename) + ".dat"
            print(inputFile, outputFile)
            try:
                M.convert(inputFile, outputFile)
            except FileNotFoundError:
                print("no scan: %i" %filename)
            except OSError:
                print("scan running: %i" %filename)
                retryFlag = True
        lastScanNo = newScanNo
        timeOut = 0
    """