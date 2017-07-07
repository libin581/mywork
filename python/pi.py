#! /usr/bin/python
#coding:utf-8

from math import hypot
from random import random
#import eventlet
import time


def test(tries):
    #hypot����㵽ԭ��ľ���
    return sum(hypot(random(), random()) < 1 for _ in range(tries))
    
def calcPi(nbFutures, tries):
    ts = time.time()
    #tries��test����Σ��������"����"ִ��nbFutures��
    result = map(test, [tries] * nbFutures) 
     
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print "time spend ", span
    return ret
 
print calcPi(3000,4000)