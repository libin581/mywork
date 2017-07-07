#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import logging
import re

str_trigger_B="A"#触发B程序的字符串
str_trigger_B_pat=re.compile(r"%s"%str_trigger_B) #正则匹配

def main():
    '''主程序入口'''
    
    # 配置日志信息  
    logging.basicConfig(level=logging.DEBUG,  
                        format='%(asctime)s-%(filename)s:%(lineno)s [%(levelname)s] %(message)s',  
                        filename='run.log',  
                        filemode='w')  
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr  
    console = logging.StreamHandler()  
    console.setLevel(logging.INFO)  
    # 设置日志打印格式  
    formatter = logging.Formatter('%(asctime)s-%(filename)s:%(lineno)s [%(levelname)s] %(message)s')  
    console.setFormatter(formatter)  
    # 将定义好的console日志handler添加到root logger  
    logging.getLogger('').addHandler(console)  
          
    
    #参数分析
   
    #调用A程序 
    os.system('echo run A | tee ./A.log') #双向重导向, 屏幕输出同时存在.log中
    logging.info("programe A start successfully")
    
    #循环读取A.log，获取特定触发B程序的字符串
    wait_seconds = 10;
    B_trigged=0;
    for ii in range(wait_seconds):
        if B_trigged==1:
            break
    
        A_LOG   = open('./A.log', "r")
        line = A_LOG.readline()
        while(line):
            if str_trigger_B_pat.search(line):
                #调用B程序 
                os.system('echo run B | tee ./B.log') #双向重导向, 屏幕输出同时存在.log中
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
    
    #日志监控
    
    
if __name__ == "__main__":        
	main()
