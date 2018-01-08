#! /usr/bin/python
# -*- coding: utf-8 -*-

#from kafka import KafkaProducer
#from kafka import KafkaConsumer
#from kafka.errors import KafkaError
import json
import os
import time
import sys
import re
import pdb
import logging
import threading
import Queue
from datetime import datetime
#import cx_Oracle

#msg id
CHECK_ENV_REQ_MSG  = 999
CHECK_ENV_RESP_MSG = 998
SEND_LOG_DATA_MSG  = 997

#unit: second 
CHECK_ENV_INTERVAL_TIME = 10 
COLLECT_DATA_INTERVAL_TIME =6*60*60#
LINE_NUMBER_PER_TIME = 100 

NUM_OF_THREADS = 1

masterList=["127.0.0.1:9092"]#master

#slave ip_port list
slaveList = []
slaveList.append("127.0.0.1:9092")
#slaveList.append("127.0.0.1:9094")

end_flag = "--end--"
end_flag_pat = re.compile(r"%s"%(end_flag))
tb_pat  = re.compile(r"\_tb\_")
idx_pat = re.compile(r"\.idx$")
hide_pat = re.compile(r"^\.")
log_time_pat = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
file_time_pat = re.compile(r"\d{4}-\d{2}-\d{2}") #2017-07-25

FILE_OFFSET = {}

TEST_MODE = 0

if TEST_MODE:
    LOG_DIR = './testData/'
else:
    LOG_DIR = os.environ.get( 'LOGPATH')
    LOG_DIR += '/decode'
    
class Kafka_producer():
    '''
    使用kafka的生产模块
    '''

    def __init__(self, kafkahost,kafkaport, kafkatopic):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers = '{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort
            ))

    def sendjsondata(self, params):
        try:
            parmas_message = json.dumps(params)
            producer = self.producer
            producer.send(self.kafkatopic, parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print e

class Kafka_consumer():
    '''
    使用Kafka—python的消费模块
    '''

    def __init__(self, kafkahost, kafkaport, kafkatopic, groupid):
        self.kafkaHost = kafkahost
        self.kafkaPort = kafkaport
        self.kafkatopic = kafkatopic
        self.groupid = groupid
        self.consumer = KafkaConsumer(self.kafkatopic, group_id = self.groupid,
                                      bootstrap_servers = '{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort ))

    def consume_data(self):
        try:
            for message in self.consumer:
                # print json.loads(message.value)
                yield message
        except KeyboardInterrupt, e:
            print e

def db_conn():
    #连接数据库
    logging.info(" Connecting to database...")
    ora_ip='10.10.10.120'
    ora_port='1521'
    instance_name='ora10'
    ora_dsn=cx_Oracle.makedsn(ora_ip,ora_port,instance_name)
    #流程配置存放在id用户，以id用户登录数据库
    logging.info( ora_dsn)
    #conn = cx_Oracle.connect('id','id',ora_dsn)
    conn = cx_Oracle.connect('id/id@10.1.245.131/ora10')
    logging.info("slave: Database connected!")
    
    return conn
            
def getKeyWordSet():
    #连接数据库
    conn = db_conn()
    cursor = conn.cursor()

    query_sql = '''select * from LOG_KEY_WORD_SET a order by a.MODULE'''
    logging.info(query_sql)

    cursor.execute(query_sql)
    result = cursor.fetchall()
    count = cursor.rowcount

    logging.info("Total key word record number:%d"%(count))
    for row in result:
        row_list = list(row)
        logging.info( row_list )

    cursor.close
    conn.close()
    
    return keyWordSet

def getTimeFromFile(dataFile): #返回以秒为单位的时间
    dataFile = os.path.basename(dataFile)
    items = dataFile.split('_')
    start_time = items[-2]
    end_time = items[-1]
    start_time = time.mktime((int(start_time[0:4]), 
                              int(start_time[4:6]), 
                              int(start_time[6:8]),
                              int(start_time[8:10]),
                              int(start_time[10:12]),
                              0,0,0,0))
    end_time = time.mktime((int(end_time[0:4]), 
                            int(end_time[4:6]), 
                            int(end_time[6:8]), 
                            int(end_time[8:10]), 
                            int(end_time[10:12]),
                            0,0,0,0))
    return start_time, end_time
    
def getFirstLineTime(file):
    line_time = 0
    with open(file, 'r') as READ_FILE:
        line = READ_FILE.readline()
        log_time_search = log_time_pat.search(line)
        if log_time_search:
            line_time = log_time_search.group()
            line_time = getSecTime(line_time)
        else:
            line = READ_FILE.readline()
            
    return line_time
    
def skipFile(file):
    if tb_pat.search(file) or \
        idx_pat.search(file) or \
        hide_pat.search(file):
        return True
    else:
        return False

    
def getDataFile():
    #找到最近改动的文件
    latest_file_time = 0
    latest_file = ''
    for  root, dirs,files in os.walk('./data/'):
        for file in files:
            file = os.path.join(root,file)
            if os.path.getmtime(file) > latest_file_time:
                latest_file_time = os.path.getmtime(file)
                latest_file = file
    if latest_file:
        logging.info('the latest data file is %s'%(latest_file))
        with open(latest_file, "r") as READ_FILE:
            lines = READ_FILE.readlines()
            if lines and end_flag_pat.search(lines[-1]):#上次处理完了，新建一个文件接着处理
                logging.info('the latest data file is complete')
                (last_start_time, last_end_time) = getTimeFromFile(latest_file)
                end_time = last_end_time + COLLECT_DATA_INTERVAL_TIME
                end_time   = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(end_time))
                start_time = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(last_end_time))
                data_file='data/logKeyWord_' + start_time + '_' + end_time
            else:#上次没有处理完，继续处理
                logging.info('the latest data file is not complete')
                data_file = latest_file

    else:#没有日志记录文件，从头开始收集
        earliest_time = time.time()
        earliest_file = []
        logging.info('LOG_DIR:%s'%(LOG_DIR))
        for  root, dirs,files in os.walk(LOG_DIR):
            for file in files:
                if skipFile(file):
                    continue
                
                file = os.path.join(root,file)
            
                #file = os.path.join(root,file)
                #READ_FILE = open(file, "r")
                #first_line=READ_FILE.readline()
                #log_time_search = log_time_pat.search(first_line)
                #if log_time_search:
                #    first_line_time = log_time_search.group()
                #    first_line_time = getSecTime(first_line_time)
                #    if first_line_time < earliest_time:
                #        earliest_time = first_line_time 
                #READ_FILE.close()

                if earliest_time > os.path.getmtime(file):
                    earliest_time = os.path.getmtime(file)
                    earlist_file = file

                first_line_time = getFirstLineTime(earlist_file)
                if first_line_time < earliest_time:
                    earliest_time = first_line_time 
                    
        start_time = earliest_time//3600*3600
        end_time   = start_time + COLLECT_DATA_INTERVAL_TIME
        start_time = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(start_time))
        end_time   = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(end_time))
        data_file  = 'data/logKeyWord_' + start_time + '_' + end_time
        
    (start_time, end_time) = getTimeFromFile(data_file)
    start_time = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(start_time))
    end_time   = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(end_time))
    logging.info("collect data from %s to %s"%(start_time, end_time))
    
    return data_file
         
