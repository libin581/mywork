#! /bin/sh
echo "++++++++++UT start++++++++++"
dateStr=$(date +%Y%m%d_%H%M%S)
fileName="log_$dateStr.txt"
echo "save into file: $fileName"
./u32ToFloat.py | tee -a "$fileName"
./floatToU32.py | tee -a "$fileName"
./complexFloatToFixed.py | tee -a "$fileName"
./complexFixedToFloat.py | tee -a "$fileName"
echo
echo "**********UT result************"
grep "FAIL" $fileName
echo
echo "++++++++++UT end++++++++++"