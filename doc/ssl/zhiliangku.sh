#!/bin/bash

function start(){
    rm -fr /usr/local/openresty/nginx/html/templates/*
    cp -r  /usr/local/zhiliangku/zhiliangku-front/front/*  /usr/local/openresty/nginx/html/templates/
    cp -r /usr/local/zhiliangku/templates/* /usr/local/openresty/nginx/html/templates/
    cp -r /usr/local/zhiliangku/doc/image /usr/local/zhiliangku/media/
    cp -r /usr/local/zhiliangku/doc/flag /usr/local/zhiliangku/media/
    cp -r /usr/local/zhiliangku/doc/custom_user_avatar /usr/local/zhiliangku/media/
    mkdir -p /usr/local/openresty/nginx/html/templates/static/images
    sudo python /usr/local/zhiliangku/manage.py collectstatic

    #cp -r  /usr/local/zhiliangku/zhiliangku-front/front  /tmp
    #cp -r /tmp/front/static   /usr/local/openresty/nginx/html/templates/
    #rm -rf  /tmp/front/static
    #cp -r  /tmp/front/*    /usr/local/openresty/nginx/html/templates/
    #rm -rf  /tmp/front
    #cp -r /usr/local/zhiliangku/templates/* /usr/local/openresty/nginx/html/templates/
    /usr/local/bin/uwsgi --ini /usr/local/zhiliangku/conf/zhiliangku.ini -d /tmp/log/zhiliangku/zhiliangku.log
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
