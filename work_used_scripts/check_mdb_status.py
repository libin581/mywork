#!/usr/bin/python
#coding=utf-8

import pexpect
import os

config_path = './mdb_config.cfg'

#远程登录主机，并执行mdb_client命令
def ssh_client(host_ip,user_name,user_pwd):
    prompt = user_name+'%'
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
        print "login to %s success."%(host_ip)
        print "----------------------------------------"
        mdb_status_check(child)


def mdb_config():
    f = open(config_path)
    fl = f.readlines()
    f.close()
    mdb_configs = []
    for i in fl:
        mdb_configs.append(i.strip().split())
    return mdb_configs


def mdb_status_check(child, outFile = open('./log/mdb_status_check.log','w+')):
    mdb_configs = mdb_config()
    warning = []
    for config in mdb_configs:
        mdb_name = config[0]
        port = config[1]
        ipaddress = config[2]
        status = config[3]
        try:
            s = 'mdb_client %s %s '%(ipaddress,port)
            print s
            child.sendline(s)
            index = child.expect(['Input user: ','mdb>> ',pexpect.EOF, pexpect.TIMEOUT])
            if index == 0:
                child.sendline('billmdb')
                child.expect('password: ')
                child.sendline('billmdb')
                child.expect('mdb>> ')
            elif index == 1:
                pass
            child.sendline('info mdb')
            child.expect('mdb>> ')
            text = child.before.split('\n')
            flag = 0
            for i in text:
                if i.startswith('mdb role'):
                    #print "%s %s : %s"%(mdb_name,ipaddress,i.strip().split()[-1])
                    if i.strip().split()[-1] != status:
                        text = """%-20s%-10s%-10s\n"""%(mdb_name,i.strip().split()[-1].upper(),status.upper())
                        warning.append(text)
                    flag = 1
            if flag == 0:
                print "%s %s : unknown"%(mdb_name,ipaddress)
                text = """%-20sUnknown   %-10s\n"""%(mdb_name,status.upper())
                warning.append(text)
        except Exception:
            #print "%s %s : down"%(mdb_name,ipaddress)
            text = """%-20sDown      %-10s\n"""%(mdb_name,status.upper())
            warning.append(text)
        finally:
            child.close()
    if warning != []:
        print "-------------------------------------"
        s = 'MDB_NAME            STATUS    EXPECTING \n'
        print s,
        outFile.write(s)
        for i in warning:
            print i,
            outFile.write(i)
    else:
        s = "The statuses of all MDB are normal as expect!\n"
        print s,
        outFile.write(s)

if __name__ == '__main__':
    host_ip = '10.10.12.146'
    user_name = 'gxbillcs'
    user_pwd = 'qatest2016'
    ssh_client(host_ip,user_name,user_pwd)
