#! /usr/bin/python
#-*- coding: utf-8 -*-

'''需求：批量查看/对比线上服务器的状态情况，
如uptime、df -h、MD5sum文件等等。
本打算让执行命令通过传参进行、密码通过交互输入（3次不对退出）。
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
    cmd = ['uptime', 'ls']  #执行命令
    username = "libin3"
    passwd = "libin3"
    threads = [4]
    f = file('iplist.txt')  #ip列表
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


