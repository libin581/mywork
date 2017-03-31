#! /bin/bash

CFLAGS=  #-O2
#lib=/usr/local/lib
#BOOST_ROOT=/home/ut/share/boost_1_46_1
LIB = ${LD_LIBRARY_PATH}

binfile=test_1

test_1:test_1.cpp
	g++ -o test_1 -lglog test_1.cpp

all:
	make $(binfile)

.PHONY: clean
clean:
	-rm -f $(binfile)  
