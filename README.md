# blog
#### 配置环境
debian python目录
root@localhost:/home/lyh# whereis python3
python3: /usr/bin/python3.5m /usr/bin/python3.5 /usr/bin/python3 /usr/lib/python3.5 /usr/lib/python3 /etc/python3.5 /etc/python3 /usr/local/lib/python3.5 /usr/share/python3 /usr/share/man/man1/python3.1.gz
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


