import xlwt
import random


class excel(object):

	def set_up(new_name):
		workbook = xlwt.Workbook(encoding = 'utf-8')
		
		worksheet=workbook.add_sheet(new_name)
	
	def song(row,line,price):	
	    new=worksheet.write(row,line,price)
	def save(name_excel):
		nen=workbook.save(name_excel+".xls")


	
excel.set_up("wodetian")
for x in range(15):
	num=random.randint(1,9)
	excel.song(x,1,num)
excel.save("我是谁")

