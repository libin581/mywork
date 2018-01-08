#! /usr/bin/python
# -*- coding: utf-8 -*-

import fcntl 
import os
import threading

FILE = "./counter.txt"  


def writeFile(a):
	FILE_WRITE = open(FILE, 'a') #����flock���ɵ���Ȱ������������ֹ���̶��ļ��Ĳ�����������������������ļ�  
	fcntl.flock(FILE_WRITE.fileno(), fcntl.LOCK_EX) #Ϊ�˱���ͬʱ�����ļ�����Ҫ�����Լ��������ļ��Ƿ��Ѿ������������������鵽�����ˣ����̻ᱻ����   

	for i in range(9):  
		counter = a+i  
		FILE_WRITE.write(str(counter)+'\n')
		FILE_WRITE.flush()
	fcntl.flock(FILE_WRITE.fileno(), fcntl.LOCK_UN)
	FILE_WRITE.close() # unlocks the file  
			
def main():
    threads = []
    #�����̣߳�ÿ������һ���߳�
    t = threading.Thread(target=writeFile,args=(10,))
    t.setDaemon(True)
    threads.append(t)

    t = threading.Thread(target=writeFile,args=(20,))
    t.setDaemon(True)
    threads.append(t)

    #�����߳�
    for t in threads:
        t.start()
		
    #�ȴ��߳̽���,�ȴ�ʱ�����ʵ���޸ģ���λ��
    for t in threads:
        t.join()
			
if __name__ == '__main__':
    main()
