#! /usr/bin/python
# -*- coding: utf-8 -*-

import fcntl 
import os
import threading

FILE = "./counter.txt"  


def writeFile(a):
	FILE_WRITE = open(FILE, 'a') #由于flock生成的是劝告锁，不能阻止进程对文件的操作，所以这里可以正常打开文件  
	fcntl.flock(FILE_WRITE.fileno(), fcntl.LOCK_EX) #为了避免同时操作文件，需要程序自己来检查该文件是否已经被加锁。这里如果检查到加锁了，进程会被阻塞   

	for i in range(9):  
		counter = a+i  
		FILE_WRITE.write(str(counter)+'\n')
		FILE_WRITE.flush()
	fcntl.flock(FILE_WRITE.fileno(), fcntl.LOCK_UN)
	FILE_WRITE.close() # unlocks the file  
			
def main():
    threads = []
    #创建线程，每个主机一个线程
    t = threading.Thread(target=writeFile,args=(10,))
    t.setDaemon(True)
    threads.append(t)

    t = threading.Thread(target=writeFile,args=(20,))
    t.setDaemon(True)
    threads.append(t)

    #启动线程
    for t in threads:
        t.start()
		
    #等待线程结束,等待时间根据实际修改，单位秒
    for t in threads:
        t.join()
			
if __name__ == '__main__':
    main()
