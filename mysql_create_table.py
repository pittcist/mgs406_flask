import mysql.connector as sql

mydb = sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db")
cur = mydb.cursor()

cmd = "CREATE TABLE students (\
    sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    name VARCHAR(30) NOT NULL,\
    addr VARCHAR(30), \
    city VARCHAR(30), \
    zip VARCHAR(30))"

cur.execute(cmd)
mydb.close()



