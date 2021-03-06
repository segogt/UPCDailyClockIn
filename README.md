# UPCDailyClockIn

疫情防控通的自动打卡脚本

# 如何使用？

1. 修改dailyClockIn.py中的username和pwd为对应的学号和数字石大密码
2. 把脚本放到自己的服务器上，这里以阿里云的ubuntu服务器为例，我放到了`/root/code/dailyClockIn.py`这个位置，然后编辑`/etc/crontab`，写入

```bash
5 0   * * *   root    python3 /root/code/dailyClockIn.py.py >> /root/code/output.log
```

[![rtmeUK.png](https://s3.ax1x.com/2020/12/18/rtmeUK.png)](https://imgchr.com/i/rtmeUK)

开头的5 0代表每天0点5分自动运行脚本，如果想修改时间，可以修改这里，第一个数字代表分钟，第二个代表小时，注意要有空格，后面的3个`*`代表每天都要打卡，不用改

3. 如果没服务器，只能每天手动运行一下脚本

# Tips

1. 本脚本中每日发送的地址都是`山东省青岛市黄岛区长江西路66号中国石油大学华东`，省份对应山东等，如果地址有变，请不要使用
2. 本脚本只适用于python3，如果还未安装，可以通过以下命令安装所需依赖(以ubuntu为例)
```bash
sudo apt install python3
sudo apt install python3-pip
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
```

# LICENSE

dailyClockIn is published under the `GNU GENERAL PUBLIC LICENSE`.See [LICENSE](LICENSE)