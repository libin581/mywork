#!/usr/bin/env python
# -*- coding:utf-8 -*-
#²Î¿¼http://blog.csdn.net/fireroll/article/details/38782757

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        data=raw_input('>')
        self.request.sendall(data)
        
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 21577
    # Create the server, binding to localhost on port 21577
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print " .... waiting for connection"

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()