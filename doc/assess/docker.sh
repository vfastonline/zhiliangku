#!/bin/bash
# $1=容器名称
# $2=容器端口
# $3=镜像端口
# $4=镜像名称

function start(){
    flag=`docker ps | grep $1 | wc -l`
    if [ $flag -eq 1 ]
    then
        imageid=`docker ps | grep $1 | awk '{print $1}'`
    else
        tmpid=`docker run -it --rm -d  -v /usr/local/share/xiaodu/script/:/usr/local/share/xiaodu/script/  -p $2:$3 --name $2 $4`
        imageid=${tmpid:0:12}
    fi
    echo {\"code\":0, \"imageid\":\"$imageid\"}

}

function stop() {
    docker kill $1 > /dev/null
    flag=`docker ps | grep $2 | wc -l`
    echo $flag
}


case "$1" in
    start)
    start $2 $3 $4 $5;;
    stop)
    stop $2;;
    *)
    echo  $"Usage: $0 {start|stop|}"
    exit 2
esac