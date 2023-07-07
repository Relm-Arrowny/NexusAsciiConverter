'''
Created on 7 Jul 2023

@author: wvx67826
'''
from src.nexusAsciiConvertor import nexusAsciiConvertor
import os
#for sigle files------------------------------------------------------------------------
M = nexusAsciiConvertor()
filename = 727909
inputFileName = "testData//i10-" +str(filename) +".nxs"
outPutFileName = str(filename) + ".dat"
M.convert(inputFileName, outPutFileName)

#for the whole folder ---------------------------------------------------------------
inPutFolder = "testData//"
outputFolder = "testData//"
for filename in sorted(os.listdir(inPutFolder)):
    if filename[-4:] == ".nxs":
        tempFilename = "%s%s.dat" %(outputFolder,filename[4:-4])  
        exist = os.path.isfile(tempFilename)
        M.convert(inPutFolder+filename, tempFilename)