#!/bin/bash
#delelte obj files.

cd $PWD

if [ -d "lteDo" ]; then
	cd lteDo
	find . -name '*Channelizer*.obj' -exec rm -rf {} \;
        find . -name '*Channelizer.obj' -exec rm -rf {} \; 
	find . -name 'Channelizer*.obj' -exec rm -rf {} \; 
	find . -name '*Snapshot**.obj' -exec rm -rf {} \; 
	find . -name '*rachDit*.obj' -exec rm -rf {} \; 
	find . -name 'CFftcDriver.obj' -exec rm -rf {} \; 
	cd ..
fi


#./make.sh UL8DSP MT
#if [ -f "BIN/UlPhyMtUl8DspNyBin.BIN" ]; then
#   cp BIN/UlPhyMtUl8DspNyBin.BIN .
#else
#   vim BIN/build.txt
#fi

./make.sh DL8DSP MT
if [ -f "BIN/UlPhyMtDlDspNyBin.BIN" ]; then
   cp BIN/UlPhyMtDlDspNyBin.BIN .
   cp BIN/Dl8DspNyCpu2.map .
else
   vim BIN/build.txt
fi

#./make.sh L1DLDSP MT
#if [ -f "BIN/UlPhyMtL1DlDspNyBin.BIN" ]; then
#    cp BIN/UlPhyMtL1DlDspNyBin.BIN  .
#else
#    vim BIN/build.txt
#fi

#./make.sh MT_ALL
