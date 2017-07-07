#!/usr/bin/python
# -*- coding:utf-8 -*-

if "__main__" == __name__:
    import socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        print("create socket succ!");
        
        sock.bind(('localhost', 8001));
        print("bind socket succ!");
        
        sock.listen(5);
        print("listen succ!");

    except:
        print("init socket err!");

    while True:
        print("listen for client...");
        conn, addr = sock.accept(); #����conn���µ�socket���������Ͽ��Է��ͺͽ������ݣ�address����һ�˵�socket��ַ</span></strong>
        print("get client");
        print(addr);
            
        conn.settimeout(5);
        szBuf = conn.recv(1024);#ʹ��sock.accept()������socket����
        print("recv:" + szBuf);
        print("recv:" + repr(szBuf));

        if "0" == szBuf:
            conn.send('exit');
        else:
            conn.send('welcome client!');

        conn.close();
        print("end of sevice");
    
    sock.close()