#! /usr/bin/python
#-*- coding: utf-8 -*-

'''���������鿴/�Ա����Ϸ�������״̬�����
��uptime��df -h��MD5sum�ļ��ȵȡ�
��������ִ������ͨ�����ν��С�����ͨ���������루3�β����˳�����
'''

#import paramiko
import sys
import threading
import pexpect
import pxssh

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin,stdout,stderr = ssh.exec_command(m)
            stdin.write("Y")
            out = stdout.readlines()
            for o in out:
                print o,
        print '[OK]%s' %(ip),
        print '========================================================================='
        ssh.close()
    except:
        print '[Error]%s' %(ip),
        print '========================================================================='

def ssh(ip,username,passwd,cmd):
    shell_cmd = 'ssh '+username+'@'+ip
    child = pexpect.spawn(shell_cmd)
    child.logfile=sys.stdout
    child.expect("password: ")
    child.sendline(passwd)
    child.expect("%")
    for m in cmd:
        child.sendline(m)
        child.expect("%")


def main():
    cmd = ['uptime', 'ls']  #ִ������
    username = "libin3"
    passwd = "libin3"
    threads = [4]
    f = file('iplist.txt')  #ip�б�
    while True:
        ip = f.readline()
        if len(ip) == 0:
            break
        #a = threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        a = threading.Thread(target=ssh,args=(ip,username,passwd,cmd))
        a.start()
        
    f.close()      
if __name__ == '__main__':
    main()


