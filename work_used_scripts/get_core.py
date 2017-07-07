#!/usr/bin/python
#-*- coding=utf-8 -*-
#本脚本用来检查主机业务流程是否有core

import pexpect
import threading
#import crypt.py 实现密码密文传输
import crypt

#多线程时，等待子线程结束的时间，单位为秒
wait_time = 120
#线程锁
lock = threading.RLock()
#打开core信息记录文件
fp_core = open('./log/core_info.txt','w+')
fp_core.truncate()

#解密工具实例化
#encrypt_pwd = crypt.aicrypt(crypt.key)

#远程登录主机，并执行find命令获得config/run下core文件情况
def ssh_client(host_ip,user_name,user_pwd):
	prompt = user_name+'%'
	#find config/run下core文件情况
	df_cmd = r"""find ./config -type f -name '*core*' -exec ls -l {} \;| awk '{print $(NF-3)$(NF-2)"\t"$(NF-1)"\t"$NF}'"""
	child = pexpect.spawn('ssh %s@%s'%(user_name,host_ip))
	index = child.expect(['(?i)yes/no','(?i)password:'])
	if index == 0:
		child.sendline('yes')
		child.expect('(?i)assword:')
		child.sendline(user_pwd)
	elif index == 1:
		child.sendline(user_pwd)
	index = child.expect(['(?i)Permission denied',prompt])
	if index == 0:
		print user_name+'@'+host_ip+': password is wrong!'
		return None
	elif index == 1:
		child.sendline(df_cmd)
		child.expect(prompt)
		core_info = child.before.split('\r\n')
		#如果主机没有业务流程core，则返回None
		if len(core_info) <=2:
			core_info = None
		child.sendline('exit')
		return core_info

#将业务流程core信息写入文件
def do_core(host_ip,user_name,user_pwd):
	core_info = ssh_client(host_ip,user_name,user_pwd)
	if core_info == None:
		return 0
	else:
		lock.acquire()
		for i in xrange(1,len(core_info)-1):
			warn_content = '%-20s%-30s\n'%(host_ip,core_info[i])
			print warn_content,
			fp_core.write(warn_content)
		fp_core.write('#'*80+'\n')
		lock.release()
		return 0

#定义main函数
def main():
	threads = []
	#打开主机信息配置文件
	fp_host = open('host_list.cfg','r')
	s = 'HOST                DATE        TIME      POSITION\n'
	print s,
	fp_core.write(s)
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
		t = threading.Thread(target=do_core,args=(host_ip,user_name,user_pwd))
		t.setDaemon(True)
		threads.append(t)
	#启动线程
	for t in threads:
		t.start()
	#等待线程结束,等待时间根据实际修改，单位秒
	for t in threads:
		t.join(wait_time)
	print "All host core check done!"
	fp_host.close()
	fp_core.close()

#-------------------------------------------main--------------------------------------
if __name__ == '__main__':
    main()
