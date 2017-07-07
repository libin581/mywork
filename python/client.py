#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, sys
reload(sys)
sys.setdefaultencoding('utf-8')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sock.connect(('localhost', 8001));  

my_str=''
for i in range(1, len(sys.argv)):
     my_str += sys.argv[i]
print my_str+":" + repr(my_str)
my_str = my_str.decode('utf-8')
print my_str+":" + repr(my_str)

sock.send(my_str.decode('utf-8'))

szBuf = sock.recv(1024)
print "recv" + szBuf
sock.close()
print "end of connect"