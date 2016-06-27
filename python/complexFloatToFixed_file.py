#! /usr/bin/env python
import sys, os
import string
import TComplexFixedToFloat
import matplotlib.pyplot as plt
import commonConfig

def TComplexFloatToFixed_file(srcFileName):
    ''' TComplexFixedToFloat_file -- convert unsigned hex data in a file to float data
        such as: TComplexFixedToFloat_file('rawhant0.dat')
    '''
    
    dstFileName = srcFileName.replace('dat','txt')

    srcFileHandle = open(srcFileName, 'r')
    complexFloatData = srcFileHandle.read()
    srcFileHandle.close()

    complexFloatDataSpec = complexFloatData
    # remove header
    if complexFloatDataSpec[0:4] == '1651':
        firstEnter = complexFloatDataSpec.find('\n')
        complexFloatDataRmHeader = complexFloatDataSpec.replace(complexFloatDataSpec[0:firstEnter+1], '')
    else:
        print 'no header line\n'
        complexFloatDataRmHeader = complexFloatDataSpec

    complexFloatDataList = complexFloatDataRmHeader.split('\n')

    #remove empty str
    complexFloatDataList.remove('')

    # remove 0x or 0X
    if (complexFloatDataList[0].find('0x') == 0):
        for n in range(complexFloatDataList.__len__()):
            complexFloatDataList[n] = complexFloatDataList[n].replace('0x','')
    elif complexFloatDataList[0].find('0X') == 0:
        for n in range(complexFloatDataList.__len__()):
            complexFloatDataList[n] = complexFloatDataList[n].replace('0X','')
    else:
        print "no '0x' or '0X' prefixed"

    complexFloatList = []
    dstFileHandle = open(dstFileName,'w')
    if len(complexFloatDataList[0]) == 8:
        for hexdata in complexFloatDataList:
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



