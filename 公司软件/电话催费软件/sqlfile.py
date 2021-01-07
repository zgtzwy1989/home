import pymysql
class htxx_sql():
    def __init__(self):
        self.new_sql=pymysql.connect(host="localhost",passwd="cq123456",user="root",db="业务",port=3306)
        self.bd=self.new_sql.cursor()
    def sql_insert(self,sql):
        self.bd.execute(sql)
        self.new_sql.commit()
        self.new_sql.close()
