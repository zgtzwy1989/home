import os
import requests
import base64
import json
def aaa():
	
	with open("第二次名单.txt","w",encoding="utf-8") as w:
		d="C:\\Users\\think\\Desktop\\tp"
		for fileurl,fileurl_1,name in os.walk(d):
			
				
			for new_name in name:
				s=os.path.join(fileurl,new_name)
				request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

					# 二进制方式打开图片文件
				f = open(s, 'rb')
				img = base64.b64encode(f.read())


				params = {"image":img,"detect_direction":270}
				access_token = '24.8d1dc706e43c58301199d4eec4c1bd0a.2592000.1593769338.282335-18570318'
				request_url = request_url + "?access_token=" + access_token
				headers = {'content-type': 'application/x-www-form-urlencoded'}
				response = requests.post(request_url, data=params, headers=headers)
				p=response.json()
				print(p)
				num=0
				for item in p['words_result']:
					num+=1
					v=str(json.dumps(item,ensure_ascii=False))#python编码问题。否则会出现ascii问题
					
					if num==4:
						w.write(v + "\n")
	w.close()


					
			    
			    
if __name__ == '__main__':
	aaa()
