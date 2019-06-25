#!/bin/bash
pid2=`ps -ef | grep program | grep -v grep | awk '{print $2}'`
if [ -z "${pid2}" ]; then
    echo "程序没有运行"
else
    echo "程序进程${pid2}"
    kill -9 $pid2
    echo "程序关闭"
fi
