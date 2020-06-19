#coding=utf-8
from bs4 import BeautifulSoup
import time
import openpyxl
import requests

# 使用代理
# 代理IP以字典形式写出来
proxy = {'http': '127.0.0.1:10809','https': '127.0.0.1:10809'}
#http://127.0.0.1:10809
list_gx=[]
for pa in range(0,100,10):
    
    url = 'https://www.google.com/search?q=%E5%85%B1%E4%BA%AB%E8%B4%A6%E5%8F%B7&hl=zh_cn&ei=aTHsXuy1HKbxhwPT3YawCA&start='+str(pa)+'&sa=N&ved=2ahUKEwisjt6n-IzqAhWm-GEKHdOuAYY4ChDy0wN6BAgMEDI&biw=1365&bih=925'
    headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers,verify=False, proxies=proxy)
    #发起请求，verify=False添加下，关闭https网站证书验证
    time.sleep(2)

    pageSource = r.text
    soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
    #print(soup)
    items=soup.find_all(class_="r")
    
    for item in items:
        title=item.find('a')
        #提取网页url和标题所在标签模块
        #print(title.text,title['href'])
    
        list_gx.append([title.text,title['href']])
        #提取网页url和标题文本，并添加到列表list_gx中
    print(list_gx)


wb = openpyxl.Workbook()
#利用openpyxl.Workbook()函数创建新的workbook（工作簿）对象，就是创建新的空的Excel文件
sheet = wb.active
#wb.active就是获取这个工作簿的活动表，通常就是第一个工作表
sheet.title = '共享账号'
#可以用.title给工作表重命名
sheet['A1']='名称'
sheet['B1']='地址'

for i in list_gx:
    sheet.append(i)

wb.save('Marvel.xlsx')

