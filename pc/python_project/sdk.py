# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MsDKgLL58BDEv58tx5PLbeY6&client_secret=3WlfFUVO9G99uep8cuH4Vlgl67B8Yq8P'
response = requests.get(host)
if response:
   v=response.json()
   print(v['access_token'])
