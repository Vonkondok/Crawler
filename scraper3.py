from selenium import webdriver
import time

#生成驱动器
driver = webdriver.Chrome(executable_path = r'D:\chromedriver.exe')

#获取网页内容
driver.get("https://www.xfz.cn/")

#模拟点击按钮
button = driver.find_element_by_class_name("more-news")
button.click()

#延迟操作，等待刷新
time.sleep(2)

#获取指定内容
title_list = driver.find_elements_by_class_name("li-title")

for title in title_list:
    print(title.text)
    
# driver.quit()


"""选中 右键检查 一般通过classname来判断 有class上class 没class看copy 看copy XPATH 复制到剪贴板看看长啥样"""

'''
for i in range(20):
    name = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr['+ str(1+i) + ']/td[4]/a')
    date = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr['+ str(1+i) + ']/td[5]')
    number = driver.find_element_by_xpath('//*[@id="dbtable"]/tbody/tr['+ str(1+i) + ']/td[6]')
    print(name.text, date.text, number.text)
 '''   

'''you-get -o /Users/wrgdand/Desktop/下载视频 https://v.youku.com/v_show/id_XNTQwMTgxMTE2.html'''

import os

video_path = '/Users/wrgdand/Desktop/'
video_link = "https://v.youku.com/v_show/id_XNTUxMjUxMjQ=.html"

os.system('you-get -o %s %s' % (video_path,video_link))

