#! /usr/bin/python
#coding:utf-8

from math import hypot
from random import random
#import eventlet
import time


def test(tries):
    #hypot，求点到原点的距离
    return sum(hypot(random(), random()) < 1 for _ in range(tries))
    
def calcPi(nbFutures, tries):
    ts = time.time()
    #tries是test的入参，这个函数"并行"执行nbFutures次
    result = map(test, [tries] * nbFutures) 
     
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print "time spend ", span
    return ret
 
print calcPi(3000,4000)