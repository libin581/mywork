
import binascii
import sys
import time
import struct
from optparse import OptionParser

MAX_BYTES_OF_DAT = 1024*550 # the max size of each vector uploading to FCM is 500kb

def convertDat2Bin(datName, binName,bigEndian):
    with open(datName, 'r') as antennaDataFileHandle:
        antennaDataFileHandle.readline()
        antennaDataText = antennaDataFileHandle.read()
        
    antennaDataTextLines = antennaDataText.splitlines()
            
    start = time.time()
    #antennaDataBytes = ''.join([binascii.unhexlify(antennaSampleTextLine[2:10]) for antennaSampleTextLine in antennaDataTextLines])
    if bigEndian:
        antennaDataBytes = ''.join([struct.pack('>I', int(antennaSampleTextLine, 16)) for antennaSampleTextLine in antennaDataTextLines])
    else:
        antennaDataBytes = ''.join([struct.pack('<I', int(antennaSampleTextLine, 16)) for antennaSampleTextLine in antennaDataTextLines])
            
    end =time.time()
    
    used = 1000 * (end - start)
    print used
    dataLength = len(antennaDataBytes)
    
    dataIndex = 0
    ind = 1
    while dataIndex < dataLength:
        antennaDataChunk = antennaDataBytes[dataIndex : dataIndex + MAX_BYTES_OF_DAT]
                
        binWriteHandle = open(binName + '_' + str(ind), 'wb')
        binWriteHandle.write(antennaDataChunk)
        binWriteHandle.close()
        
        dataIndex += MAX_BYTES_OF_DAT
        ind += 1

def bin2Dat(binName, datName, bigEndian):
    binFileHandle = open(binName, 'rb')
    datFileHandle = open(datName, 'w')
    
    binTxt = binFileHandle.read()
    i = 0
    while i < len(binTxt):
        if bigEndian:
            binByte = struct.unpack('>I',binTxt[i:i+4])
        else:                
            binByte = struct.unpack('<I',binTxt[i:i+4])
        datFileHandle.write("0x%08x\n" % binByte)
        i += 4
        
    datFileHandle.close()
    binFileHandle.close()              
         
def convertDat2SingleBin(datName, binName,bigEndian):
    with open(datName, 'rb') as datFileHandle:
        datFileHandle.readline()
        datTxt = datFileHandle.read()

    start            = time.time()
    datLines         = datTxt.splitlines()

    if bigEndian:
        antennaDataBytes = ''.join([struct.pack('>I', int(antennaSampleTextLine, 16)) for antennaSampleTextLine in datLines])
    else:
        antennaDataBytes = ''.join([binascii.unhexlify(antennaSampleTextLine[2:10]) for antennaSampleTextLine in datLines])

    binHandler       = open(binName+'.bin', 'wb')
    binHandler.write(antennaDataBytes)
    binHandler.close()
    end              = time.time()
    used             = 1000 * (end - start)
    print used

if __name__=="__main__":
    
    parser = OptionParser()
    
    parser.add_option("-m", "--mode", action="store",
                      dest="mode", help="support 2 MODE:dat2bin,bin2dat")
    parser.add_option("-b", "--bigEndian", action="store_true", default=False, 
                      dest="bigEndian", help="set big endian for output, default: small endian")
    parser.add_option("-s", "--source", action="store",
                      dest="source", help="source file to be converted")
    parser.add_option("-d", "--dest", action="store",
                      dest="dest", help="destination file name")
    
    (options,args) = parser.parse_args()
    mode = options.mode
    source = options.source
    dest = options.dest
    bigEndian = options.bigEndian
    
    if mode=='dat2bin':
        convertDat2Bin(str(source),str(dest),bigEndian)
    elif mode=='bin2dat':
        bin2Dat(str(source),str(dest),bigEndian)
    elif mode=='dat2singlebin':
        convertDat2SingleBin(str(source),str(dest),bigEndian)
    else:
        print "wrong mode! please see " + __file__ + " -help"
        