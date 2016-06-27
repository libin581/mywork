import string, sys, os
def u32ToFloat(HexData):
    strHexDataTemp = HexData.replace('0x','')
    strHexData = strHexDataTemp.replace('0X','')
    decData = int(strHexData, 16)
    binData = bin(decData)
    bitNum  = len(binData[2:])
    zerostr = '0'*(32-bitNum)
    binData32bit = zerostr + binData[2:]
    s = int(binData32bit[0], 2) # 31th bit is sign bit
    e = int(binData32bit[1:9], 2) # % 30 ~ 23 bits are 'e'
    x = float(int(binData32bit[9:32], 2))/(2.0**23) #22 ~ 0 bits are 'x'
    floatData = (-1)**s * (1 + x) * 2**(e - 127)
    return floatData

if __name__ == '__main__':
    floatData = u32ToFloat('0x060715F8')
    print floatData

