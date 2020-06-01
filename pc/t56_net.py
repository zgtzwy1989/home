import os
from urllib import request,parse
import bs4 
import chardet
url='http://bbs.t56.net/'
headers = {
	
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
	}
pas=request.Request(url=url ,headers=headers)
html=request.urlopen(pas)
html=html.read().decode('gbk')



soup=bs4.BeautifulSoup(html,"html.parser")
i=soup.find("ul",class_="phb_box phb_style_one").find_all("a")
with open("./每日新闻","w",encoding="utf-8") as f:
	for new in i:
		z=new.get_text("title")
		
		url1=parse.quote(new.get("href"))
		url1=url+url1
		
		f.write(z+"\n")
		f.write(url1+"\n")
f.close()
