import requests,lxml.etree
import urllib3.request

url='http://www.66ip.cn/areaindex_10/1.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
response=requests.get(url=url,headers=headers)
response.encoding="gbk"
tree=lxml.etree.HTML(response.text)
list1=tree.xpath("//table/tr[position()>1]")
for i in list1:
	
	
	s=i.xpath('.//td[position()<3]/text()')
	print(s)
	
	proxies={"http":f"http://{s[0]}:{s[1]}",
			"https":f"https://{s[0]}:{s[1]}"}
	params={"wd":"ip"}
	try:
		response=requests.get(url="https://www.httpbin.org/ip",headers=headers,proxies=proxies,timeout=3)
		response.encoding="utf-8"
		
	except Exception as e:
		pass
	else:
		response.encoding="utf-8"
		print(response.text)
	finally:
		pass
	

	





