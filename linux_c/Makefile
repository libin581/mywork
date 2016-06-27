#! /bin/bash

CFLAGS=  #-O2
lib=/usr/local/lib

binfile=alarm callProcess client1 server1 ctrlc1 ctrlc2 \
epollEcho fork1 fork2 fork-wait hello program\
lock1 lock2 msg1 msg2 pexec \
pipe1 pipe2 pipe3 pipe4 pollEcho popen1 popen2 \
sem1  shm1 shm2 simpleEcho simple_write \
system1 thread1 thread2 thread3 thread4 \
daemonTest lock3 printTest1 printTest2 time2asc\
upper useupper simple_read copy_system\
copy_block copy_stdio \

objects=alarm.o callProcess.o client1.o server1.o ctrlc1.o \
ctrlc2.o daemon.o daemonTest.o epollEcho.o fork1.o fork2.o fred.o \
bill.o program.o hello.o

alarm:
	gcc $(CFLAGS) -o alarm ./alarm.c

callProcess:
	gcc $(CFLAGS) -o callProcess ./callProcess.c

client1:
	gcc $(CFLAGS) -o client1 ./client1.c

server1:
	gcc $(CFLAGS) -o server1 ./server1.c

ctrlc1:
	gcc $(CFLAGS) -o ctrlc1 ./ctrlc1.c

ctrlc2:
	gcc $(CFLAGS) -o ctrlc2 ./ctrlc2.c
	
daemonTest:
	gcc $(CFLAGS) -c ./daemon.c
	gcc $(CFLAGS) -c ./daemonTest.c
	gcc $(CFLAGS) -o daemonTest daemon.o daemonTest.o
    
epollEcho:
	g++ $(CFLAGS) -o epollEcho ./epollEcho.cpp

fork1:
	gcc $(CFLAGS) -o fork1 ./fork1.c

fork2:
	gcc $(CFLAGS) -o fork2 ./fork2.c

fork-wait:
	gcc $(CFLAGS) -o fork-wait ./fork-wait.c

hello:
	gcc $(CFLAGS) -o hello ./hello.c

helloworld:
	gcc $(CFLAGS) -o helloworld ./helloworld.c

lock1:
	gcc $(CFLAGS) -o lock1 ./lock1.c

lock2:
	gcc $(CFLAGS) -o lock2 ./lock2.c

lock3:
	gcc $(CFLAGS) -o lock3 ./lock3.c

msg1:
	gcc $(CFLAGS) -o msg1 ./msg1.c

msg2:
	gcc $(CFLAGS) -o msg2 ./msg2.c

pipe1:
	gcc $(CFLAGS) -o pipe1 ./pipe1.c

pipe2:
	gcc $(CFLAGS) -o pipe2 ./pipe2.c
      
pipe3:
	gcc $(CFLAGS) -o pipe3 ./pipe3.c

pipe4:
	gcc $(CFLAGS) -o pipe4 ./pipe4.c

pexec:
	gcc $(CFLAGS) -o pexec ./pexec.c

pollEcho:
	g++ $(CFLAGS) -o pollEcho ./pollEcho.cpp
      
popen1:
	gcc $(CFLAGS) -o popen1 ./popen1.c
      
popen2:
	gcc $(CFLAGS) -o popen2 ./popen2.c
      
program:
	gcc $(CFLAGS) -c ./bill.c
	gcc $(CFLAGS) -c ./fred.c
	gcc $(CFLAGS) -c ./program.c
	gcc $(CFLAGS) -o program program.o bill.o fred.o

printTest1:
	g++ $(CFLAGS) -o printTest1 ./printTest.cpp

printTest2:
	gcc $(CFLAGS) -o printTest2 ./printTest.c

sem1:
	gcc $(CFLAGS) -o sem1 ./sem1.c  

shm1:
	gcc $(CFLAGS) -o shm1 ./shm1.c  

shm2:
	gcc $(CFLAGS) -o shm2 ./shm2.c  
  
simpleEcho:
	g++ $(CFLAGS) -o simpleEcho ./simpleEcho.cpp    
    
simple_write:
	gcc $(CFLAGS) -o simple_write ./simple_write.c  

system1:
	gcc $(CFLAGS) -o system1 ./system1.c

thread1:
	gcc $(CFLAGS) -o thread1 ./thread1.c -lpthread

thread2:
	gcc $(CFLAGS) -o thread2 ./thread2.c -lpthread

thread3:
	gcc $(CFLAGS) -o thread3 ./thread3.c -lpthread

thread4:
	gcc $(CFLAGS) -o thread4 ./thread4.c -lpthread

time2asc:
	g++ $(CFLAGS) -o time2asc ./time2asc.cpp

upper:
	gcc $(CFLAGS) -o upper ./upper.c

useupper:
	gcc $(CFLAGS) -o useupper ./useupper.c

simple_read:
	gcc $(CFLAGS) -o simple_read ./simple_read.c

copy_system:
	gcc $(CFLAGS) -o copy_system ./copy_system.c

copy_block:
	gcc $(CFLAGS) -o copy_block ./copy_block.c

copy_stdio:
	gcc $(CFLAGS) -o copy_stdio ./copy_stdio.c

all:
	make $(binfile)

.PHONY: clean
clean:
	-rm -f $(binfile) $(objects)
