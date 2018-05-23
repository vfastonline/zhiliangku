#!/bin/bash
# $1=容器名称
# $2=考核脚本名称

function kaohe(){
    flag=`docker ps | grep $1| wc -l`
    if [ $flag -eq 1 ]
    then
        msg=`docker exec $1 bash /usr/local/share/xiaodu/script/$2`
#        echo $msg
#        docker kill $1 > /dev/null
        echo  -e  {\"code\":0, \"msg\":\"$msg\", \"grade\":\"100\"}
#        echo  -e  $msg
    else
        echo -e {\"code\":1, \"msg\":\"考核容器未正确启动\",  \"grade\":\"0\"}
    fi
}


kaohe $1 $2
