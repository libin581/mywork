#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import cx_Oracle
import logging

def db_conn():
    #连接数据库
    ora_ip='10.10.10.120'
    ora_port='1521'
    instance_name='ora10'
    ora_dsn=cx_Oracle.makedsn(ora_ip,ora_port,instance_name)
    #流程配置存放在id用户，以id用户登录数据库
    logging.info( ora_dsn)
    #conn = cx_Oracle.connect('id','id',ora_dsn)
    conn = cx_Oracle.connect('id/id@10.1.245.131/ora10')
    
    return conn

def usage():
    logging.info( '''
    -------------------------------------------------------------------------
    usage:
    batch_rename_process.py            : help info
    batch_rename_process.py -h         : help info
    batch_rename_process.py --help     : help info
    
    select all processes with name or name prefix:
        batch_rename_process.py -s  process_name #process_name is process completed name or process name prefix 
    
    replace processes' name or configuration items with new name:
        batch_rename_process.py -u  old_process_name  new_process_name # used for single process or some processes with same prefix  
                                                    
        batch_rename_process.py -uf file_name    # used for many processes
                                                 # file contains old process names and new process names with space seprated    
                                                 # old process names as the first column, new process names as the second column  
                                                 # such as :
                                                 # rat_mms rat_mms_1234
                                                 # rat_sms rat_sms_333
                                                  
        batch_rename_process.py -ut temp_table   # used for many processes
                                                 # temp table contains old process names and new process names
                                                 # old process names as the first column, new process names as the second column
          
    eg:
       batch_rename_process.py -s rat_mms%
       batch_rename_process.py -s rat_mms
       batch_rename_process.py -u rat_mms% rat_mms_1234
       batch_rename_process.py -u rat_mms  rat_mms_1234
       batch_rename_process.py -uf file
       batch_rename_process.py -ut temp_table
  
    --------------------------------------------------------------------------
    '''
    )
    
def updateSql(old_process_name_prefix, new_process_name_prefix, selIn, cursor):
    old_process_name_prefix_no_percent = old_process_name_prefix
    if old_process_name_prefix[-1] == "%":
        old_process_name_prefix_no_percent = old_process_name_prefix[0:-1]
    
    update_sql_1 = '''
    update id.pdc_flow_srv_pipe_line d SET d.pipe_line_value=
    REPLACE(d.pipe_line_value,'%s','%s') 
    where  d.srv_id IN (SELECT b.srv_id FROM id.RDC_FLOW_SRV b WHERE b.flow_id IN 
    (SELECT c.flow_id FROM id.rdc_flow c WHERE c.flow_name like '%s'))'''%(old_process_name_prefix_no_percent,
    new_process_name_prefix,old_process_name_prefix)

    ##a.srv_id should modify to a.level_obj_id for hunan
    update_sql_2 = '''
    update id.pdc_flow_srv_param_oth a set a.cfg_value=
    REPLACE(a.cfg_value,'%s','%s') 
    where a.level_obj_id in (SELECT b.srv_id FROM id.RDC_FLOW_SRV b where b.flow_id in 
    (SELECT c.flow_id FROM id.rdc_flow c where c.flow_name like '%s'))'''%(old_process_name_prefix_no_percent,
    new_process_name_prefix,old_process_name_prefix)

    update_sql_3 = '''
    update id.RDC_FLOW_SRV b set b.srv_name=
    REPLACE(b.srv_name,'%s','%s') 
    where b.flow_id IN 
    (SELECT c.flow_id FROM id.rdc_flow c WHERE c.flow_name like '%s')'''%(old_process_name_prefix_no_percent,
    new_process_name_prefix,old_process_name_prefix)
    
    update_sql_4 = '''
    update id.rdc_flow c set c.flow_name=
    REPLACE(c.flow_name,'%s','%s') 
    WHERE c.flow_name like '%s' '''%(old_process_name_prefix_no_percent,
    new_process_name_prefix,old_process_name_prefix)

    update_sql_5 = '''
    update id.pdc_flow_srv e set e.srv_name=
    REPLACE(e.srv_name,'%s','%s') 
    where e.flow_id in 
    (SELECT t.flow_id FROM id.pdc_flow t where t.flow_code like '%s')'''%(old_process_name_prefix_no_percent,
    new_process_name_prefix,old_process_name_prefix)
    
    update_sql_6 = '''
    update ID.PDC_FLOW t set 
    t.flow_code =REPLACE(t.flow_name,'%s','%s'),
    t.queue_code =REPLACE(t.queue_code,'%s','%s'),
    t.flow_name =REPLACE(t.flow_name,'%s','%s') 
    WHERE t.flow_name like '%s' '''%(old_process_name_prefix_no_percent,new_process_name_prefix,
    old_process_name_prefix_no_percent,new_process_name_prefix,
    old_process_name_prefix_no_percent,new_process_name_prefix,
    old_process_name_prefix)
    
    update_sql_7 = '''
    commit'''
    
    logging.info( update_sql_1);cursor.execute(update_sql_1)
    logging.info( update_sql_2);cursor.execute(update_sql_2)
    if selIn == "1":
        logging.info( update_sql_3);cursor.execute(update_sql_3)
        logging.info( update_sql_4);cursor.execute(update_sql_4)
        logging.info( update_sql_5);cursor.execute(update_sql_5)
        logging.info( update_sql_6);cursor.execute(update_sql_6)
    logging.info( update_sql_7);cursor.execute(update_sql_7)
    
