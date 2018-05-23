#!/bin/bash
# $2=容器名称
# $3=容器端口
# $4=镜像端口
# $5=镜像名称
# $6=考核脚本名称

function start(){
    flag=`docker ps | grep $2 | wc -l`
    if [ $flag -eq 1 ]
    then
        imageid=`docker ps | grep $2 | awk '{print $1}'`
    else
        tmpid=`docker run -it --rm -d  -v /usr/local/share/xiaodu/script/$6:/usr/local/share/xiaodu/script/$6  -p $3:$4 --name $2 $5`
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
    start docker $2 $3 $4 $5 $6;;
    stop)
    stop docker $2;;
    *)
    echo  $"Usage: $0 {start|stop|}"
    exit 2
esac