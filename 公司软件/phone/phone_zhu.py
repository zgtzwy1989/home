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
        self.l2 = QLabel("税号", self)
        self.edit2 = QLineEdit()
        self.butt1=QPushButton(text="确认")
        self.butt2 = QPushButton(text="录入")
        self.qv1=QVBoxLayout()
        self.qv1.addWidget(self.l1)
        self.qv1.addWidget(self.l2)
        self.qv2 = QVBoxLayout()
        self.qv2.addWidget(self.edit1)
        self.qv2.addWidget(self.edit2)
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


    def excl(self):
        self.wb=openpyxl.load_workbook("E:\实验.xlsx")
        self.sheet = self.wb.sheetnames
        self.look_sheet = self.wb[self.sheet[0]]
        self.max_row=self.look_sheet.max_row
    def read_qt(self):
        name = self.edit1.text()
        print(name)
        for i in self.look_sheet.iter_rows(min_row=2,max_row=self.max_row):
            if i[0].value==name:
                print(i[0].value)
                self.edit2.setText(f"{i[1].value}")
                print(i[1].value)
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

                # self.look_sheet[f"{mac}"]=qqq
                # print("lalalaaaa")
                # self.wb.save()
                # print("w")
if __name__ =="__main__":
    app=QApplication(sys.argv)#argv是一个列表，所以上面的参数按顺序
    demo=wig()
    demo.show()
    sys.exit(app.exec())






