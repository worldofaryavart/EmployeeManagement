import mysql.connector as a
legend=a.connect(host="localhost",
                 user="root",
                 passwd="247231",
                 database="employee")
sql="""CREATE TABLE PERSONAL
(Name VARCHAR(10),
City VARCHAR(30),
Birthdate VARCHAR(20),
Phone VARCHAR(15))"""
c=legend.cursor()
c.execute(sql)
