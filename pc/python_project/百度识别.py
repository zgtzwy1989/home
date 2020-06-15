 
# encoding:utf-8

import requests
import base64



'''
通用文字识别
'''
                   
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('123.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"detect_direction":270}
access_token = '24.8d1dc706e43c58301199d4eec4c1bd0a.2592000.1593769338.282335-18570318'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
p=response.json()
print(p)
for item in p['words_result']:
    print(item['words'])
