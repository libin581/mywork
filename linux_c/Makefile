#! /bin/bash

CFLAGS=  #-O2
#lib=/usr/local/lib
#BOOST_ROOT=/home/ut/share/boost_1_46_1
INCLUDE = .:${BOOST_ROOT} 
LIB = ${LD_LIBRARY_PATH}

binfile=alarm callProcess client1 server1 ctrlc1 ctrlc2 \
epollEcho fork1 fork2 fork-wait hello program\
lock1 lock2 msg1 msg2 pexec \
pipe1 pipe2 pipe3 pipe4 pollEcho popen1 popen2 \
sem1  shm1 shm2 simpleEcho simple_write \
system1 thread1 thread2 thread3 thread4 \
daemonTest lock3 printTest1 printTest2 time2asc\
upper useupper simple_read copy_system\
copy_block copy_stdio boost_lambda boost_regex

objects=alarm.o callProcess.o client1.o server1.o ctrlc1.o \
ctrlc2.o daemon.o daemonTest.o epollEcho.o fork1.o fork2.o fred.o \
bill.o program.o hello.o a.out


alarm:alarm.c
	gcc -I$(INCLUDE) $(CFLAGS) -o alarm  alarm.c

callProcess:callProcess.c
	gcc -I$(INCLUDE) $(CFLAGS) -o callProcess  callProcess.c

client1:client1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o client1  client1.c

server1:server1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o server1  server1.c

ctrlc1:ctrlc1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o ctrlc1  ctrlc1.c

ctrlc2:ctrlc2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o ctrlc2  ctrlc2.c

daemon.o:daemon.c
	gcc -I$(INCLUDE) $(CFLAGS) -o daemon.o -c daemon.c
daemonTest.o:daemonTest.c
	gcc -I$(INCLUDE) $(CFLAGS) -o daemonTest.o -c daemonTest.c
daemonTest:daemonTest.o daemon.o
	gcc -I$(INCLUDE) $(CFLAGS) -o daemonTest daemon.o daemonTest.o
    
epollEcho:epollEcho.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o epollEcho  epollEcho.cpp

fork1:fork1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o fork1  fork1.c

fork2:fork2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o fork2  fork2.c

fork-wait:fork-wait.c
	gcc -I$(INCLUDE) $(CFLAGS) -o fork-wait  fork-wait.c

hello:hello.c
	gcc -I$(INCLUDE) $(CFLAGS) -o hello  hello.c

helloworld:helloworld
	gcc -I$(INCLUDE) $(CFLAGS) -o helloworld  helloworld.c

lock1:lock1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o lock1  lock1.c

lock2:lock2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o lock2  lock2.c

lock3:lock3.c
	gcc -I$(INCLUDE) $(CFLAGS) -o lock3  lock3.c

msg1:msg1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o msg1  msg1.c

msg2:msg2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o msg2  msg2.c

pipe1:pipe1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o pipe1  pipe1.c

pipe2:pipe2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o pipe2  pipe2.c
      
pipe3:pipe3.c
	gcc -I$(INCLUDE) $(CFLAGS) -o pipe3  pipe3.c

pipe4:pipe4.c
	gcc -I$(INCLUDE) $(CFLAGS) -o pipe4  pipe4.c

pexec:pexec.c
	gcc -I$(INCLUDE) $(CFLAGS) -o pexec  pexec.c

pollEcho:pollEcho.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o pollEcho  pollEcho.cpp
      
popen1:popen1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o popen1  popen1.c
      
popen2:popen2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o popen2  popen2.c
 
bill.o:bill.c
	gcc -I$(INCLUDE) $(CFLAGS) -o bill.o  -c bill.c
fred.o:fred.c
	gcc -I$(INCLUDE) $(CFLAGS) -o fred.o  -c fred.c
program.o:program.c
	gcc -I$(INCLUDE) $(CFLAGS) -o program.o  -c program.c
program:bill.o fred.o program.o
	gcc -I$(INCLUDE) $(CFLAGS) -o program program.o bill.o fred.o

printTest1:printTest.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o printTest1  printTest.cpp

printTest2:printTest.c
	gcc -I$(INCLUDE) $(CFLAGS) -o printTest2 printTest.c

sem1:sem1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o sem1  sem1.c  

shm1:shm1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o shm1  shm1.c  

shm2:shm2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o shm2  shm2.c  
  
simpleEcho:simpleEcho.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o simpleEcho  simpleEcho.cpp    
    
simple_write:simple_write.c
	gcc -I$(INCLUDE) $(CFLAGS) -o simple_write  simple_write.c  

system1:system1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o system1  system1.c

thread1:thread1.c
	gcc -I$(INCLUDE) $(CFLAGS) -o thread1  thread1.c -lpthread

thread2:thread2.c
	gcc -I$(INCLUDE) $(CFLAGS) -o thread2  thread2.c -lpthread

thread3:thread3.c
	gcc -I$(INCLUDE) $(CFLAGS) -o thread3  thread3.c -lpthread

thread4:thread4.c
	gcc -I$(INCLUDE) $(CFLAGS) -o thread4  thread4.c -lpthread

time2asc:time2asc.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o time2asc  time2asc.cpp

upper:upper.c
	gcc -I$(INCLUDE) $(CFLAGS) -o upper  upper.c

useupper:useupper.c
	gcc -I$(INCLUDE) $(CFLAGS) -o useupper  useupper.c

simple_read:simple_read.c
	gcc -I$(INCLUDE) $(CFLAGS) -o simple_read  simple_read.c

copy_system:copy_system.c
	gcc -I$(INCLUDE) $(CFLAGS) -o copy_system  copy_system.c

copy_block:copy_block.c
	gcc -I$(INCLUDE) $(CFLAGS) -o copy_block  copy_block.c

copy_stdio:copy_stdio.c
	gcc -I$(INCLUDE) $(CFLAGS) -o copy_stdio  copy_stdio.c

boost_lambda:boost_lambda.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_lambda boost_lambda.cpp

boost_regex:boost_regex.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_regex boost_regex.cpp -L$(LIB) -lboost_regex

all:
	make $(binfile)

.PHONY: clean
clean:
	-rm -f $(binfile) $(objects) 
