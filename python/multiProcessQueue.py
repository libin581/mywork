#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys 
import multiprocessing
import time

def worker(name, lock, count, dct, q, exit_flag):
    while not exit_flag.is_set():
        if not q.empty():
            # ��ʱ���ƣ����ڼ�ʱ��Ӧexit_flag
            item = q.get_nowait()
            
            lock.acquire()
            print('process {}, item {}, count {}'.format(name, item, count.value))
            dct[str(item)] = count.value
            count.value += 1
            lock.release()
            
            time.sleep(0.1)
            q.task_done()

def main():
    # �߳��˳���־λ
    exit_flag = multiprocessing.Event()
    exit_flag.clear()

    # ����������к��̳߳�
    manager = multiprocessing.Manager()
    q = manager.Queue()
    num_of_processes = 5 
    lock = multiprocessing.Lock()
    
    count = multiprocessing.Value('d', 0)
    
    aa={}
    aa["aa"] = 1
    aa["bb"] =2 
    dct = manager.dict(aa)
    
    processes = [multiprocessing.Process(target=worker, args=(str(i+1), lock, count, dct, q, exit_flag))
               for i in range(num_of_processes)]
    
    for i in range(50):
        q.put(i)
    
    for ps in processes:
        ps.start()

    q.join()

    # ��������ɣ�֪ͨ�߳��˳�����join�ȴ�
    exit_flag.set()
    for ps in processes:
        ps.join()
        
    print dct 
        
if __name__ == '__main__':
    main()
