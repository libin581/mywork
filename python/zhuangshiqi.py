#! /usr/bin/python

import time
import pdb

#pdb.set_trace()

def foo():
    print 'in foo()'

def timeit(func):
    def wrapper():
       start = time.clock()
       func()
       end =time.clock()
       print 'used:', end - start
    
    return wrapper

foo = timeit(foo)

foo()


