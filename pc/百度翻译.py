import urllib.request
import urllib.parse
import json
url="https://fanyi.baidu.com/sug"
headers={
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
		
		}
post_data={"kw":"s"}
data=urllib.parse.urlencode(post_data).encode()

pos=urllib.request.Request(url=url,headers=headers)
#或者在Request中传入dat apos=urllib.request.Request(url=url,headers=headers,data=data,method="POST")

hml=urllib.request.urlopen(pos,data=data)
hml=hml.read().decode()
print(json.loads(hml))#json解析