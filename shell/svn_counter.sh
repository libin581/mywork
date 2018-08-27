#! /bin/bash
# 计算有效变更代码量的脚本
# 包括注释，但不包括新增的空行
version() {
    OS=`uname -o`
    echo "svn_counter ($OS) 0.0.1"
}
 
 
usage() {
    echo "usage: svn_counter [-t SVN_REPOSITORY_URL] [-s START_REVISION]"
    echo "                      [-e END_REVISION] [-u USER_NAME]"
    echo "                      [-p PASSWD]"
    echo "       svn_counter [-v|-h]"
    echo 
    echo "        -t,                 目标SVN库地址"
    echo "        -s,                 起始修订号"
    echo "        -e,                 结束修订号"
    echo "        -a,                 提交作者"
    echo "        -u,                 svn帐号"
    echo "        -p,                 svn密码"
    echo "        -h,                 帮助"
    echo "        -v,                 版本信息"
}
 
 
if [ $# -lt 1 ]; then
    usage
    exit 1 
fi
 
 
while getopts "t:s:e:a:u:p:vh" opt; do
    case $opt in
        t) target=$OPTARG;;
        s) start_revision=$OPTARG;;
        e) end_revision=$OPTARG;;
        a) author=$OPTARG;;
        u) user=$OPTARG;;
        p) passwd=$OPTARG;;
        v) version; exit 1;;
        h) usage; exit 1;;
    esac
done
 
 
if [ -z $target ]; then
    echo "请输入目标SVN库地址!"
    exit 1
fi
 
 
if [ -z $start_revision ]; then
    echo "请输入起始修订号!"
    exit 1
fi
 
 
 
 
#SVN_CMD='/home/work/local/svn/bin/svn'
SVN_CMD='svn'
 
 
TEMPFILE=temp_diff.log
USERNAME=${user}
PASSWD=${passwd}
TOTAL=0
 
 
if [ -z $author ]; then
    if [ -z $end_revision ]; then
        ${SVN_CMD} diff -r$start_revision $target --username $USERNAME --password $PASSWD > $TEMPFILE
    else
        ${SVN_CMD} diff -r$start_revision:$end_revision $target --username $USERNAME --password $PASSWD > $TEMPFILE
    fi
 
 
    #去掉含空格的空行
    TOTAL=`grep "^+" $TEMPFILE | grep -v "^+++" | sed 's/^.//'| sed s/[[:space:]]//g |sed '/^$/d'|wc -l`
    #没有去掉有的空行
    #TOTAL=`grep "^+" $TEMPFILE|grep -v "^+++"|sed 's/^.//'|sed '/^$/d'|wc -l`
    
    rm -fr $TEMPFILE
    echo "$TOTAL"
else
    if [ -z $end_revision ]; then   
        revs=`${SVN_CMD} log -q $target  -r $start_revision:HEAD --username $USERNAME --password $PASSWD |awk '{print \$1,\$3}'| grep  ${author}| awk '{print \$1}'`
    else 
        revs=`${SVN_CMD} log -q $target  -r $start_revision:$end_revision --username $USERNAME --password $PASSWD |awk '{print \$1,\$3}'| grep  ${author}| awk '{print \$1}'`
    fi 
    for rev in ${revs};do
        rev=${rev:1}
        last_rev=$((rev-1))
 
 
        ${SVN_CMD} diff -r${last_rev}:${rev} $target --username $USERNAME --password $PASSWD  > $TEMPFILE
        count=`grep "^+" $TEMPFILE | grep -v "^+++" | sed 's/^.//'| sed s/[[:space:]]//g |sed '/^$/d'|wc -l`
        TOTAL=$((TOTAL+count))
        rm -rf $TEMPFILE
    done    
    echo "$TOTAL" 
fi
