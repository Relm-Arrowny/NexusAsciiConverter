'''
Created on 19 Mar 2024

@author: wvx67826

@description:
    gda scannable for Nexus acsii converter which will trigger convertion at a n2A converter server, it requires an n2Aclient object and a running n2A server.

@version 1.0
    
'''

from gda.device.scannable import ScannableBase
from gda.device.scannable import ScannableUtils

class N2Ascanable (ScannableBase):
    def __init__(self, name, n2AClient):
        self.setName(name)
        self.setInputNames([name])
        self.setExtraNames([]);
        self.setOutputFormat(["%s"])
        self.currentposition = "N2A On"
        self.n2AClinet = n2AClient
        self.iambusy=0
        self.level = 101

    def isBusy(self):
        return self.iambusy
    
    def asynchronousMoveTo(self):
        pass
        
    def rawGetPosition(self):
        self.iambusy =1
        
        self.iambusy = 0
        return self.currentposition
    def atScanEnd(self):
        self.n2AClinet.sendFileName(lwf())

n2A = N2Ascanable("n2A", n2AC) #for point detector

    