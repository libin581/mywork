#!/usr/bin/python
#-*- coding=utf-8 -*-
#script for monitor the disk_usage
import pdb
import pexpect
import threading
#import crypt.py 实现密码密文传输
import crypt
#多线程时，等待子线程结束的时间，单位为秒
wait_time = 120

#解密工具实例化
#encrypt_pwd = crypt.aicrypt(crypt.key)

#远程登录主机，并执行df命令获得存储使用超过90%的分区
def ssh_client(host_ip,user_name,user_pwd):
    prompt = user_name+'%'
    #目前监控主机data0X、billXXX分区存储，可以在$6处新增监控分区
    df_cmd = r"df -h |awk -F'[ %]+' '{if(($6~/data/||$6~/bill/)&&($5>=90)){print $0}}'"
    child = pexpect.spawn('ssh %s@%s'%(user_name,host_ip))
    index = child.expect(['yes/no','assword:'])
    if index == 0:
        child.sendline('yes')
        child.expect('assword:')
        child.sendline(user_pwd)
    elif index == 1:
        child.sendline(user_pwd)
    index = child.expect(['Permission denied',prompt])
    if index == 0:
        print user_name+'@'+host_ip+': password is wrong!'
        return None
    elif index == 1:
        child.sendline(df_cmd)
        child.expect(prompt)
        store_info = child.before.split('\r\n')
        #如果主机没有使用超过90%分区，则返回None
        store_info = [store_info[i] for i in range(len(store_info)) if '\xc8\xa8\xcf\xde\xb2\xbb\xb9\xbb' not in store_info[i]]
        if len(store_info) <=2:
            store_info = None
        child.sendline('exit')
        return store_info

#将存储使用超过90%的主机、分区信息写入文件并打印告警信息
def do_host_store(host_ip,user_name,user_pwd,outFile):
    store_info = ssh_client(host_ip,user_name,user_pwd)
    if store_info == None:
        return 0
    else:
        s = "WARNING : %s@%s storage is over 90 percent!\n"%(user_name,host_ip)
        print s,
        outFile.write(s)
        lock.acquire()
        outFile.write(user_name+'@'+host_ip+'\n')
        for i in xrange(1,len(store_info)-1):
            outFile.write(store_info[i]+'\n')
        outFile.write('\n')
        lock.release()
        return 0
#----------------------------------main--------------------------------------------------
def main(outFile = open('./log/monitor_store.log','w+')):
    threads = []
    global lock
    lock = threading.RLock()
    #打开主机信息配置文件
    fp_host = open('host_list.cfg','r')
    host_info = fp_host.readlines()
    for line in host_info:
        host_list = line.strip().split()
        host_ip = host_list[0]
        user_name = host_list[1]
        user_pwd = host_list[2]
        #user_pwd = encrypt_pwd.decrypt(user_pwd)
        #单线程时用
        # do_host_store(host_ip,user_name,user_pwd)
    ###############################多线程时用begin#####################################
        #创建线程，每个主机一个线程
        t = threading.Thread(target=do_host_store,args=(host_ip,user_name,user_pwd,outFile))
        t.setDaemon(True)
        threads.append(t)
    #启动线程
    for t in threads:
        t.start()
    #等待线程结束,等待时间根据实际修改，单位秒
    for t in threads:
        t.join(wait_time)
    print "All host store check done!"
    fp_host.close()

if __name__ == '__main__':
    main()