def getSecTime(timeIn):#把datetime转成以秒为单位的time, 精确到秒
    date_time = datetime.strptime(timeIn, '%Y-%m-%d %H:%M:%S')
    timeSec = time.mktime(date_time.timetuple())
    return timeSec
         
def procFile(word_count, keyWords, start_time, end_time, file):
    global FILE_OFFSET
    baseFile = os.path.basename(file)
    with open(file, "r") as READ_FILE:
        if FILE_OFFSET.has_key(baseFile):
            READ_FILE.seek(FILE_OFFSET[baseFile])
        lines     = []
        timeFlag  = False
        line      = READ_FILE.readline()
        offset = 0
        while line:
            offSet = READ_FILE.tell()
            
            log_time_search = log_time_pat.search(line)
            if log_time_search:
                log_time  = log_time_search.group()
                if getSecTime(log_time) >= end_time:
                    timeFlag = True
            else:
                line = READ_FILE.readline()
                continue
        
            if not timeFlag:
                lines.append(line)
            
            line = READ_FILE.readline()
            
            if len(lines) >= LINE_NUMBER_PER_TIME or not line or timeFlag:
                wordList = []
                for ln in lines:
                    wordList += ln.split()
                #logging.info("%d, %d"%(len(lines), len(wordList)))
                for keyWord in keyWords:
                    wordCount = wordList.count(keyWord);
                    if wordCount != 0:
                        if word_count.has_key(keyWord):
                            word_count[keyWord] += wordCount 
                        else:
                            word_count[keyWord] = wordCount
                lines=[]
                
            if timeFlag:
                break
                
        if not line: 
            if file_time_pat.search(baseFile): #已切割日志文件的最后，删除offset
                if FILE_OFFSET.has_key(baseFile):
                    del FILE_OFFSET[baseFile]
        else:
            FILE_OFFSET[baseFile] = offSet

