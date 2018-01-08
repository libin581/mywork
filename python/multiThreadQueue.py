#! /usr/bin/python
# -*- coding: utf-8 -*-

import Queue
import sys 
import threading
import time

count = 0;

def worker(name, lock, q, exit_flag):
    while not exit_flag.is_set():
        try:
            # 超时控制，便于及时响应exit_flag
            item = q.get_nowait()
        except Queue.Empty:
            continue
            
        global count
        lock.acquire()
        print('thread {}, item {}, count {}'.format(name, item, count))
        count += 1
        lock.release()
        
        time.sleep(0.1)
        q.task_done()

def main():
    # 线程退出标志位
    exit_flag = threading.Event()
    exit_flag.clear()

    # 创建共享队列和线程池
    q = Queue.Queue()
    num_of_threads = 5 
    RLock = threading.RLock()
    
    threads = [threading.Thread(target=worker, args=(str(i+1), RLock, q, exit_flag))
               for i in range(num_of_threads)]
    
    for i in range(50):
        q.put(i)
    
    for t in threads:
        t.start()

    q.join()

    # 任务处理完成，通知线程退出，并join等待
    exit_flag.set()
    for t in threads:
        t.join()
        
if __name__ == '__main__':
    main()
