#!/bin/bash

function start(){
    cp -r  /usr/local/zhiliangku/zhiliangku-front/front/*  /usr/local/zhiliangku/templates/
    cp -r /usr/local/zhiliangku/doc/image /usr/local/zhiliangku/media/
    cp -r /usr/local/zhiliangku/doc/flag /usr/local/zhiliangku/media/
    cp -r /usr/local/zhiliangku/doc/custom_user_avatar /usr/local/zhiliangku/media/
    python /usr/local/zhiliangku/manage.py collectstatic
    uwsgi --ini /usr/local/zhiliangku/conf/zhiliangku.ini -d /tmp/log/zhiliangku/zhiliangku.log
}


function stop() {
    pid=`ps -ef | grep uwsgi | grep zhiliangku | awk -F " " '{print $2}'`
    echo $pid
    kill -9 $pid
}

function status(){
    ps -ef | grep uwsgi| grep zhiliangku
}



case "$1" in
    start)
    start;;
    stop)
    stop;;
    status)
    status;;
    *)
    echo  $"Usage: $0 {start|stop|}"
    exit 2
esac
