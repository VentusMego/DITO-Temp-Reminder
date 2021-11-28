from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import re
import time
from dateutil import parser
import datetime
import requests

SECRETPASS = os.environ['SECRETPASS']
SECRETPHONE = os.environ['SECRETPHONE']
SECRETSCKEY = os.environ['SECRETSCKEY']

api = "https://sctapi.ftqq.com/"+ SECRETSCKEY +".send"

def check_func(word, url):
    return url in word

def send_server(receiver, text):
    data = {
        'text':receiver, #标题
        'desp':text} #内容
    result = requests.post(api, data = data)
    return(result)

#目前已经迁移完毕，等待Actions配置与关键信息隐藏
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
#打开 DITO 个人登录页
driver.get("https://my.dito.ph/")
driver.find_element_by_css_selector(".ant-input:nth-child(2)").send_keys(SECRETPHONE)
driver.find_element_by_id("PasswordLoginForm_password").send_keys(SECRETPASS)
driver.find_element_by_css_selector(".ant-btn > span").click()
#logged in 但有弹窗，因为没有Cookies
sleep(0.5)
#/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]
# 
driver.find_element_by_xpath("//*/div[2]/div/div[2]/div/div[2]/div[3]/button[2]").click()
#driver.get("https://my.dito.ph/pto/home")
sleep(0.5)
#进入个人页，即抓取页面
html = driver.page_source   #抓取页面内容
#print(html)，内有具体流量内容

#抓出来的部分在另一个py文件中
nowtime = datetime.datetime.now()
sharedvaildtime1regex = re.compile(r'Shared Data(.*?)</div>')
sharedvaildtime2regex = re.compile(r'Valid until:  (.*?)</p>')
sharedvaildtime1 = sharedvaildtime1regex.findall(html)
print(sharedvaildtime1)
sharedvaildtime = sharedvaildtime2regex.findall(sharedvaildtime1[0])
print(sharedvaildtime[0])
print("剩余流量过期时间: " + str(parser.parse(sharedvaildtime[0])-nowtime))
#可以显示但是需要一个好的计算方式

#同上，流量筛选两遍，主要看流量是否多于1GB，即区分MB、GB字样
sharedvailddata1regex = re.compile(r'Shared Data(.*?</span></p></div></div></div>)')
sharedvailddata2regex = re.compile(r'><span>(.*?) MB')
sharedvailddata1 = sharedvailddata1regex.findall(html)
print(sharedvailddata1)
if check_func(sharedvailddata1[0], 'MB'):
    sharedvailddata = sharedvailddata2regex.findall(sharedvailddata1[0])
    print("流量剩余" + sharedvailddata[0] + "MB")
else:
    print("流量充足")

if check_func(str(parser.parse(sharedvaildtime[0])-nowtime), 'day'):
    if check_func(sharedvailddata1[0], 'MB'):
        req = send_server("DITO流量不足","DITO时间：**" + str(parser.parse(sharedvaildtime[0])-nowtime) + "** DITO流量：**" + sharedvailddata[0] + "MB**")
    else:
        print("完全充足，测试成功")
else:
    if check_func(sharedvailddata1[0], 'MB'):
        req = send_server("DITO时间、流量不足","DITO时间：**" + str(parser.parse(sharedvaildtime[0])-nowtime) + "** DITO流量：**" + sharedvailddata[0] + "MB**")
    else:
        req = send_server("DITO时间不足","DITO时间：**" + str(parser.parse(sharedvaildtime[0])-nowtime) + "** DITO流量：**" + sharedvailddata[0] + "MB**")


