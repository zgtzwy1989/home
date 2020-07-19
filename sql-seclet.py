import tkinter as tk
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import StringVar
import pymysql
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
selcet_name=tk.Label(text="数据查询功能").place(x=0,y=0)
id_label=tk.Label(text="id:").place(x=20,y=30)
e=StringVar()
id_input=tk.Entry(sql,textvariable=e).place(x=60,y=30)
name_label=tk.Label(text="商户名称:").place(x=0,y=60)
name_input=tk.Entry().place(x=60,y=60)
seclet_button=tk.Button(sql,text="查询",command=reply).place(x=300,y=30)

sql.mainloop()
