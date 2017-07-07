#!/usr/bin/python
#-*- coding=utf-8 -*-
#���ű������������ҵ�������Ƿ���core

import pexpect
import threading
#import crypt.py ʵ���������Ĵ���
import crypt

#���߳�ʱ���ȴ����߳̽�����ʱ�䣬��λΪ��
wait_time = 120
#�߳���
lock = threading.RLock()
#��core��Ϣ��¼�ļ�
fp_core = open('./log/core_info.txt','w+')
fp_core.truncate()

#���ܹ���ʵ����
#encrypt_pwd = crypt.aicrypt(crypt.key)

#Զ�̵�¼��������ִ��find������config/run��core�ļ����
def ssh_client(host_ip,user_name,user_pwd):
	prompt = user_name+'%'
	#find config/run��core�ļ����
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
		#�������û��ҵ������core���򷵻�None
		if len(core_info) <=2:
			core_info = None
		child.sendline('exit')
		return core_info

#��ҵ������core��Ϣд���ļ�
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

#����main����
def main():
	threads = []
	#��������Ϣ�����ļ�
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
		#���߳�ʱ��
		# do_host_store(host_ip,user_name,user_pwd)
	###############################���߳�ʱ��begin#####################################
		#�����̣߳�ÿ������һ���߳�
		t = threading.Thread(target=do_core,args=(host_ip,user_name,user_pwd))
		t.setDaemon(True)
		threads.append(t)
	#�����߳�
	for t in threads:
		t.start()
	#�ȴ��߳̽���,�ȴ�ʱ�����ʵ���޸ģ���λ��
	for t in threads:
		t.join(wait_time)
	print "All host core check done!"
	fp_host.close()
	fp_core.close()

#-------------------------------------------main--------------------------------------
if __name__ == '__main__':
    main()
