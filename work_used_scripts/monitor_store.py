#!/usr/bin/python
#-*- coding=utf-8 -*-
#script for monitor the disk_usage
import pdb
import pexpect
import threading
#import crypt.py ʵ���������Ĵ���
import crypt
#���߳�ʱ���ȴ����߳̽�����ʱ�䣬��λΪ��
wait_time = 120

#���ܹ���ʵ����
#encrypt_pwd = crypt.aicrypt(crypt.key)

#Զ�̵�¼��������ִ��df�����ô洢ʹ�ó���90%�ķ���
def ssh_client(host_ip,user_name,user_pwd):
    prompt = user_name+'%'
    #Ŀǰ�������data0X��billXXX�����洢��������$6��������ط���
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
        #�������û��ʹ�ó���90%�������򷵻�None
        store_info = [store_info[i] for i in range(len(store_info)) if '\xc8\xa8\xcf\xde\xb2\xbb\xb9\xbb' not in store_info[i]]
        if len(store_info) <=2:
            store_info = None
        child.sendline('exit')
        return store_info

#���洢ʹ�ó���90%��������������Ϣд���ļ�����ӡ�澯��Ϣ
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
    #��������Ϣ�����ļ�
    fp_host = open('host_list.cfg','r')
    host_info = fp_host.readlines()
    for line in host_info:
        host_list = line.strip().split()
        host_ip = host_list[0]
        user_name = host_list[1]
        user_pwd = host_list[2]
        #user_pwd = encrypt_pwd.decrypt(user_pwd)
        #���߳�ʱ��
        # do_host_store(host_ip,user_name,user_pwd)
    ###############################���߳�ʱ��begin#####################################
        #�����̣߳�ÿ������һ���߳�
        t = threading.Thread(target=do_host_store,args=(host_ip,user_name,user_pwd,outFile))
        t.setDaemon(True)
        threads.append(t)
    #�����߳�
    for t in threads:
        t.start()
    #�ȴ��߳̽���,�ȴ�ʱ�����ʵ���޸ģ���λ��
    for t in threads:
        t.join(wait_time)
    print "All host store check done!"
    fp_host.close()

if __name__ == '__main__':
    main()
