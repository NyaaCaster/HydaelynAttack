# HydaelynAttack
## 简易定制化DDOS打击工具，可用于自动打击部署

*倾听……感受……思考……*

## 前言

这只是为了维护艾欧泽亚不受钓鱼诈骗网站干涉而定制的自动打击策略，故很多参数写死定向打击特定网站，虽然根据实际情况，有能力编辑者脚本中最好自己维护打击目标，但请不要滥用于其他途径。

## 环境级工具

- [x] Linux
- [x] Python3
- [x] Python3-pip
- [x] Python3-pip tqdm
- [x] Python3-pip pyfiglet

## linunx系统语法注意
- 如果是ubuntu debian系的系统，命令前缀使用 apt
- 如果是centos redhead系的系统，命令前缀使用 yum
- 如果是非root权限账号，请在上述命令前加 sudo

## 安装
```shell
apt update -y
apt install git python3 python3-pip -y
pip3 install tqdm pyfiglet
git clone https://github.com/NyaaCaster/HydaelynAttack.git
```

## 运行
```shell
Python3 HydaelynAttack/HydaelynAttack.py
```
