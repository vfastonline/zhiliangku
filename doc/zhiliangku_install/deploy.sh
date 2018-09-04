#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)
openresty_repo=$basepath"/openresty_repo"
user=vfast

yum_install() {
    yum -y install zlib* openssl* mysql-server mysql mysql-devel libuuid-devel *gcc* wget
}


mysql_(){
    service mysqld restart
    mysqladmin -u root password '111111'
    if [ -f "$basepath/vfast.sql" ]; then
        mysql -uroot -p111111 < $basepath/vfast.sql
    fi
}

python_(){
    wget http://python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz --no-check-certificate
    xz -d Python-3.6.3.tar.xz
    tar -xvf Python-3.6.3.tar
    cd Python-3.6.3
    ./configure
    if [ $? -ne 0 ]; then
        echo "configure err"
    else
        make all && make install
    fi
    make clean && make distclean
    cd -
}

set_python(){
    echo `/usr/local/bin/python3.6 -V`
    if [ $? -ne 0 ]; then
        echo "failed"
    else
        mv /usr/bin/python /usr/bin/python2.7.bak
        ln -s /usr/local/bin/python3.6 /usr/bin/python
        sed -i 's/python/python2.7/' /usr/bin/yum
    fi
}

pip_(){
    wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
    python get-pip.py
    echo `pip -V`
    pip install uwsgi
}


add_openresty_repo(){
    cat $openresty_repo >> /etc/yum.repos.d/CentOS-Base.repo

    yum -y install openresty
    yum -y install openresty-resty
    yum -y groupinstall "Development Tools"
    yum -y install pcre-devel openssl-devel
}

zhiliangku_(){
    if [ ! -d "/usr/local/zhiliangku" ];then
        mkdir -p /usr/local/zhiliangku
    fi
    tar -zxvf $basepath/zhiliangku-1.0.tar.gz -C /usr/local/zhiliangku --strip-components 1
    cd /usr/local/zhiliangku
    python setup.py build
    python setup.py install
    cd -
}



nginx_conf(){
    if [ ! -d "/usr/local/openresty/nginx/conf/servers" ];then
        mkdir -p /usr/local/openresty/nginx/conf/servers
    fi
    cp -r  $basepath/zhiliangku.conf /usr/local/openresty/nginx/conf/servers/
    sed -i '$i\include servers/*.conf;' /usr/local/openresty/nginx/conf/nginx.conf
    /usr/local/openresty/nginx/sbin/nginx -t
    /usr/local/openresty/nginx/sbin/nginx -c /usr/local/openresty/nginx/conf/nginx.conf
}

uwsgi_(){
    egrep "^$user" /etc/passwd >& /dev/null
    if [ $? -ne 0 ]
    then
        useradd $user
    fi

    cp -r $basepath/zhiliangku.sh /etc/init.d/
    /etc/init.d/zhiliangku.sh stop
    /etc/init.d/zhiliangku.sh start
}

set_startup(){
    sed -i '$a\\n/usr/local/openresty/nginx/sbin/nginx -c /usr/local/openresty/nginx/conf/nginx.conf' $1
    sed -i '$a\sh /etc/init.d/uwsgi stop' $1
    sed -i '$a\sh /etc/init.d/uwsgi start' $1
    sed -i '$a\sh service mysqld restart' $1
}

echo "正在安装 zlib* openssl* mysql-server mysql mysql-devel libuuid-devel *gcc* wget"
yum_install
mysql_
python_
set_python
pip_
add_openresty_repo
zhiliangku_
nginx_conf
uwsgi_
set_startup /etc/rc.local