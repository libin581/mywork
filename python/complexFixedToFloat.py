#! /usr/bin/env python
import string
def complexFixedToFloat(HexData, Qformat=15):
    ''' complexFixedToFloat -- convert an unsigned hex integer to a float complex data
        such as: complexFixedToFloat('0xCF682D7A')
    '''
    strHexDataTemp = HexData.replace('0x', '')
    strHexData = strHexDataTemp.replace('0X', '')
    realQformat = int(strHexData[0:4], 16)
    realRmQ     = realQformat*(2.0**(-1*Qformat))
    imagQformat = int(strHexData[4:8], 16)
    imagRmQ     = imagQformat*(2.0**(-1*Qformat))
    complexFloatData = complex(realRmQ, imagRmQ)
    return complexFloatData

if __name__ == '__main__':
    functionName = "complexFixedToFloat"
    print "------UT for %s---------" % (functionName)

    from complexFloatToFixed import complexFloatToFixed
    testData = '0xCF682D7A'
    complexFixedData = complexFloatToFixed(complexFixedToFloat(testData, 15), 15)
    print complexFixedData
    if testData == complexFixedData:
        print "--------------%s PASS--------------" % (functionName)
    else:
        print "--------------%s FAIL--------------" % (functionName)
