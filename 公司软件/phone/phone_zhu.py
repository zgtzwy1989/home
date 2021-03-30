import sys,openpyxl
from qtpy.QtWidgets import QLineEdit,QWidget,QVBoxLayout,QLabel,QStyle,QMessageBox,QHBoxLayout,QLayout,QPushButton,QApplication,QRadioButton
class wig(QWidget):
    def __init__(self):
        super(wig, self).__init__()
        self.resize(300,300)
        self.YS()
        self.off_button_settings()
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
        self.l10= QLabel("财务名字", self)
        self.edit10 = QLineEdit()
        self.l11 = QLabel("财务电话", self)
        self.edit11 = QLineEdit()
        self.l12 = QLabel("办税人姓名", self)
        self.edit12 = QLineEdit()
        self.l13 = QLabel("办税人电话", self)
        self.edit13 = QLineEdit()
        self.l14 = QLabel("办盘联系人", self)
        self.edit14 = QLineEdit()
        self.l15 = QLabel("办盘联系人电话", self)
        self.edit15 = QLineEdit()
        self.off_button = QRadioButton('已联系', self)  # 1
        self.la_ramark = QLabel("备注", self)
        self.edit_ramark = QLineEdit()
        self.la_datetime = QLabel("预约日期", self)
        self.edit_datetime = QLineEdit()
        self.butt1=QPushButton(text="按顺序显示")
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
        self.qv1.addWidget(self.l10)
        self.qv1.addWidget(self.l11)
        self.qv1.addWidget(self.l12)
        self.qv1.addWidget(self.l13)
        self.qv1.addWidget(self.l14)
        self.qv1.addWidget(self.l15)
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
        self.qv2.addWidget(self.edit10)
        self.qv2.addWidget(self.edit11)
        self.qv2.addWidget(self.edit12)
        self.qv2.addWidget(self.edit13)
        self.qv2.addWidget(self.edit14)
        self.qv2.addWidget(self.edit15)
        self.qh2=QHBoxLayout()
        self.qh2.addWidget(self.la_ramark)
        self.qh2.addWidget(self.edit_ramark)
        self.qh2.addWidget(self.la_datetime)
        self.qh2.addWidget(self.edit_datetime)
        self.qv3 = QVBoxLayout()
        self.qv3.addWidget(self.off_button)
        self.qv3.addLayout(self.qh2)
        self.qv3.addWidget(self.butt1)
        self.qv3.addWidget(self.butt2)
        self.qh1=QHBoxLayout()
        self.qh1.addLayout(self.qv1)
        self.qh1.addLayout(self.qv2)
        self.qh1.addLayout(self.qv3)
        self.setLayout(self.qh1)
        self.count=1
        self.butt1.clicked.connect(self.read_qt)
        self.butt2.clicked.connect(self.iter_qt)
    def off_button_settings(self):
        self.off_button.setChecked(False)
        self.edit_ramark.setEnabled(False)
        self.edit_datetime.setEnabled(False)
        self.off_button.toggled.connect(self.off_button_settings_edit)
    def off_button_settings_edit(self):
        print(self.off_button.isChecked())
        if self.off_button.isChecked():
            self.edit_ramark.setEnabled(True)
            self.edit_datetime.setEnabled(True)
        else:
            self.edit_ramark.setEnabled(False)
            self.edit_datetime.setEnabled(False)
    def excl(self):
        self.wb=openpyxl.load_workbook(r"d:\电话组催费数据-泰兴分.xlsx")
        self.sheet = self.wb.sheetnames
        self.look_sheet = self.wb[self.sheet[0]]
        self.max_row = self.look_sheet.max_row
    def read_qt(self):
        #name = self.edit1.text()
        self.count = 1
        for i in self.look_sheet.iter_rows(min_col=56,max_col=56):
            # print(self.count)
            # new=self.count
            if i[0].value==None:
                break
            self.count += 1
        for r in self.look_sheet.iter_rows(min_row=self.count,max_row=self.count):
            print(r[1].value)
            #print(i[1].value,i[2].value,i[4].value,i[5].value,i[10].value,i[39].value,i[41].value,i[41].value,i[41].value)
            self.edit1.clear()
            self.edit2.clear()
            self.edit3.clear()
            self.edit4.clear()
            self.edit5.clear()
            self.edit6.clear()
            self.edit7.clear()
            self.edit8.clear()
            self.edit9.clear()
            self.edit10.clear()
            self.edit11.clear()
            self.edit12.clear()
            self.edit13.clear()
            self.edit14.clear()
            self.edit15.clear()
            self.edit1.setText(f"{r[1].value}")
            self.edit2.setText(f"{r[2].value}")
            self.edit3.setText(f"{r[4].value}")
            self.edit4.setText(f"{r[5].value}")
            self.edit5.setText(f"{r[10].value}")
            self.edit6.setText(f"{r[38].value}")
            self.edit7.setText(f"{r[39].value}")
            self.edit8.setText(f"{r[41].value}")
            self.edit9.setText(f"{r[54].value}")
            self.edit10.setText(f"{r[42].value}")
            self.edit11.setText(f"{r[44].value}")
            self.edit12.setText(f"{r[45].value}")
            self.edit13.setText(f"{r[47].value}")
            self.edit14.setText(f"{r[49].value}")
            self.edit15.setText(f"{r[51].value}")
    def iter_qt(self):
        print(type(self.edit_ramark.text()),self.edit_datetime.text())
        new=self.count
        print(new)
        self.look_sheet[f"BD{new}"]="已联系"
        if len(self.edit_ramark.text()) == 0:
            pass
        else:
            self.look_sheet[f"BE{new}"] =f"{self.edit_ramark.text()}"
            self.edit_ramark.clear()
        if len(self.edit_datetime.text()) == 0:
            pass
        else:
            self.look_sheet[f"BF{new}"] = f"{self.edit_datetime.text()}"
            self.edit_datetime.clear()
        self.off_button_settings()
        print("1")
        if self.count==1:
            QMessageBox.information(self, '通知', '本单位已录入')
        self.count = 1
        self.wb.save(r"e:\电话组催费数据-泰兴分.xlsx")
        self.wb.save(r"d:\电话组催费数据-泰兴分_备份.xlsx")
        QMessageBox.information(self, '通知', '已录入完成')
        print("wang")
if __name__ =="__main__":
    app=QApplication(sys.argv)#argv是一个列表，所以上面的参数按顺序
    demo=wig()
    demo.show()
    sys.exit(app.exec())






