 
# encoding:utf-8

import requests
import base64



'''
通用文字识别
'''
                   
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"detect_direction":400}
access_token = '24.56ee4a3ce148e32b455dd119abae9009.2592000.1605366243.282335-18570318'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
p=response.json()
print(p)
for item in p['words_result']:
    print(item['words'])
    exit()