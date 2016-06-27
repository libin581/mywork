#!/bin/sh
echo "delete local file"
delfile()
{
   cd $1
   ls | while read filename
   do
      rm $1/$filename
   done
}
echo "uncompress file"
uncompressfile()
{
  cd $1
  ls |grep .Z|while read filename 
   do
      uncompress $1/$filename
   done
}
echo "get file"
ftpgetdata()
{
ftp -n<<!
open 10.180.76.6
user bill_new bill!791
binary
prompt off
cd  $1
mget *.Z
close
bye
!
}
echo "main fun"
cd /billapp/scripts/rating/get_xdr
cat get_xdr_decode_34.cfg | while read  dcd_name srcdir destdir
do
cd $destdir
echo "delete "$destdir
delfile $destdir
echo "------------------------------------------------>"
done
echo "------------------------------------------------>"
cd /billapp/scripts/rating/get_xdr
cat get_xdr_decode_34.cfg | while read  dcd_name srcdir destdir
do
cd $destdir
echo "---->ftp "$dcd_name
ftpgetdata $srcdir
echo "---->uncompress"
uncompressfile $destdir
echo "------------------------------------------------>"
echo

done

