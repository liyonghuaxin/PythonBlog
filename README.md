# blog

博客地址：[http://www.haoshuiguo.vip](http://www.haoshuiguo.vip)

#### 配置环境
环境：nginx+uWSGI+django  
运行原理：the web client <-> the web server <-> the socket <-> uwsgi <-> Django  
linux系统：Debian9  
虚拟环境：python3.5.3 django2.0.5（查看命令python -m django --version）  
数据库：mysql（Server version: 10.1.26-MariaDB-0+deb9u1 Debian 9.1）  

项目位置：  
/home/lyh/sites/pythonBlog  
虚拟环境：/home/lyh/sites/venv  
nginx配置：/etc/nginx
uWSGI安装在虚拟环境下, 配置文件在根目录下 


安装pip、virtualenv并创建虚拟环境venv
* apt install python3-pip
* pip3 install virtualenv
* virtualenv --no-site-packages venv

配置虚拟环境
* pip install django
* pip install django-haystack
* pip install django_pure_pagination
* pip install whoosh django-haystack jieba
* pip install mysqlclient  
[PyMySQL/mysqlclient-python](https://github.com/PyMySQL/mysqlclient-python)  apt-get install python-dev libmysqlclient-dev  
[libmysqlclient-dev安装失败](https://otland.net/threads/libmysqlclient-dev-debian-stretch.253851/)  解决 apt-get install default-libmysqlclient-dev  
* pip install markdown
#### 描述 Description
用python搭建自己的博客  
#### 学习资料
[『Django实战』](https://ke.qq.com/course/274447)
#### 结语
Web开发除了掌握最基础的Web框架，还需要掌握常用的Web功能和开发技术，例如电商网站的购物车功能模块等...  
技术只是载体，实现了需求才体现了它的价值
#### 相关文档
[uWSGI](http://uwsgi-docs.readthedocs.io/en/latest/index.html)  
[Setting up Django and your web server with uWSGI and nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html?highlight=nginx)  
[Django 安全配置(setting.py)详解](https://segmentfault.com/a/1190000003756582)  
#### 遇到的问题
[解决Django Admin管理界面样式表(CSS Style)丢失问题](http://wangye.org/blog/archives/572/)  

测试uWSGI启动django时，权限不同  
uwsgi --socket mysite.sock --module demo.wsgi --chmod-socket=666 成功  
uwsgi --socket mysite.sock --module demo.wsgi --chmod-socket=664 失败了  

配置文件uwsgi.ini
note-site = true 访问失败显示 Internal Server Error

#### 其它
##### python 
root@localhost:/home/lyh# whereis python3  
python3: /usr/bin/python3.5m /usr/bin/python3.5 /usr/bin/python3 /usr/lib/python3.5 /usr/lib/python3 /etc/python3.5 /etc/python3 /usr/local/lib/python3.5 /usr/share/python3 /usr/share/man/man1/python3.1.gz 


##### MySQL：  
root@localhost:/home/lyh# whereis mysql  
mysql: /usr/bin/mysql /etc/mysql /usr/include/mysql /usr/share/mysql /usr/share/man/man1/mysql.1.gz  

查看mysql运行状态：service mysql status  或        systemctl status mysql.service    [systemctl命令](http://man.linuxde.net/systemctl)  

create database pyBlogDb;

增加MySQL用户并赋予相关权限
grant select,insert,update,delete,create,alter,index on *.* to user_1@"%" Identified by "123"; 

##### 查看端口号
lsof -i:80  

##### nginx
root@localhost:/home/lyh/sites# whereis nginx  
nginx: /usr/sbin/nginx /usr/lib/nginx /etc/nginx /usr/share/nginx /usr/share/man/man8/nginx.8.gz  
ps -ef | grep nginx    查看nginx进程

##### uWSGI
uwsgi --version   # 查看 uwsgi 版本  

ps ax | grep uwsgi    查看uwsgi进程  

在uwsgi9090.ini所在目录运行uwsgi --ini uwsgi9090.ini启动django项目  
其它相关命令 nohup uwsgi --ini uwsgi9090.ini& &nbsp; &nbsp; tail -f -n 1000 nohup.out  

在相关文件下运行，文件位置由uwsgi配置文件确定  
uwsgi --ini uwsgi.ini             # 启动  
uwsgi --reload uwsgi.pid          # 重启  
uwsgi --stop uwsgi.pid            # 关闭  








