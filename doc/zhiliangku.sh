#!/bin/bash

function start(){
    uwsgi --ini /usr/local/zhiliangku/conf/zhiliangku.ini -d /tmp/zhiliangku/zhiliang.log
}


function stop() {
    pid=`ps -ef | grep uwsgi | grep zhiliangku | awk -F " " '{print $2}'`
    echo $pid
    kill -9 $pid
}




case "$1" in
    start)
    start;;
    stop)
    stop;;
    *)
    echo  $"Usage: $0 {start|stop|}"
    exit 2
esac
