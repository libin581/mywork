#! /usr/bin/python
__author__ = 'b2li'

import string
from math import *  
def floatToU32(floatData):
    '''floatToU32 -- convert float data to a unsigned hex integer
        such as: floatToU32(0.54)  
    '''

    if floatData > 0:
        sign = 1
    else:
        sign = -1

    pow_2_23 = pow(2, 23)

    absFloatData = abs(floatData)
    logFloatData = log(absFloatData)/log(2)
    if logFloatData>0:
        exp = floor(logFloatData)
    else:
        exp = ceil(logFloatData)

    man = (absFloatData/pow(2, exp)-1)*pow_2_23

    exp127 = exp+127

    if sign>0:
        hexData = hex(int(man+exp127*pow_2_23))
    else:
        hexData = hex(int(2147483648+man+exp127*pow_2_23))

    hexDataWithoutHeader1 = hexData.replace('0x', '')
    hexDataWithoutHeader2 = hexDataWithoutHeader1.replace('L', '')

    diff    = 8 - hexDataWithoutHeader2.__len__()
    u32Data = '0x' + '0'*diff + hexDataWithoutHeader2.upper()

    return u32Data

if __name__ == '__main__':
    functionName = "floatToU32"
    print "------UT for %s---------" % (functionName)

    from u32ToFloat import *
    testData = '0xC237F5C3'
    print testData
    u32Data = floatToU32(u32ToFloat(testData))
    print u32Data
    if testData == u32Data:
        print "--------------%s PASS--------------" % (functionName)
    else:
        print "--------------%s FAIL--------------" % (functionName)
