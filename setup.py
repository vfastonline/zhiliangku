# coding:utf-8
# package project

from setuptools import setup, find_packages

requires = [
	'django==2.1',
	'PyMySQL',
	'passlib==1.7.1',
	'mysqlclient',
	'requests==2.19.1',
	'django-colorfield==0.1.15',
	'Django-Select2==6.1.2',
	'django-suit==0.2.26',
	'pycrypto==2.6.1',
	'django-cors-headers==2.4.0',
	'django-multiselectfield==0.1.8',
	'django-breadcrumbs==1.1.3',
	'redis==2.10.6',
	'djangorestframework==3.8.2',
	'markdown==2.6.11',
	'django-filter==2.0.0',
	'ujson==1.35',
	'pillow==5.2.0',
	'channels',
	'Daphne',
	'asgiref',
	'channels_redis',
	'Twisted[tls,http2]',
]
# config,doc,media,templates,zhiliangku-front
setup(
	name="zhiliangku",
	version="1.0",

	author="xuhuiliang",
	author_email="593548215@qq.com",

	# 自动寻找带有 __init__.py 的文件夹
	packages=find_packages(exclude=["logs"]),

	install_requires=requires,

	description="zhiliangku",

	# 单独的一些py脚本,不是在某些模块中
	scripts=["manage.py"],

	# 静态文件等，配合MANIFEST.in (package_data 参数不太好使)
	include_package_data=True,

	# 如果是正式的项目，还会有更多的信息（例如开源证书写在下面）
	# url="http://wifi21.com",
)
