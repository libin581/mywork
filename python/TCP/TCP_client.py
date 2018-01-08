#!/usr/bin/env python
# -*- coding:utf-8 -*-
#²Î¿¼http://blog.csdn.net/fireroll/article/details/38782757

from socket import *

HOST = 'localhost'
PORT = 21577
BUFSIZE=1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock=socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    #data=raw_input('>')
    #if not data:
    #    break
    data=tcpCliSock.recv(BUFSIZE)
    print data.strip()
    
    tcpCliSock.send('%s\r\n' % data.upper())
    if not data:
        break

    tcpCliSock.close()
