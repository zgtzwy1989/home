import sys,openpyxl,datetime
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QInputDialog,QMessageBox
class Demo (QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(70,70)
        self.main()
        self.new_excel.clicked.connect(self.new1)#创建新的数据表
        self.new.clicked.connect(self.new2)#写入新的数据
        self.old_read.clicked.connect(self.new3)#读取数据
        self.old_write.clicked.connect(self.new4)
    def main(self):
        self.new = QPushButton("新的数据", self)
        self.old_read = QPushButton("读取数据", self)
        self.new_excel = QPushButton("创建新的数据表", self)
        self.old_write = QPushButton("写入数据", self)
        self.one = QLabel("上一条数据", self)
        self.one_like = QLineEdit(self)
        self.write_data = QLabel("领取数值", self)
        self.write_data_like = QLineEdit(self)
        self.result = QLabel("结果", self)
        self.result_like = QLineEdit(self)
        self.result_bz = QLabel("领取人", self)
        self.result_bz_like = QLineEdit(self)

        # 列排序
        self.l1_px = QVBoxLayout()
        self.l1_px.addWidget(self.new)
        self.l1_px.addWidget(self.old_read)
        self.l1_px.addWidget(self.old_write)
        self.l1_px.addWidget(self.new_excel)
        # self.setLayout(self.l1_px)
        self.l2_px = QVBoxLayout()
        self.l2_px.addWidget(self.one)
        self.l2_px.addWidget(self.write_data)
        self.l2_px.addWidget(self.result)
        self.l2_px.addWidget(self.result_bz)
        # self.setLayout(self.l2_px)
        self.l3_px = QVBoxLayout()
        self.l3_px.addWidget(self.one_like)
        self.l3_px.addWidget(self.write_data_like)
        self.l3_px.addWidget(self.result_like)
        self.l3_px.addWidget(self.result_bz_like)
        # 行排序
        self.h1_px = QHBoxLayout()
        self.h1_px.addLayout(self.l1_px)
        self.h1_px.addLayout(self.l2_px)
        self.h1_px.addLayout(self.l3_px)
        self.setLayout(self.h1_px)
    def new1(self):
        print("111")
        wb = openpyxl.Workbook(r"登记表.xlsx")
        ws = wb.create_sheet(title="登记本", index=0)
        text = ["序号","时间","开始号", "领取数值", "结束号", "领取人","退回时间",'段号']
        ws.append(text)
        wb.save(r"登记表.xlsx")
        QMessageBox.information(self, "消息框标题", "创建初始数据完成。", QMessageBox.Yes | QMessageBox.No)
    def new2(self):
        value, ok = QInputDialog.getText(self, "提示", "请输入开始票据\n\n请输入文本:", QLineEdit.Normal, "这是默认值")
        wb = openpyxl.load_workbook(r'登记表.xlsx')
        ws = wb["登记本"]
        max_column = ws.max_row
        num=max_column+1
        print(max_column)
        value=value.rjust(9, '0')
        ws["c"+f"{num}"]=value
        wb.save(r'登记表.xlsx')
        QMessageBox.information(self, "消息框标题", "创建完成。", QMessageBox.Yes )
    def nwe3_1(self):
        if len(self.write_data_like.text()) !=0:
            num=int(self.i[0].value)+int(self.write_data_like.text())
            ss=str(num)
            self.result_new=(ss.rjust(9,'0'))
            self.result_like.setText(self.result_new)

        else:
            self.result_like.clear()

    def new3(self):
        self.result_like.clear()
        self.result_bz_like.clear()
        wb = openpyxl.load_workbook(r'登记表.xlsx')
        ws = wb["登记本"]
        max_column = ws.max_row
        for self.i in ws.iter_rows(min_row=max_column,min_col=3):
            self.one_like.setText(self.i[0].value)
        print(self.i[0].value,max_column)
        self.write_data_like.textChanged[str].connect(self.nwe3_1)
    def new4(self):
        '''
        a份数，b是结果 c领取人
        "序号","时间","开始号", "领取数值", "结束号", "领取人","退回时间",'段号'
        '''
        #a份数，b是结果 c领取人
        wb = openpyxl.load_workbook(r'登记表.xlsx')
        ws = wb["登记本"]
        max_column = ws.max_row
        a=self.write_data_like.text()
        b=self.result_like.text()
        c=self.result_bz_like.text()
        print(type(a),type(b),c)
        ws["d"+f"{max_column}"]=str(a)
        ws["e"+f"{max_column}"]=str(b)
        ws["f"+f"{max_column}"]=str(c)
        num=int(b)+1
        num=str(num).rjust(9,"0")
        ws["c"+f"{max_column+1}"]=str(num)
        #拼接短号
        text_new=ws["c" + f"{max_column}"].value + "-" + ws["e"+f"{max_column}"].value
        ws["h"+f'{max_column}']=str(text_new)
        #序号
        ws["a"+f'{max_column}']=int(max_column-1)
        #时间
        ws["b" + f'{max_column}']=str(datetime.date.today())
        wb.save(r'登记表.xlsx')
        wb.save(r'd:/登记表.xlsx')
        QMessageBox.information(self,"消息框标题","保存成功。",QMessageBox.Yes )
        self.result_like.clear()
        self.result_bz_like.clear()
        self.write_data_like.clear()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    tt=Demo()
    tt.show()
    app.exit(app.exec_())