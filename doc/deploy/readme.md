

### NGINX:
```
/usr/local/openresty/nginx/conf/nginx.conf 添加include servers/*.conf;
/usr/local/openresty/nginx/conf/servers/m.conf   nginx配置文件
```

### UWSGI:
```
/etc/init.d/uwsgi
```

### rc.local

```
/usr/local/openresty/nginx/sbin/nginx
sh /etc/init.d/uwsgi stop       
sh /etc/init.d/uwsgi start
```