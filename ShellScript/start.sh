#!/bin/bash
echo "程序正在启动......"
java -Djava.ext.dirs="../lib" -cp ../lib/program.jar com.company.start&
echo "程序启动成功"
