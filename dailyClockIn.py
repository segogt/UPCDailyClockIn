import requests
import re
import json
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os

# 如果不用邮箱的话，只写上自己的学号密码即可
username = "xxxxxx" # 学号
pwd = "xxxxxxx"    # 数字石大密码
need_mail=False  # 是否需要每天接收邮件提醒，需要就改成True，不需要就改成False

# 如果需要邮件提醒就修改下面的邮箱账号为自己的账号，并写入qq邮箱授权码，关于授权码如何获得可以自行搜索
my_sender='aaa@qq.com'    # 发件人邮箱账号,这里我写的qq邮箱，如果使用其他邮箱可以自行修改mail函数部分
my_pass = 'cefelcjbulnrbbjb'              # 发件人qq邮箱授权码
my_user='aaa@qq.com'      # 收件人邮箱账号，我这边发送给自己


# 以下部分无需修改
eai_sess="g95p4igbjfpmnfo5krhgdcnoj2"
print("\n\n--------------------------------------")
today = str(datetime.date.today()).replace('-','')
print(today)
print("--------------------------------------")
def mail(sub,content):
    ret=True
    try:
        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["来自自动打卡bot",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["我自己",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=sub               # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret=False
    return ret

def ClockIn():
    while True:
        try:
            # 登录
            session = requests.Session()
            paramsPost = {"password":pwd,"username":username}
            headers = {"Origin":"https://app.upc.edu.cn","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","Connection":"close","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36","Referer":"https://app.upc.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.upc.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex","Sec-Fetch-Site":"same-origin","Sec-Fetch-Dest":"empty","DNT":"1","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"cors","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
            cookies = {"eai-sess":eai_sess}
            response = session.post("https://app.upc.edu.cn/uc/wap/login/check", data=paramsPost, headers=headers, cookies=cookies,verify=False)
            UUkey=re.findall("UUkey=(\w+);",response.headers["Set-Cookie"])[0]
            headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Connection":"close","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36","Sec-Fetch-Site":"none","Sec-Fetch-Dest":"document","DNT":"1","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"navigate","Cache-Control":"max-age=0","Upgrade-Insecure-Requests":"1","Sec-Fetch-User":"?1","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"}
            cookies = {"Hm_lpvt_48b682d4885d22a90111e46b972e3268":"1607672880","UUkey":UUkey,"Hm_lvt_48b682d4885d22a90111e46b972e3268":"1607528712","eai-sess":eai_sess}
            response = session.get("https://app.upc.edu.cn/ncov/wap/default/index", headers=headers, cookies=cookies)
            id = re.findall('"id":(\w+)',response.text)[0]
            created = re.findall('"created":(\w+)',response.text)[0]
            # 第三部分，保存数据
            paramsPost = {"date":today,"gllx":"","tw":"3","jrsfqzfy":"","sfcxtz":"0","jcjg":"","sfygtjzzfj":"0","jcbhlx":"","sfzhbsxsx":"0","sftjwh":"0","bztcyy":"","sfsqhzjkk":"0","sfyqjzgc":"","gwszdd":"","province":"\x5c71\x4e1c\x7701","sqhzjkkys":"","ismoved":"0","id":id,"sfjcbh":"0","area":"\x5c71\x4e1c\x7701 \x9752\x5c9b\x5e02 \x9ec4\x5c9b\x533a","szcs":"","sfcyglq":"0","created":created,"fjsj":"20200820","sfzgsxsx":"0","szsqsfybl":"0","jcbhrq":"","szgj":"","sfyyjc":"0","qksm":"","fxyy":"","gtjzzfjsj":"","city":"\x9752\x5c9b\x5e02","sfcxzysx":"0","remark":"","sfjcwhry":"0","jrsfqzys":"","jcjgqr":"0","uid":"13630","sftjhb":"0","szgjcs":"","address":"\x5c71\x4e1c\x7701\x9752\x5c9b\x5e02\x9ec4\x5c9b\x533a\x957f\x6c5f\x8def\x8857\x9053\x534e\x4e1c\x8def\x4e2d\x56fd\x77f3\x6cb9\x5927\x5b66(\x534e\x4e1c)","sfzx":"1","sfjchbry":"0","jcqzrq":"","glksrq":"","geo_api_info":"{\"type\":\"complete\",\"position\":{\"Q\":35.940682237414,\"R\":120.17553249782998,\"lng\":120.175532,\"lat\":35.940682},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":30,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"0532\",\"adcode\":\"370211\",\"businessAreas\":[],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"\x957f\x6c5f\x897f\x8def\",\"streetNumber\":\"66\x53f7\",\"country\":\"\x4e2d\x56fd\",\"province\":\"\x5c71\x4e1c\x7701\",\"city\":\"\x9752\x5c9b\x5e02\",\"district\":\"\x9ec4\x5c9b\x533a\",\"township\":\"\x957f\x6c5f\x8def\x8857\x9053\"},\"formattedAddress\":\"\x5c71\x4e1c\x7701\x9752\x5c9b\x5e02\x9ec4\x5c9b\x533a\x957f\x6c5f\x8def\x8857\x9053\x534e\x4e1c\x8def\x4e2d\x56fd\x77f3\x6cb9\x5927\x5b66(\x534e\x4e1c)\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","sfjcqz":""}
            headers = {"Origin":"https://app.upc.edu.cn","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","Connection":"close","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36","Referer":"https://app.upc.edu.cn/ncov/wap/default/index","Sec-Fetch-Site":"same-origin","Sec-Fetch-Dest":"empty","DNT":"1","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"cors","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
            cookies = {"Hm_lpvt_48b682d4885d22a90111e46b972e3268":"1607529871","UUkey":UUkey,"Hm_lvt_48b682d4885d22a90111e46b972e3268":"1607528712","eai-sess":eai_sess}
            response = session.post("https://app.upc.edu.cn/ncov/wap/default/save", data=paramsPost, headers=headers, cookies=cookies,verify=False)
            res = json.loads(response.text)
            if res["e"]==1 and res["m"]=="今天已经填报了":
                if need_mail:
                    mail("打卡成功","{}:打卡成功\n".format(today))
                print("{}:打卡成功\n".format(today))
                exit()
        except Exception as e:
            if need_mail:
                mail("打卡失败","{0}:打卡失败，原因是{1}\n".format(today,e)) 
            print("{0}:打卡失败，原因是{1}\n".format(today,e))
        
if __name__ == "__main__":
    ClockIn()