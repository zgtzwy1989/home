import yagmail
class wy_emaill_send():
	def __init__(self,wy_password,emaill_subject,emaill_contents,emaill_send_name):
		self.wy_password=wy_password
		self.emaill_contents=emaill_contents
		self.emaill_subject=emaill_subject
		self.emaill_send_name=emaill_send_name
	def emaill_set(self):
		yag=yagmail.SMTP(user="tz_wangyu@126.com",password=self.wy_password,host="smtp.126.com")
		contents=[self.emaill_contents]
		yag.send([self.emaill_send_name],self.emaill_subject,contents)
		print("结束")
password=input("请输入密码：")
subject=input("请输入主题：")
contents=input("请输入内容：")
send_name=input("请输入收件人：")
t=wy_emaill_send(password,subject,contents,send_name)
t.emaill_set()


