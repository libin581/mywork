def main():
    '''
    部署和启动日志关键字系统脚本
    1. 检测master主机上的脚本状况
    2. 把脚本送到各slave主机
    3. 检测各slave主机上脚本运行状况
        如果正在运行，则停止进程，替换脚本，启动进程
        如果没有正在运行，替换脚本，启动进程
    4. 收集脚本启动成功的日志
    '''
    ##测试生产模块
    producer = Kafka_producer("127.0.0.1", 9092, "logKeyVal")
    for id in range(10):
        params = '{abetst}:{null}---'+str(id)
        print "send:"+params
        producer.sendjsondata(params)

if __name__ == '__main__':
    main()