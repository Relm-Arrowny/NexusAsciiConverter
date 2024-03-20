'''
Created on 19 Mar 2024
172.23.110.74 
@author: wvx67826
@Description:
    Client class that intended to be run within GDA to communicate with the Neuxs ascii converter server
    Running this script will automatically create an client objects.

'''

from beamline.TCL_Controls.TCPSocket.TCPSocket import TCPSocket


class N2AClient(TCPSocket):
    def __init__(self, bufferSize = 4096, timeout = 5):
        super(N2AClient, self).__init__(bufferSize, timeout)
    def sendFileName(self, value):
        com = "%s" %value
        self.sendCom(com)
        return 1#self.readBuffer()

#================== get data ==============================================================

HOST = "172.23.110.74" # The server's hostname or IP address for Hutch Windows computer
PORT = 8888  # The port used by the server
#172.23.110.69
n2AC = N2AClient(bufferSize = 2048, timeout = 15)
print(n2AC.connection(HOST, PORT))