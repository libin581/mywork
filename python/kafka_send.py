#! /usr/bin/python
# -*- coding: utf-8 -*-
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time

CHECK_ENV_INTERVAL_TIME = 10

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

def main():
    '''
    '''
    ##测试生产模块
    producer = Kafka_producer("127.0.0.1", 9092, "logKeyVal")
    while True:
        for id in range(10):
            params = '{abetst}:{null}---'+str(id)
            print "send:"+params
            producer.sendjsondata(params)
        time.sleep(CHECK_ENV_INTERVAL_TIME)

if __name__ == '__main__':
    main()