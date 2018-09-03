#!/bin/bash

cp -r  /usr/local/zhiliangku/zhiliangku-front/front  /tmp



cp -r /tmp/front/static   /usr/local/openresty/nginx/html/templates/

rm -rf  /tmp/front/static


cp -r  /tmp/front/*    /usr/local/openresty/nginx/html/templates/

rm -rf  /tmp/front
