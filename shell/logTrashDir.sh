#! /bin/bash

if [ ! -f ~/trash/.log ]
then
    touch ~/trash/.log
    chmod 700 ~/trash/.log
fi

echo $1 $2 $3 $4>> ~/trash/.log
