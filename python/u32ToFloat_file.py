import sys, os
import string
#import matpltlib
import fileinput
import time

import commonConfig
import u32ToFloat

def u32ToFloat_file_1():

    timer = []
    timer.append(time.time())

    srcFileName = 'mme.dat'
    dstFileName = srcFileName.replace('dat','txt')
    dstFileHandle = open(dstFileName,'w')

    for line in fileinput.input(srcFileName):
        hexData = line.replace('\n','')
        if hexData[0:4] == '1651':
            pass
        elif (len(hexData) != 8) and (len(hexData) != 10):
            pass
        else:
            hexDataTemp = hexData.replace('0x','')
            hexDataRmHeader = hexDataTemp.replace('0X','')
            floatData = u32ToFloat.u32ToFloat(hexDataRmHeader)
            dstFileHandle.write(str(floatData)+'\n')

    dstFileHandle.close()

    timer.append(time.time())
    print 'consume time %f' % (timer[1]-timer[0])



def u32ToFloat_file_2():
    timer = []
    timer.append(time.time())

    srcFileName = 'mme.dat'
    dstFileName = srcFileName.replace('dat','txt')

    srcFileHandle = open(srcFileName, 'r')
    u32Data = srcFileHandle.read()
    srcFileHandle.close()

    u32DataSpec = u32Data
    # remove header
    if u32DataSpec[0:4] == '1651':
        firstEnter = u32DataSpec.find('\n')
        u32DataRmHeader = u32DataSpec.replace(u32DataSpec[0:firstEnter+1], '')
    else:
        print 'no header line\n'
        u32DataRmHeader = u32DataSpec

    u32DataList = u32DataRmHeader.split('\n')

    #remove empty str
    u32DataList.remove('')

    # remove 0x or 0X
    if (u32DataList[0].find('0x') == 0):
        for n in range(u32DataList.__len__()):
            u32DataList[n] = u32DataList[n].replace('0x','')
    elif u32DataList[0].find('0X') == 0:
        for n in range(u32DataList.__len__()):
            u32DataList[n] = u32DataList[n].replace('0X','')
    else:
        print "no '0x' or '0X' prefixed"

    floatDataList = []
    dstFileHandle = open(dstFileName,'w')
    if len(u32DataList[0]) == 8:
        for hexData in u32DataList:
            floatData = u32ToFloat.u32ToFloat(hexData)
            floatDataList.append(floatData)
            dstFileHandle.write(str(floatData)+'\n')
    else:
        print 'unknown data length\n'
        sys.exit()

    dstFileHandle.close()

    timer.append(time.time())

    print 'consume time %fs' % (timer[1]-timer[0])


if __name__ == '__main__':
   u32ToFloat_file_1()
   u32ToFloat_file_2()