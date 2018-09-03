#!/usr/bin/env bash
basepath=$(cd `dirname $0`; pwd)

# 多服务器用空格分隔
SERVERS="47.93.229.122"
PASSWORD=K4j5%6B5J#W^j1pJ

auto_ssh_copy_id() {
    expect -c "set timeout -1;
        spawn ssh-copy-id root@$1; 
        expect {
            *(yes/no)* {send -- yes\r;exp_continue;}
            *assword:* {send -- $2\r;exp_continue;}
            eof        {exit 0;}
        }";
}

ssh_copy_id_to_all() {
    for SERVER in $SERVERS
    do
        auto_ssh_copy_id $SERVER $PASSWORD
    done
}

ssh_copy_id_to_all


for SERVER in $SERVERS
do
    scp -r $basepath root@$SERVER:/root/
    scp -r ../../dist/*.tar.gz root@$SERVER:/root/deploy
    ssh root@$SERVER /root/deploy/deploy.sh
done