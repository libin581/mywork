#! /usr/bin/env python
import sys, os
import string
import TComplexFixedToFloat
import matplotlib.pyplot as plt
import commonConfig

def TComplexFixedToFloat_file(srcFileName):
    ''' TComplexFixedToFloat_file -- convert unsigned hex data in a file to float data
        such as: TComplexFixedToFloat_file('rawhant0.dat')
    '''
    
    dstFileName = srcFileName.replace('dat','txt')

    srcFileHandle = open(srcFileName, 'r')
    complexFixedData = srcFileHandle.read()
    srcFileHandle.close()

    complexFixedDataSpec = complexFixedData
    # remove header
    if complexFixedDataSpec[0:4] == '1651':
        firstEnter = complexFixedDataSpec.find('\n')
        complexFixedDataRmHeader = complexFixedDataSpec.replace(complexFixedDataSpec[0:firstEnter+1], '')
    else:
        print 'no header line\n'
        complexFixedDataRmHeader = complexFixedDataSpec

    complexFixedDataList = complexFixedDataRmHeader.split('\n')

    #remove empty str
    complexFixedDataList.remove('')

    # remove 0x or 0X
    if (complexFixedDataList[0].find('0x') == 0):
        for n in range(complexFixedDataList.__len__()):
            complexFixedDataList[n] = complexFixedDataList[n].replace('0x','')
    elif complexFixedDataList[0].find('0X') == 0:
        for n in range(complexFixedDataList.__len__()):
            complexFixedDataList[n] = complexFixedDataList[n].replace('0X','')
    else:
        print "no '0x' or '0X' prefixed"

    complexFloatList = []
    dstFileHandle = open(dstFileName,'w')
    if len(complexFixedDataList[0]) == 8:
        for hexdata in complexFixedDataList:
            complexFloatData = TComplexFixedToFloat.TComplexFixedToFloat(hexdata, 15)
            complexFloatList.append(complexFloatData)
            dstFileHandle.write(str(complexFloatData)+'\n')
    else:
        print 'unknown data length\n'
        sys.exit()

    dstFileHandle.close()

# draw
    plt.scatter(complexFixedDataList)

if __name__ == '__main__':
    srcFileName = 'rawhant0.dat'
    TComplexFixedToFloat_file(srcFileName)



