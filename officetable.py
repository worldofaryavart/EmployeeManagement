import mysql.connector as a
legend=a.connect(host="localhost",
                 user="root",
                 passwd="247231",
                 database="employee")
sql="""CREATE TABLE OFFICE
(Ecode VARCHAR(10),
Name VARCHAR(30),
Post VARCHAR(20),
Joining VARCHAR(10),
BasicPay integer)"""
c=legend.cursor()
c.execute(sql)
