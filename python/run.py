#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import logging
import re

str_trigger_B="A"#����B������ַ���
str_trigger_B_pat=re.compile(r"%s"%str_trigger_B) #����ƥ��

def main():
    '''���������'''
    
    # ������־��Ϣ  
    logging.basicConfig(level=logging.DEBUG,  
                        format='%(asctime)s-%(filename)s:%(lineno)s [%(levelname)s] %(message)s',  
                        filename='run.log',  
                        filemode='w')  
    # ����һ��Handler��ӡINFO�����ϼ������־��sys.stderr  
    console = logging.StreamHandler()  
    console.setLevel(logging.INFO)  
    # ������־��ӡ��ʽ  
    formatter = logging.Formatter('%(asctime)s-%(filename)s:%(lineno)s [%(levelname)s] %(message)s')  
    console.setFormatter(formatter)  
    # ������õ�console��־handler��ӵ�root logger  
    logging.getLogger('').addHandler(console)  
          
    
    #��������
   
    #����A���� 
    os.system('echo run A | tee ./A.log') #˫���ص���, ��Ļ���ͬʱ����.log��
    logging.info("programe A start successfully")
    
    #ѭ����ȡA.log����ȡ�ض�����B������ַ���
    wait_seconds = 10;
    B_trigged=0;
    for ii in range(wait_seconds):
        if B_trigged==1:
            break
    
        A_LOG   = open('./A.log', "r")
        line = A_LOG.readline()
        while(line):
            if str_trigger_B_pat.search(line):
                #����B���� 
                os.system('echo run B | tee ./B.log') #˫���ص���, ��Ļ���ͬʱ����.log��
                logging.info("programe B start successfully")
                B_trigged = 1
                break
            else:
                sleep(1)
                line = A_LOG.readline()
        A_LOG.close()
    
    if B_trigged == 0:
        logging.info("10 seconds eclapse, the trigger string(%s) still not found"%str_trigger_B)
        sys.exit()
    
    #��־���
    
    
if __name__ == "__main__":        
	main()
