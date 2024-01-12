import pymysql as mq
myobj=mq.connect("localhost","root","")
cursorobj=myobj.cursor()
try:
db="create database haseeb"
cursorobj.execute(db)
print("Database Created")
except:
print("Database Error")
