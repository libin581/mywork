def main():
    '''
    �����������־�ؼ���ϵͳ�ű�
    1. ���master�����ϵĽű�״��
    2. �ѽű��͵���slave����
    3. ����slave�����Ͻű�����״��
        ����������У���ֹͣ���̣��滻�ű�����������
        ���û���������У��滻�ű�����������
    4. �ռ��ű������ɹ�����־
    '''
    ##��������ģ��
    producer = Kafka_producer("127.0.0.1", 9092, "logKeyVal")
    for id in range(10):
        params = '{abetst}:{null}---'+str(id)
        print "send:"+params
        producer.sendjsondata(params)

if __name__ == '__main__':
    main()