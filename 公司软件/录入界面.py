import sys,pymysql
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMessageBox
class Demo (QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(400,400)
        self.setWindowTitle("录入系统")
        self.ql_tsbq=QLabel("今天电话数",self)#标签数
        self.ql_sh=QLabel("企业税号",self)#税号
        self.ql_zw=QLabel("职位",self)#职位
        self.ql_phone=QLabel("电话",self)#电话
        self.ql_content=QLabel("内容",self)#内容
        self.ql_sh_edit=QLineEdit(self)
        self.ql_zw_edit = QLineEdit(self)
        self.ql_phone_edit = QLineEdit(self)
        self.ql_content_edit = QLineEdit(self)
        self.qr_button=QPushButton("确认",self)
        self.qc_button = QPushButton("清除",self)

#标题方框横向排序：
        self.v1=QHBoxLayout()#税号
        self.v1.addWidget(self.ql_sh)
        self.v1.addWidget(self.ql_sh_edit)
        self.v2 = QHBoxLayout()
        self.v2.addWidget(self.ql_zw)
        self.v2.addWidget(self.ql_zw_edit)
        self.v3 = QHBoxLayout()
        self.v3.addWidget(self.ql_phone)
        self.v3.addWidget(self.ql_phone_edit)
        self.v4 = QHBoxLayout()
        self.v4.addWidget(self.ql_content)
        self.v4.addWidget(self.ql_content_edit)
# 按钮横向排序h2
        self.h2 = QHBoxLayout()
        self.h2.addWidget(self.qr_button)
        self.h2.addWidget(self.qc_button)
#所有项目纵向排列
        self.zv1=QVBoxLayout()
        self.zv1.addLayout(self.v1)
        self.zv1.addLayout(self.v2)
        self.zv1.addLayout(self.v3)
        self.zv1.addLayout(self.v4)
        self.zv1.addLayout(self.h2)
        self.setLayout(self.zv1)
        self.qr_button.clicked.connect(self.inster)
        self.qc_button.clicked.connect(self.clear)
    def i(self,sql):
        ws = pymysql.connect(host="localhost", passwd="cq123456", user="root", port=3306, db="业务")
        wb = ws.cursor()
        wb.execute(sql)
        ws.commit()
        ws.close()

    def inster(self):
        sh=self.ql_sh_edit.text()
        zw=self.ql_zw_edit.text()
        phone=self.ql_phone_edit.text()
        nr=self.ql_content_edit.text()
        
        sql=f"insert into 电话联系表(`税号`,联系人,`电话`,content)value('{sh}','{zw}','{phone}','{nr}')"
        print(sql)
        self.i(sql)
        QMessageBox.information(self, "消息框标题", "保存成功。", QMessageBox.Yes)
        self.ql_zw_edit.clear()
        self.ql_phone_edit.clear()
        self.ql_content_edit.clear()
    def clear(self):
        self.ql_sh_edit.clear()
        self.ql_zw_edit.clear()
        self.ql_phone_edit.clear()
        self.ql_content_edit.clear()











if __name__ == '__main__':
    app=QApplication(sys.argv)
    TT=Demo()
    TT.show()
    app.exit(app.exec_())