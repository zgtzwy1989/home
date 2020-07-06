import tkinter as tk
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from tkinter import StringVar


def reply():##弹窗窗口
	p=StringVar()
	sql1=tk.Toplevel()
	sql1.title("查询软件")
	sql1.geometry("400x300")
	id_label_min=tk.Label(sql1,text=f"{e.get()}").place(x=0,y=10)
	p=StringVar()
	p.set(e.get())
	p=StringVar()
	id_input=tk.Entry(sql1,text=f"{e.get()}",textvariable=p).place(x=20,y=10)
	name_label_min=tk.Label(sql1,text="商户名称").place(x=120,y=10)
	#name_input_min=tk.Entry(sql1).place(x=180,y=10)
	img=Image.open(r"C:\\Users\\Administrator\\Desktop\\timg.jpg")#图片地址
	img=img.resize((300,200),Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	sss=tk.Label(sql1,image=img).place(x=0,y=60)
	sql1.mainloop()

sql=tk.Tk()
sql.title("查询软件")
sql.geometry("400x300")
id_label=tk.Label(text="id:").place(x=20,y=0)
e=StringVar()
id_input=tk.Entry(sql,textvariable=e).place(x=60,y=0)
name_label=tk.Label(text="商户名称:").place(x=0,y=30)
name_input=tk.Entry().place(x=60,y=30)
seclet_button=tk.Button(sql,text="查询",command=reply).place(x=300,y=30)
sql.mainloop()


