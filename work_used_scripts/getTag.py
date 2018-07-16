#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pdb

def usage():
    print '''
    getTag.py + 十六进制的tag值
    eg:
        getTag.py 5F8101 #129
      
    '''

def getbits(x, p, n):
    x,p,n=int(x,16),int(p),int(n)
    return ( int(x) >> (p+1-n))  & ~(~0 << n);

def main():
    '''
    把十六进制的tag，转成十进制tag
    '''

    if len(sys.argv) == 1:
        usage()
        sys.exit()
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
         usage()
         sys.exit()
    else:
         tagHex = sys.argv.pop()

    tagx = tagHex[0:2]
    ident = getbits(tagx,4,5)
    if (ident == 31):
        tag2x = tagHex[2:4]
        if not tag2x:
            return
        ident = getbits(tag2x, 6, 7)
        ii=4
        while getbits(tag2x, 7,1):
            ident <<= 7
            tag2x = tagHex[ii:ii+2]
            ii+=2
            if not tag2x:
                return
            ident += getbits(tag2x, 6, 7)
    print ident
    
if __name__ == '__main__':
    main()
