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

uncompressfile()
{
  cd $1
  ls |grep .Z|while read filename 
   do
      uncompress $1/$filename
   done
}

dcd_name=gprs_tap3.dcd
srcdir="/data09/liumh/orc_xdr1/20150829/ggprs/ggsn_cngo"
echo "---->ftp "$dcd_name
ftpgetdata $srcdir
echo "---->uncompress"
destdir="./"
uncompressfile $destdir