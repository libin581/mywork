#! /usr/bin/env python
__author__ = 'b2li'

from math import *
import string
def complexFloatToFixed(complexFloatData, Qformat=15):
    '''complexFloatToFixed -- convert float complex data to a unsigned hex integer
        such as: complexFloatToFixed(1+j)  
    '''

    realFloat = complexFloatData.real
    imagFloat = complexFloatData.imag
    #-------------- processing real part---------------
    #-------------- matlab code --------------------
    #if (RealValue(ii) > 0)
    #    RealFixValue = dec2hex(floor(RealValue(ii) * 2^Qx_i));
    #else
    #    RealFixValue = dec2hex(floor(2^16 + 1 + RealValue(ii) * 2^Qx_i));
    #end
    #Diff = 4 - length(RealFixValue);
    #for jj = 1:Diff
    #    RealFixValue = ['0' RealFixValue];
    #end

    amplCoeff = pow(2, Qformat)
    if realFloat > 0:
        realFix  = int(floor(realFloat*amplCoeff))
    else:
        realFix  = int(floor(pow(2, 16) + 1 + realFloat*amplCoeff))

    realFixHex = hex(realFix)
    realWithoutHeader1 = realFixHex.replace('0x','')
    realWithoutHeader2 = realWithoutHeader1.replace('0X','')
    Diff       = 4 - realWithoutHeader2.__len__()
    realHex    = '0'*Diff + realWithoutHeader2

    #-------------- processing imag part---------------
    #if (ImagValue(ii) > 0)
    #    ImagFixValue = dec2hex(floor(ImagValue(ii) * 2^Qx_i));
    #else
    #    ImagFixValue = dec2hex(floor(2^16 + 1 + ImagValue(ii) * 2^Qx_i));
    #end
    #Diff = 4 - length(ImagFixValue);
    #for jj = 1:Diff
    #    ImagFixValue = ['0' ImagFixValue];
    #end

    if imagFloat > 0:
        imagFix  = int(floor(imagFloat*amplCoeff))
    else:
        imagFix  = int(floor(pow(2, 16) + 1 + imagFloat*amplCoeff))

    imagFixHex = hex(imagFix)
    imagWithoutHeader1 = imagFixHex.replace('0x','')
    imagWithoutHeader2 = imagWithoutHeader1.replace('0X','')
    Diff       = 4 - imagWithoutHeader2.__len__()
    imagHex    = '0'*Diff + imagWithoutHeader2 

    # pack the real and imag parts
    complexFixedData = '0x'+(realHex+imagHex).upper()

    return complexFixedData

if __name__ == '__main__':
    functionName = "complexFloatToFixed"
    print "------UT for %s---------" % (functionName)
    from complexFixedToFloat import *
    testNumber = '0xCF682D7A'
    print testNumber
    complexFixedData = complexFloatToFixed(complexFixedToFloat(testNumber, 15), 15)
    print complexFixedData
    if testNumber == complexFixedData:
        print "--------------%s PASS--------------" % (functionName)
    else:
        print "--------------%s FAIL--------------" % (functionName)
        
