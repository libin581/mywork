#! /bin/bash

dbgecho()
{
[ ! -z "$DEBUG" ] && echo "$1"
}

what=aaa
DEBUG=on
dbgecho $what

what=bbb
DEBUG=
dbgecho $what



