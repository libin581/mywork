#! /bin/bash
#sudo mount -t vboxsf regression_testing /home/ut/regression_testing/

winFile=$1
linuxFile=$2

sudo mount -t vboxsf -o iocharset=cp936 $winFile /home/ut/$linuxFile/




