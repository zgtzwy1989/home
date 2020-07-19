import tkinter as tk
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import StringVar
import pymysql,tkinter.ttk#复选菜单模块,threading
'''
全局变量
insert_id_input_zhu     主界面 
insert_name_input_zhu
'''


def mysql_jk_insert(sql):#插入数据接口
	conn=pymysql.connect(user="root",host="localhost",passwd="cq123456",db="业务",port=3306,charset="utf8")
	cur=conn.cursor()
	cur.execute(sql)
	conn.commit()
	conn.close()
	return "ok"


	
def ibsert_information():#电话预约录入按钮接口
	A=insert_id.get()
	B=insert_name.get()
	C=insert_pos_information.get()


	
	if C=="pos退回":
		sql=f'INSERT into `电话联系表`values({int(A)},"{B}",1);'
		my_sql=mysql_jk_insert(sql)
		insert_id_input.delete(0,"end")
		insert_name_input.delete(0,"end")
		insert_is_pos_Information.current(0)	
	if C=="pos丢失":
		sql=f'INSERT into `电话联系表`values({int(A)},"{B}",2);'
		my_sql=mysql_jk_insert(sql)
		insert_id_input.delete(0,"end")
		insert_name_input.delete(0,"end")
		insert_is_pos_Information.current(0)	
		
	if C=="pos正常":
		sql=f'INSERT into `电话联系表`values({int(A)},"{B}",0);'
		my_sql=mysql_jk_insert(sql)
		insert_id_input.delete(0,"end")
		insert_name_input.delete(0,"end")
		
def reply():##弹窗窗口
	
	s=e.get()
	print(type(s))

	
	conn = pymysql.connect(host='localhost', port=3306, user='root', 
            passwd='cq123456', db='业务', charset='utf8')
	cour=conn.cursor()
	effect_cour=cour.execute(f"SELECT * FROM world WHERE Merchant_id LIKE '%{s}%'")
	p=cour.fetchone()
	print(p)
	p0=p[0]
	p1=p[1]
	p2=p[2]
	cour.close()
	sql1=tk.Toplevel()
	sql1.title("查询软件")
	sql1.geometry("600x500")
	id_label_min=tk.Label(sql1,text=f"id:").place(x=0,y=10)
	id_man=StringVar()
	id_man.set(p0)
	id_input_min=tk.Entry(sql1,textvariable=id_man).place(x=20,y=10)
	name_label_min=tk.Label(sql1,text="商户名称").place(x=120,y=10)
	name_man=StringVar()
	name_man.set(p1)
	name_input_min=tk.Entry(sql1,textvariable=name_man).place(x=180,y=10)
	img=Image.open(r"E:\\img\\{}.jpg".format(p2))
	img=img.resize((500,400),Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	sss=tk.Label(sql1,image=img).place(x=0,y=60)
	sql1.mainloop()

sql=tk.Tk()
sql.title("查询软件")
sql.geometry("400x300")
selcet_name=tk.Label(sql,text="数据查询功能(查询商户名字不好用)").place(x=0,y=0)
id_label=tk.Label(sql,text="id:").place(x=20,y=30)
e=StringVar()
id_input=tk.Entry(sql,textvariable=e).place(x=60,y=30)
name_label=tk.Label(sql,text="商户名称:").place(x=0,y=60)
name_input=tk.Entry().place(x=60,y=60)
seclet_button=tk.Button(sql,text="查询",command=reply).place(x=300,y=30)
#电话预约录入：
insert_name_label_BT=tk.Label(sql,text="预约录入功能").place(x=0,y=150)#标题
insert_burron=tk.Button(sql,text="电话联系预约",width=13,command=ibsert_information).place(x=270,y=180)
insert_id_label=tk.Label(sql,text="id:").place(x=20,y=180)

insert_id=StringVar()
insert_id_input=tk.Entry(sql,textvariable=insert_id)
insert_id_input.place(x=50,y=180)#修饰后可能会转义
insert_name_label=tk.Label(sql,text="商户名称:").place(x=0,y=210)

insert_name=StringVar()
insert_name_input=tk.Entry(sql,textvariable=insert_name)
insert_name_input.place(x=60,y=210)
insert_pos_information=StringVar()
insert_is_pos_Information_label=tk.ttk.Label(sql,text="特殊情况说明:").place(x=0,y=240)
insert_is_pos_Information=tk.ttk.Combobox(sql,values=["pos正常","pos退回","pos丢失"],textvariable=insert_pos_information)
insert_is_pos_Information.place(x=80,y=240)
insert_is_pos_Information.current(0)	


sql.mainloop()
