#! /bin/bash

cd /usr/local/zookeeper-3.4.10/
bin/zkServer.sh start conf/zoo_sample.cfg
sleep 15
netstat -tunlp|grep 2181
bin/zkServer.sh status
jps

cd ../kafka_2.10-0.9.0.0/
bin/kafka-server-start.sh config/server0.properties 
sleep 30
netstat -tunlp|egrep "(2181|9092|9093|9094)"
jps

