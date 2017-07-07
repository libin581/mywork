#! /usr/bin/python
# -*- coding:utf-8 -*-

'''multiprocessing学习'''

import time
import multiprocessing 
from multiprocessing.dummy import Pool as ThreadPool

def worker(i):
    """thread worker function"""
    print 'Worker', i
    time.sleep(0.1)
    print 'Worker', i, 'ww'


lock = multiprocessing.Lock()
def cat(i):
    lock.acquire()
    print "cat", i
    time.sleep(0.1)
    print "cat", i, "cc"
    lock.release()

s = multiprocessing.Semaphore(2)
def cow(i):
    s.acquire()
    print "cow", i
    time.sleep(0.1)
    print "cow", i, "mm"
    s.release()
    
    
if __name__ == '__main__':
    
    print "eg 1, 并行执行,两次输出中间有别的输出"
    proc_record=[]
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        proc_record.append(p);
    for p in proc_record:
        p.join()

    print "\neg 2:并行执行，指定线程池大小，用map简化代码，多核，输出可能是乱序的"
    p1=ThreadPool(4)
    p1.map(worker, range(10))
    p1.close()
    p1.join()

    print "\neg 3:增加锁，两次输出中间不会插入别的输出"
    p2=ThreadPool(4)
    p2.map(cat, range(0,10))
    p2.close()
    p2.join()
        
    print "\neg 4:增加信号量，注意信号量是1和2时，输出是有区别的"
    p3=ThreadPool(4)
    p3.map(cow, range(0,10))
    p3.close()
    p3.join()