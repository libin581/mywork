#! /bin/bash

CFLAGS =  #-O2
INCLUDE = .

tinystr.o:tinystr.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o tinystr.o -c tinystr.cpp
tinyxml.o:tinyxml.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o tinyxml.o -c tinyxml.cpp
tinyxmlerror.o:tinyxmlerror.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o tinyxmlerror.o -c tinyxmlerror.cpp
tinyxmlparser.o:tinyxmlparser.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o tinyxmlparser.o -c tinyxmlparser.cpp
tinyxmltest.o:tinyxmltest.cpp
	g++ -I$(INCLUDE) $(CFLAGS) -o tinyxmltest.o -c tinyxmltest.cpp
tinyxmltest:tinystr.o tinyxml.o tinyxmlerror.o tinyxmlparser.o tinyxmltest.o
	g++ -I$(INCLUDE) $(CFLAGS) -o tinyxmltest tinystr.o tinyxml.o tinyxmlerror.o tinyxmlparser.o tinyxmltest.o 
    
clean:
	-rm -f *.o tinyxmltest