from urllib import request,parse
import chardet

if __name__=="__main__":
	url='http://www,baidu.com/s?'
	
	qs={"wd":wd}
	qs=parse.urlencode(qs)
	fullurl=url+qs
	print(fullurl)
	rep=request.urlopen(fullurl)
	html=rsp.read()