def writeFile(WRITE_FILE, word_count, flow):
    WRITE_FILE.write('flow:'+flow)
    for keyWord in word_count.keys():
        WRITE_FILE.write(','+keyWord+':'+str(word_count[keyWord]))
    WRITE_FILE.write('\n')
         
def procFlow(data_file, lock, keyWordSet, q, exit_flag):
    while not exit_flag.is_set():
        try:
            # 超时控制，便于及时响应exit_flag
            flowDir = q.get_nowait()
        except Queue.Empty:
            continue
            
        dir_list = flowDir.split('/')
        flow = dir_list[-1]
        module = dir_list[-2]
        keyWords = keyWordSet[module]
        #lock.acquire()
        if not keyWords:
        #    logging.info('keyWords are null for module %d'%(module))
            continue
        #else:
        #    logging.info('flow %s in module %s is proccessing, keyWords are {%s}'%(flow, module, keyWords))
        #lock.release()

        keyWords = keyWords.split(';')
        word_count = {}
        (start_time, end_time) = getTimeFromFile(data_file)
        for  root, dirs, files in os.walk(flowDir):
            for file in files: 
                if skipFile(file):
                    continue
                    
                file = os.path.join(root,file)
                if not TEST_MODE:
                    first_line_time = getFirstLineTime(file)
                    if first_line_time >= end_time or os.path.getmtime(file) < start_time or \
                        os.path.getsize(file) < 1:
                        continue
                        
                #lock.acquire()
                #logging.info("process file %s"%(file))
                #lock.release()
                procFile(word_count, keyWords, start_time, end_time, file)
                
            if word_count:
                #lock.acquire()
                with open(data_file,'a') as WRITE_FILE:
                    writeFile(WRITE_FILE, word_count, flow)
                #lock.release()
        q.task_done()        
    
def procLogDir(data_file, keyWordSet, flows, isComplete):
    # 线程退出标志位
    exit_flag = threading.Event()
    exit_flag.clear()

    # 创建共享队列和线程池
    q = Queue.Queue()
    
    for  root, dirs, files in os.walk(LOG_DIR):
        if not files:
            continue
        
        dir_list = root.split('/')
        flow = dir_list[-1]
        if not isComplete and flow in flows:
            continue
            
        q.put(root)
            
    RLock = threading.RLock()
    threads = [threading.Thread(target=procFlow, args=(data_file, RLock, keyWordSet, q, exit_flag))
               for i in range(NUM_OF_THREADS)]

    for t in threads:
        t.start()
    
    q.join()

    # 任务处理完成，通知线程退出，并join等待
    exit_flag.set()
    for t in threads:
        t.join()

    with open(data_file,'a') as WRITE_FILE:
        WRITE_FILE.write(end_flag)
         
def getLogData(keyWordSet):
    data_file = getDataFile()
    data_file = os.path.basename(data_file)
    data_file = 'data/' + data_file
    (start_time, end_time) = getTimeFromFile(data_file)
    curr_time = time.time()
    if end_time > curr_time:
        curr_time = time.strftime('%4Y%2m%2d%2H%2M',time.localtime(curr_time))
        logging.info('end time is bigger than current time %s'%(curr_time))
        return data_file
    
    if os.path.exists(data_file):
        #统计上次未完成文件中的流程
        READ_FILE = open(data_file,'r')
        lines = READ_FILE.readlines()
        flows=[]
        for line in lines: #格式如：flow:de_sms_hw, warn:5
            items = line.split(':')
            flow  = items[0].strip()
            if flow not in flows:
                flows.append(flow)
        READ_FILE.close()
     
        procLogDir(data_file, keyWordSet, flows, False)
    else:
        logging.info('creat new file: %s'%(data_file))

        procLogDir(data_file, keyWordSet, [], True)
        
    return data_file
    
            
def recvMsg(identity):
    if identity == 'master':
        logging.info("I'm master to recv msg")
        #msg no
        #consumer = Kafka_consumer('127.0.0.1', '9092', 'logKeyVal', 'python-logKeyVal')
        #message = consumer.consume_data()
        #for m in message:
        #    logging.info(m.value+" received")
            
        # analysis
        
        # load into database
        while True:
            time.sleep(CHECK_ENV_INTERVAL_TIME)
        
    else:#identity == 'slave':
        logging.info("I'm slave to recv msg")
        #msg no
        #consumer = Kafka_consumer('127.0.0.1', 9092, "logKeyVal", 'python-logKeyVal')
        #message = consumer.consume_data()
        #for m in message:
        #    logging.info(m.value+" received")
        
        #    # check env
        #    
        #    #send 
        #    msg='msgId:%d'%(CHECK_ENV_RESP_MSG)
        #    ip, port = masterList[0].split(":")
        #    kafkaSend(ip, '9093', "logKeyVal", msg)
        #    logging.info(msg+ " sended")

