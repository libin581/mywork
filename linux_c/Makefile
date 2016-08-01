#! /bin/bash

CFLAGS=  #-O2
#lib=/usr/local/lib
#BOOST_ROOT=/home/ut/share/boost_1_46_1
INCLUDE = .:${BOOST_ROOT} 
LIB = ${LD_LIBRARY_PATH}

binfile=alarm callProcess client1 server1 ctrlc1 ctrlc2 \
epollEcho fork1 fork2 hello program\
lock1 lock2 msg1 msg2 pexec \
pipe1 pipe2 pipe3 pipe4 pollEcho popen1 popen2 \
sem1  shm1 shm2 simpleEcho simple_write \
system1 thread1 thread2 thread3 thread4 \
daemonTest lock3 printTest1 printTest2 time2asc\
upper useupper simple_read copy_system\
time2ll time2loc lock4 lock5\
copy_block copy_stdio boost_lambda boost_regex\
boost_format boost_minmax string_test\
map_test algorithm_test sem1 sem1_compare\
sigchld print-env print-pid set_test\
template_test thread_pool_test\
boost_thread_simple boost_thread_mutex\
boost_thread_mutex_condition boost_thread_specific_ptr

objects=alarm.o callProcess.o client1.o server1.o ctrlc1.o \
ctrlc2.o daemon.o daemonTest.o epollEcho.o fork1.o fork2.o fred.o \
bill.o program.o hello.o a.out thread_pool_test.o thread_pool.o


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

lock4:lock4.c
	gcc -I$(INCLUDE) $(CFLAGS) -o lock4  lock4.c

lock5:lock5.c
	gcc -I$(INCLUDE) $(CFLAGS) -o lock5  lock5.c

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

sem1:sem1.c semun.h
	gcc -I$(INCLUDE) $(CFLAGS) -o sem1 sem1.c

sem1_compare:sem1_compare.c
	gcc -I$(INCLUDE) $(CFLAGS) -o sem1_compare  sem1_compare.c  
  
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

string_test:string_test.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o string_test string_test.cpp

time2ll:time2ll.c
	gcc -I$(INCLUDE) $(CFLAGS) -o time2ll time2ll.c

time2loc:time2loc.c
	gcc -I$(INCLUDE) $(CFLAGS) -o time2loc time2loc.c

map_test:map_test.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o map_test map_test.cpp

algorithm_test:algorithm_test.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o algorithm_test algorithm_test.cpp

sigchld: sigchld.c
	gcc -I$(INCLUDE) $(CFLAGS) -o sigchld sigchld.c

set_test: set_test.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o set_test set_test.cpp

print-env: print-env.c
	gcc -I$(INCLUDE) $(CFLAGS) -o print-env print-env.c

print-pid: print-pid.c
	gcc -I$(INCLUDE) $(CFLAGS) -o print-pid print-pid.c

template_test: template_test.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o template_test template_test.cpp

boost_lambda:boost_lambda.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_lambda boost_lambda.cpp

boost_regex:boost_regex.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_regex boost_regex.cpp -L$(LIB) -lboost_regex

boost_format:boost_format.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_format boost_format.cpp 

boost_minmax:boost_minmax.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_minmax boost_minmax.cpp 

boost_thread_simple:boost_thread_simple.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_thread_simple boost_thread_simple.cpp -L$(LIB) -lboost_system -lboost_thread

boost_thread_mutex:boost_thread_mutex.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_thread_mutex boost_thread_mutex.cpp -L$(LIB) -lboost_system -lboost_thread

boost_thread_mutex_condition:boost_thread_mutex_condition.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_thread_mutex_condition boost_thread_mutex_condition.cpp -L$(LIB) -lboost_system -lboost_thread

boost_thread_specific_ptr:boost_thread_specific_ptr.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o boost_thread_specific_ptr boost_thread_specific_ptr.cpp -L$(LIB) -lboost_system -lboost_thread

thread_pool.o:thread_pool.cpp thread_pool.h
	g++ -I$(INCLUDE) $(CFLAGS) -o thread_pool.o -c thread_pool.cpp 
thread_pool_test.o:thread_pool_test.cpp thread_pool.h
	g++ -I$(INCLUDE) $(CFLAGS) -o thread_pool_test.o -c thread_pool_test.cpp 
thread_pool_test:thread_pool_test.o thread_pool.o
	g++ -I$(INCLUDE) $(CFLAGS) -o thread_pool_test thread_pool_test.o thread_pool.o -lpthread

all:
	make $(binfile)

.PHONY: clean
clean:
	-rm -f $(binfile) $(objects) 
