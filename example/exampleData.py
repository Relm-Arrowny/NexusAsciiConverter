'''
Created on 7 Jul 2023

@author: wvx67826
'''
from src.nexusAsciiConvertor import nexusAsciiConvertor
import os
#for single files------------------------------------------------------------------------
M = nexusAsciiConvertor()

# input/output file name
filename = 727909   
inputFileName = "testData//i10-" +str(filename) +".nxs"

outPutFileName = str(filename) + ".dat"

#Do the conversion 
M.convert(inputFileName, outPutFileName)

#Same as above but for the entire folder ---------------------------------------------------------------
inPutFolder = "testData//"
outputFolder = "testData//"
for filename in sorted(os.listdir(inPutFolder)):
    if filename[-4:] == ".nxs": #only work on .nxs extension 
        tempFilename = "%s%s.dat" %(outputFolder,filename[4:-4])  
        exist = os.path.isfile(tempFilename)
        M.convert(inPutFolder+filename, tempFilename)