def sendMsg(identity):
    if identity == 'master':
        logging.info("I'm master to send msg")
        #producer = Kafka_producer("127.0.0.1", 9092, "logKeyVal")
        #while True:
            # send CHECK_ENV_REQ_MSG to slave every CHECK_ENV_INTERVAL_TIME
        #    msg='msgId:%d'%(CHECK_ENV_REQ_MSG)
        #    producer.sendjsondata(msg)
        #    logging.info("master: send msg "+msg)
        #    time.sleep(CHECK_ENV_INTERVAL_TIME)
    else:#identity == 'slave'
        #logging.info("I'm slave to send msg")
        
        if not os.path.exists('./data'):
            os.makedirs('./data')
        
        #producer = Kafka_producer("127.0.0.1", 9092, "logKeyVal")
        
        #collect log data every COLLECT_DATA_INTERVAL_TIME
        while True:
            startTime = time.clock()
            #get key words from database
            #keyWordSet=getKeyWordSet()           
            keyWordSet={}
            keyWordSet['decode'] = 'failed;error'
            #get log data
            data_file = getLogData(keyWordSet)
            #send SEND_LOG_DATA_MSG
            if os.path.exists(data_file):
                READ_FILE = open(data_file, "r")
                lines = READ_FILE.readlines()
                if end_flag_pat.search(lines[-1]):
                    lines.pop()
                    for line in lines:
                        msg='msgId:%d,%s'%(SEND_LOG_DATA_MSG, line.strip())
                        #producer.sendjsondata(msg)
                        logging.info("slave: send msg, "+ msg)
                READ_FILE.close()
                endTime = time.clock()
                logging.info('collect data for file %s eclapses %f seconds'%(data_file, endTime-startTime))
            
                for file in FILE_OFFSET.keys():
                    logging.info('file:%s, offset:%d'%(file, FILE_OFFSET[file]))
            
            (start_time, end_time) = getTimeFromFile(data_file)
            if time.time() - end_time < COLLECT_DATA_INTERVAL_TIME:
                logging.info("sleeping ...")
                time.sleep(COLLECT_DATA_INTERVAL_TIME)

def usage():
    logging.info('''
    usage:
    This script is used to collect key words of logs and load to database,
    can be used by master and slave machines.
    usage:
    python log_key_word.py         : help info
    python log_key_word.py --help  : help info
    python log_key_word.py -h      : help info
    python log_key_word.py master  : used for master machines
    python log_key_word.py slave   : used for slave machines
    ''')

def main():
    '''
    日志关键字系统脚本，master和slave用同一套脚本，用入参区分，方便部署
    日志记录文件命名形如：data/logKeyWord_201707250900_201707251000
    '''
    
    if not os.path.exists('./log'):
        os.makedirs('./log')
    
    
    # 配置日志信息  
    logging.basicConfig(level=logging.DEBUG,  
                        format='%(asctime)s [%(levelname)s] %(message)s',  
                        #datefmt='%y-%m-%d %H:%M:%S',  
                        filename='log/log_key_word.log',  
                        filemode='w')  
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr  
    console = logging.StreamHandler()  
    console.setLevel(logging.INFO)  
    # 设置日志打印格式  
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')  
    console.setFormatter(formatter)  
    # 将定义好的console日志handler添加到root logger  
    logging.getLogger('').addHandler(console)  
    
    if len(sys.argv) == 1:
        usage() 
        sys.exit()
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        usage() 
        sys.exit()
    else:
        identity = sys.argv.pop()
        identity = identity.lower()
        if not (identity == 'master' or identity == "slave"):
            logging.error("error input parameter!!!")
            usage()
            sys.exit()

    logging.info("I'm "+identity)
        
    threads = []
    #创建线程，每个主机一个线程
    t = threading.Thread(target=recvMsg,args=(identity,))
    t.setDaemon(True)
    threads.append(t)
    
    t = threading.Thread(target=sendMsg,args=(identity,))
    t.setDaemon(True)
    threads.append(t)
    
    #启动线程
    for t in threads:
        t.start()
    #等待线程结束,等待时间根据实际修改，单位秒
    for t in threads:
        t.join()
        
if __name__ == '__main__':
    main()
    
    