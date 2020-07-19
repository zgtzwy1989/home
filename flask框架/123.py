from flask import Flask,render_template,request
import pymysql
import json
app = Flask(__name__)

@app.route('/')
def index():
	 #1、获取留言板数据
    data=why("select * from 工作表")
 
    return render_template("./index.html",data=data)
#定义视图，显示留言添加的页面
@app.route("/add")
def add():
	#显示留言添加页面
	return render_template("./add.html") 
#定义视图函数，接受表单数据，完成数据入库
@app.route("/insert",methods=["post"])
def insert():
	#1.接受数据
	qq=request.form.to_dict()
	#2.把数据接入
	sql='insert into 工作表 ("id","merchantsname","image_url","remarks" ) values (f"{qq[info]}",f"{qq[nikenam]}")'
	why(sql)
	return "完成"
	#2、把数据分配到模板中（html）

def why(sql):
	#封装mysql操作
	conn = pymysql.connect(host='localhost', port=3306, user='root', 
            passwd='cq123456', db='农行业务', charset='utf8')
	try:
		#获取数据库游标
		con=conn.cursor()
		#执行sql语句，返回行数
		row=con.execute(sql)
		conn.commit()#提交数据库
		#获取数据库(fetchall()全部数据库，fetchone()单行数据库)
		data=con.fetchall()
		print(data)
		if data:
			return data
		else:
			return row
		
	except:
		conn.rollback()   #回滚
	finally:
		conn.close()
if __name__ == '__main__':
	app.run(host="127.0.0.3",debug=False,port=7325)