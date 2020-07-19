import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', 
            passwd='cq123456', db='农行业务', charset='utf8')
con=conn.cursor()
que=con.execute("select * from 工作表")
que=que.fetchone()
print(data)