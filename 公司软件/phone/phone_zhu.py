import qtpy.QtWidgets,sys,openpyxl,re
from qtpy.QtWidgets import QLineEdit,QWidget,QVBoxLayout,QLabel,QStyle,QMessageBox,QHBoxLayout,QLayout,QPushButton,QApplication
class wig(QWidget):
    def __init__(self):
        super(wig, self).__init__()
        self.resize(300,300)
        self.YS()
        self.excl()

        
    def YS(self):
        self.l1=QLabel("单位名称",self)
        self.edit1=QLineEdit()
        self.l2 = QLabel("欠费金额", self)
        self.edit2 = QLineEdit()
        self.l3 = QLabel("催款状态", self)
        self.edit3 = QLineEdit()
        self.l4 = QLabel("催款备注", self)
        self.edit4 = QLineEdit()
        self.l5 = QLabel("到期日期", self)
        self.edit5 = QLineEdit()
        self.l6=QLabel("生产经营电话", self)
        self.edit6 = QLineEdit()
        self.l7 = QLabel("法人名字", self)
        self.edit7 = QLineEdit()
        self.l8 = QLabel("法人电话", self)
        self.edit8 = QLineEdit()
        self.l9 = QLabel("发票电话", self)
        self.edit9 = QLineEdit()
        self.butt1=QPushButton(text="确认")
        self.butt2 = QPushButton(text="录入")
        self.qv1=QVBoxLayout()
        self.qv1.addWidget(self.l1)
        self.qv1.addWidget(self.l2)
        self.qv1.addWidget(self.l3)
        self.qv1.addWidget(self.l4)
        self.qv1.addWidget(self.l5)
        self.qv1.addWidget(self.l6)
        self.qv1.addWidget(self.l7)
        self.qv1.addWidget(self.l8)
        self.qv1.addWidget(self.l9)
        self.qv2 = QVBoxLayout()
        self.qv2.addWidget(self.edit1)
        self.qv2.addWidget(self.edit2)
        self.qv2.addWidget(self.edit3)
        self.qv2.addWidget(self.edit4)
        self.qv2.addWidget(self.edit5)
        self.qv2.addWidget(self.edit6)
        self.qv2.addWidget(self.edit7)
        self.qv2.addWidget(self.edit8)
        self.qv2.addWidget(self.edit9)
        self.qv3 = QVBoxLayout()
        self.qv3.addWidget(self.butt1)
        self.qv3.addWidget(self.butt2)
        self.qh1=QHBoxLayout()
        self.qh1.addLayout(self.qv1)
        self.qh1.addLayout(self.qv2)
        self.qh1.addLayout(self.qv3)
        self.setLayout(self.qh1)
        
        self.butt1.clicked.connect(self.read_qt)
        self.butt2.clicked.connect(self.iter_qt)
    def inser_excl(self):
        self.inser_wb=openpyxl.load_workbook(r"D:\催费log\催费.xlsx")
        self.sheet = self.wb.sheetnames
        self.look_sheet = self.wb[self.sheet[0]]



    def excl(self):
        self.wb=openpyxl.load_workbook(r"d:\电话组催费数据-泰兴分.xlsx")
        self.sheet = self.wb.sheetnames
        self.look_sheet = self.wb[self.sheet[0]]

        self.max_row=self.look_sheet.max_row
    def read_qt(self):
        name = self.edit1.text()
        #print(name)
        for i in self.look_sheet.iter_rows(min_row=3,max_row=self.max_row):
            print(i[1].value,name)
            if i[1].value==name:
                print(i[1].value)
                print(i[1].value,i[2].value,i[4].value,i[5].value,i[10].value,i[39].value,i[41].value,i[41].value,i[41].value)
                self.edit2.setText(f"{i[2].value}")
                self.edit3.setText(f"{i[4].value}")
                self.edit4.setText(f"{i[5].value}")
                self.edit5.setText(f"{i[10].value}")
                self.edit6.setText(f"{i[38].value}")
                self.edit7.setText(f"{i[39].value}")
                self.edit8.setText(f"{i[41].value}")
                self.edit9.setText(f"{i[50].value}")



    def iter_qt(self):

        qqq=self.edit2.text()
        name = self.edit1.text()
        print(type(qqq),name)
        for i in self.look_sheet.iter_rows(min_row=2, max_row=self.max_row):
            if i[0].value == name:
                print(i[0].value)
                sss=i[1]
                print(sss)
                num_row=re.search(r"<Cell 'Sheet1'.B(.*?)>",sss).group(1)
                print(num_row)
                self.look_sheet[f"{num_row}"]=qqq
                print("lalalaaaa")
                self.wb.save()
                print("w")
if __name__ =="__main__":
    app=QApplication(sys.argv)#argv是一个列表，所以上面的参数按顺序
    demo=wig()
    demo.show()
    sys.exit(app.exec())






