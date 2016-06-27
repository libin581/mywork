#! /bin/bash

dirs -v
dirs -v


read opt
if [ $opt -ne 0 ];then
    opt=$(($opt-1))
    popd 1>/dev/null
    pushd +$opt 1>/dev/null
    pushd . 1>/dev/null
else
    return
fi

