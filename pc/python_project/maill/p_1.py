from urllib import request
import chardet

if __name__=="__main__":
	url='http://js.aisino.com/'
	rsp=request.urlopen(url)
	html=rsp.read()#读出解析内容
	#将也买你导入字典
	cs=chardet.detect(html)
	print(cs)
	
	#打印出来的内容解码
	#使用get取值不会出错
	html=html.decode(cs.get('encoding',"utf-8"))
	print(html)


