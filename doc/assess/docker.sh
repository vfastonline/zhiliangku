#!/bin/bash
# $1=容器名称
# $2=容器端口
# $3=镜像端口
# $4=镜像名称

function start(){
    flag=`docker ps | grep $2 | wc -l`
    if [ $flag -eq 1 ]
    then
        imageid=`docker ps | grep kaohe | awk '{print $1}'`
    else
        tmpid=`docker run -it --rm -d  -v /usr/local/share/xiaodu/script/$5:/usr/local/share/xiaodu/script/$5  -p $2:$3 --name '$1' $4`
        imageid=${tmpid:0:12}
    fi
    echo {\"code\":0, \"imageid\":\"$imageid\"}

}

function stop() {
    docker kill $2 > /dev/null
    flag=`docker ps | grep $2 | wc -l`
    echo $flag
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