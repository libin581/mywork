#!/usr/bin/env python
 
from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH,
                          ForkingMixIn as FMI)
from time import ctime
 
HOST = ''
PORT = 21577
ADDR = (HOST, PORT)
 
class Server(FMI, TCP):
    pass
 
class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        #self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
        data=raw_input('>')
        self.request.sendall(data)
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
 
tcpServ = Server(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()

