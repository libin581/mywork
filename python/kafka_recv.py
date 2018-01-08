#! /usr/bin/python
# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json


class Kafka_consumer():
    '''
    ʹ��Kafka��python������ģ��
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


def main():
    '''
    '''

    ##��������ģ��
    #����ģ��ķ��ظ�ʽΪConsumerRecord(topic=u'ranktest', partition=0, offset=202, timestamp=None, 
    #\timestamp_type=None, key=None, value='"{abetst}:{null}---0"', checksum=-1868164195, 
    #\serialized_key_size=-1, serialized_value_size=21)
    consumer = Kafka_consumer('127.0.0.1', 9092, "logKeyVal", 'python-logKeyVal')
    message = consumer.consume_data()
    for i in message:
        print i.value


if __name__ == '__main__':
    main()
