import tkinter as tk
import tkinter.messagebox
def reply():##弹窗窗口
	sql1=tk.Tk()
	sql1.title("查询软件")
	sql1.geometry("400x300")
	sql1.mainloop()
sql=tk.Tk()
sql.title("查询软件")
sql.geometry("400x300")
id_label=tk.Label(text="id:").place(x=20,y=0)
id_input=tk.Entry().place(x=60,y=0)
name_label=tk.Label(text="商户名称:").place(x=0,y=30)
name_input=tk.Entry().place(x=60,y=30)
seclet_button=tk.Button(sql,text="查询",command=reply).place(x=300,y=30)



sql.mainloop()