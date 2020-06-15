from urllib import request
import chardet

if __name__=="__main__":
	url='http://js.aisino.com/'
	rep=request.urlopen(url)
	print(type(rep))
	print(rep)
	print('url{}'.format(rep.geturl()))
	print('info{}'.format(rep.info()))
	print('code{}'.format(rep.getcode()))
	


