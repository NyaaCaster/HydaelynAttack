# HydaelynAttack ![](https://img.shields.io/apm/l/vim-mode) ![](https://img.shields.io/github/stars/NyaaCaster/HydaelynAttack?style=social)
## 简易定制化DDOS打击工具，可用于自动打击部署

*倾听……感受……思考……*

## 前言

这只是为了维护艾欧泽亚不受钓鱼诈骗网站干涉而定制的自动打击策略，故很多参数写死定向打击特定网站，虽然根据实际情况，有能力编辑者脚本中最好自己维护打击目标，但请不要滥用于其他途径。
**注意，本项目攻击方式流量消耗很大，每轮打击消耗约12M流量，计费制网络资源用户请规划好自己的开销计划。**

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
------
## 脚本文件说明
- [x] HydaelynAttack.py *基本款，对ffwecc.top fwess.top liwuhe51.top三个网站同时循环打击，咏唱时间120秒，复唱时间60~600秒随机*
- [x] HydaelynAttack_ffwecc.py *只循环打ffwecc.top，咏唱时间120秒，复唱时间60~600秒随机*
- [x] HydaelynAttack_fwess.py *只循环打fwess.top，咏唱时间120秒，复唱时间60~600秒随机*
- [x] HydaelynAttack_liwuhe51.py *只循环打liwuhe51.top，咏唱时间120秒，复唱时间60~600秒随机*
- [x] HydaelynAttack_p.py *携作版，使用前用 git pull 指令更新项目，获得我发布的最新打击目标，执行本脚本携同我一起打击，咏唱时间120秒，复唱时间60~600秒随机*
- [x] HydaelynAttack_p_once.py *携作版部署版，一次性执行，用于crontab等计划任务定时部署,使用前用 git pull 指令更新获得统一目标，咏唱时间120秒*

## TO DO
- [ ] 集成到ACT高级触发器里自动执行
