'''
Created on 7 Jul 2023

@author: wvx67826
'''

import h5py    # HDF5 support
import numpy as np
import collections.abc

class nexusAsciiConverter():
    def __init__(self):
        self.clearData()
    
    def visitData(self, name, node):
        if isinstance(node, h5py.Dataset):
            if (not node.shape):
                self.metaName.append(name)
                self.metaValue.append(node[()])
            else:
                self.dataName.append (name)
                self.dataValue.append(node[()])
                if (node[()].size > self.longestData):
                    self.longestData = node[()].size 
        return None
    
    def loadData(self, filename):
        self.nexusData = h5py.File(filename, "r")
   
    def storeData(self):
        self.nexusData.visititems(self.visitData)
        
    def writeAscii(self, filename):
        f = open(filename, 'w+')
        
        for i in range(len(self.metaName)):
                f.write("%s = %s" %(self.metaName[i],self.metaValue[i]))
                f.write("\n" )
        for i in self.dataName:
            f.write("%s \t" %i)
        f.write("\n" )
        for j in range (0,self.longestData):
            for k in range (0,len(self.dataValue)):

                if j<len(self.dataValue[k]):
                    f.write("%s \t" %self.dataValue[k][j])
                else:
                    f.write("0 \t")
            f.write("\n" )
        f.close()
    
    def convert(self, inputFileName, outPutFileName):
        self.clearData()
        self.loadData(inputFileName)
        self.storeData()
        self.writeAscii(outPutFileName)
    
    def clearData(self):
        self.metaName = []
        self.metaValue = []
        self.dataName = []
        self.dataValue = []
        self.nexusData = None
        self.longestData = 0
        
        