def querySql(process_name, cursor):
    #a. srv_id should modify to a.level_obj_id for hunan
    query_sql = '''
    select c.flow_id,c.flow_name,b.srv_name,a.cfg_name,a.cfg_value,d.srv_id,d.pipe_line_value 
    FROM id.pdc_flow_srv_param_oth a,id.RDC_FLOW_SRV b,id.rdc_flow c,id.pdc_flow_srv_pipe_line d 
    where  c.flow_name like '%s' 
    AND a.level_obj_id= b.srv_id and b.flow_id = c.flow_id and b.srv_id=d.srv_id'''%(process_name)
    
    logging.info(query_sql)
    
    cursor.execute(query_sql)
    result = cursor.fetchall() 
    count = cursor.rowcount
    
    logging.info( "=====================")
    logging.info( "Total:%d"%(count))
    logging.info( "=====================")
    for row in result:
            row_list = list(row)
            del row_list[4]
            logging.info( row_list )

    return count 
    
def main():
    '''主程序入口'''
    
    # 配置日志信息  
    logging.basicConfig(level=logging.DEBUG,  
                        format='%(message)s',  
                        datefmt='%m-%d %H:%M',  
                        filename='rename_process.log',  
                        filemode='w')  
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr  
    console = logging.StreamHandler()  
    console.setLevel(logging.INFO)  
    # 设置日志打印格式  
    #formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')  
    #console.setFormatter(formatter)  
    # 将定义好的console日志handler添加到root logger  
    logging.getLogger('').addHandler(console)  
          
    
    #参数分析
    if len(sys.argv) == 3 and sys.argv[1] == "-s":
        process_name=sys.argv.pop()
        #print "process name: %s"%(process_name)
        logging.info("process name: %s"%(process_name)) 

    elif len(sys.argv) == 4 and sys.argv[1] == "-u":
        new_process_name = sys.argv.pop()
        old_process_name = sys.argv.pop()
        #print "replace %s with %s"%(new_process_name, old_process_name)
        logging.info("replace %s with %s"%(new_process_name, old_process_name))
    elif len(sys.argv) == 3 and sys.argv[1] == "-uf":
        file_name = sys.argv.pop()        
    elif len(sys.argv) == 3 and sys.argv[1] == "-ut":
        table_name = sys.argv.pop()        
    elif len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        usage()
        sys.exit()
    else:
        #print ' not support option: %s or not enough parameters!!!'%(sys.argv[1])
        logging.error(' not support option: %s or not enough parameters!!!'%(sys.argv[1]))
        usage()
        sys.exit()
    
    #连接数据库
    #print "Connecting to database..."
    logging.info("Connecting to database...")
    conn = db_conn()
    cursor = conn.cursor()
    #print "Database connected!"
    logging.info("Database connected!")
    
    option = sys.argv[1]
    if option == "-s":
        querySql(process_name, cursor)
            
    elif option == "-u":
                
        #print ''' 
        #  please select number for which to do:
        #  1. change process's name  
        #  2. change configuration items
        #      '''
        logging.info(''' 
          please select number for which to do:
          1. change process's name  
          2. change configuration items
              ''')
        
        selIn=raw_input()
        
        count = querySql(old_process_name, cursor)
        
        if count > 0 :
            #print "\n---replace %s with %s---"%(old_process_name, new_process_name)  
            logging.info("\n---replace %s with %s---"%(old_process_name, new_process_name))
            updateSql(old_process_name, new_process_name, selIn, cursor)        
    
    elif option == "-uf":
        #print "read process names from file: %s"%(file_name)
        logging.info("read process names from file: %s"%(file_name))
        if not os.path.isfile(file_name):
            #print "%s is not file or dir!!!"%(file_name)
            logging.error("%s is not file or dir!!!"%(file_name))
            sys.exit()
    
        line_list=[]
        READ_FILE   = open(file_name, "r")
        line = READ_FILE.readline()
        while(line):
            line_list.append(line)
            line = READ_FILE.readline()
        READ_FILE.close()

        #print ''' 
        #  please select number for which to do:
        #  1. change process's name  
        #  2. change configuration items
        #     '''
        logging.info(''' 
          please select number for which to do:
          1. change process's name  
          2. change configuration items
              ''')      
              
        selIn=raw_input()
        
        for line in line_list:
            line = line.strip()
            if line:
                old_new_process_name = line.split()
                count  = querySql(old_new_process_name[0], cursor)

                if count > 0:
                    #print "\n---replace %s with %s ---"%(old_new_process_name[0], old_new_process_name[1])  
                    logging.info("\n---replace %s with %s ---"%(old_new_process_name[0], old_new_process_name[1]))
                    updateSql(old_new_process_name[0], old_new_process_name[1], selIn, cursor)        
                
    elif option == "-ut":
        #print "read process names from table: %s"%(table_name)
        logging.info("read process names from table: %s"%(table_name))
        
        query_sql = "select * from %s "%(table_name)
        
        logging.info( query_sql )
        
        cursor.execute(query_sql)
        result = cursor.fetchall() 
        count = cursor.rowcount
        logging.info( "=====================")
        logging.info( "Total:%d"%(count))
        logging.info( "=====================")
        if count == 0:
            sys.exit()
            
        for row in result:
                logging.info( row )

        logging.info( ''' 
          please select number for which to do:
          1. change process's name  
          2. change configuration items
              ''')
        selIn=raw_input()
        
        for row in result:
            old_process_name = row[0].strip()
            new_process_name = row[1].strip()
            
            count = querySql(old_process_name, cursor)

            if count > 0:
                logging.info( "\n---replace %s with %s ---"%(old_process_name, new_process_name))
                updateSql(old_process_name, new_process_name, selIn, cursor)        
                
    cursor.close
    conn.close()
    
if __name__ == "__main__":        
	main()
    
    