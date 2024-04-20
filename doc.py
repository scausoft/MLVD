#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import subprocess

mount_path = "/data/docker_mysql5.7"   # 挂载路径

# my.cnf 配置文件
my_cnf = """[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
# Custom config should go here
#!includedir /etc/mysql/conf.d/
innodb_buffer_pool_size = 1G
skip-host-cache
skip-name-resolve    # 禁用dns解析
max_connections=1000 #最大连接数
"""

# 运行容器命令
run_cmd = r"""sudo docker run \
    -p 3307:3306 \
    -v /data/docker_mysql5.7/data:/var/lib/mysql \
    -v /data/docker_mysql5.7/cnf:/etc/mysql \
    -v /etc/localtime:/etc/localtime:ro \
    --privileged=true \
    --name docker_mysql5.7 \
    --restart always \
    -e MYSQL_ROOT_PASSWORD=123456 \
    -d mysql:5.7
"""


# docker 安装
def docker_install():
    docker_daemon = {"registry-mirrors": ["https://registry.docker-cn.com"]}   # daemon.json
    daemon_path = r"etc/docker/daemon.json"
    #docker检测是否安装
    if not os.system("docker version"):
        print("docker 已安装")
    else:
        print("docker 正在安装...")
        os.system("yum install docker -y")
        os.system("systemctl restart docker")
        os.system("systemctl enable docker")
        os.system("systemctl enable docker")
        with open(daemon_path, "w", encoding="utf-8") as f:
            json.dump(docker_daemon, f, ensure_ascii=False, indent=4)

# mysql 安装
def mysql_install(my_cnf: str, mount_path: str, docker_run: str):
    """
    my_cnf: str  # my.cnf
    mount_path: str   # 挂载的目录
    docker_run: str   #  docker run命令
    """
    os.system("docker pull mysql:5.7")    # 拉取镜像
    os.system("mkdir -p {}/cnf".format(mount_path))
    os.system("mkdir -p {}/data".format(mount_path))
    config_path = "{}/cnf/my.cnf".format(mount_path)
    with open(config_path, "w") as f:
        f.write(my_cnf)
    os.system(docker_run)
    os.system("docker ps -a |grep mysql")

docker_install()
mysql_install(my_cnf, mount_path, run_cmd)
