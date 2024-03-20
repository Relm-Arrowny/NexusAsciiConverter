'''
Created on 19 Mar 2024


@author: wvx67826

@description:
    Server side of the Neuxs to acsii convertor for GDA atScanEnd scannable. It listen for file name and convert the Neuxs file to acsii and write the data to a processing file.
@useage:
    simple run n2Aserver.py with python will start the server with port 8888
@version: 1.0.0

'''

import socket
import numpy as np
from time import time, sleep
import nexusAsciiConverter
import sys, re

class N2AServer():
    
    def __init__(self, ip ="", port = 8888):
        self.HOST = ip # The server's hostname or IP address
        self.PORT = port  # The port used by the server
        self.serverRunning = False
        self.conn = None
        self.nac = nexusAsciiConverter.nexusAsciiConverter()
    def start(self):
        self.serverRunning = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((self.HOST, self.PORT))
                s.listen()
                self.conn, addr = s.accept()
                print("Connected: %s" %addr)
            except:
                print("fail to start server")
            
            
            while self.serverRunning:
                self.processRequest(s)      
                    

        return True
#=================================================================================
    
    def processRequest(self, s):
        print("waiting for command")
        queued_data = self.conn.recv(1024)
        print(queued_data)
        
        if not queued_data:
            queued_data =  [b"close"]
        else:
            queued_data = queued_data.decode("utf_8")
            temp = re.split(r"(\d+$)", queued_data)
            beamline = re.search(r"(?<=\/dls\/)(.*)(?=\/data)", temp[0])
            self.nac.convert(temp[0] + beamline.group() + "-" +temp[1] +
            ".nxs", temp[0] + "processing/" + beamline.group() +
             "-" +temp[1] + "dat")
            print(temp, beamline)
            
        return True
#=====================================================================================================================
    def sendError(self, errorMessage = "Unknown request"):
        self.conn.sendall(errorMessage.encode("utf_8"))
    
    def sendAck(self):
        sendData = b"1"
        self.conn.sendall(sendData)
        
if __name__== "__main__":
    n2a = N2AServer()
    n2a.start()
    