from selenium import webdriver
from time import sleep
import re
import time
from dateutil import parser
import datetime

def check_func(word, url):
    return url in word

driver=webdriver.Chrome()
#打开 DITO 个人登录页
driver.get("https://my.dito.ph/")
driver.find_element_by_css_selector(".ant-input:nth-child(2)").send_keys('【手机号，格式为XX XXXX XXX，包括空格】')#填入手机号
driver.find_element_by_id("PasswordLoginForm_password").send_keys('【固定密码】')#六位个人密码
driver.find_element_by_css_selector(".ant-btn > span").click()
#logged in 但有弹窗，因为没有Cookies
sleep(2)
#/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]
# 
driver.find_element_by_xpath("//*/div[2]/div/div[2]/div/div[2]/div[3]/button[2]").click()
#driver.get("https://my.dito.ph/pto/home")
sleep(2)
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
print("剩余流量过期时间" + str(parser.parse(sharedvaildtime[0])-nowtime))
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

#TBD 基于Server酱的消息通知