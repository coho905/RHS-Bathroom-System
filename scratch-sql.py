import mariadb
import datetime
import time
import student

conn = mariadb.connect(user="riverbend", password="********", host="35.245.195.219", port=3306, database="riverbend")
cursor = conn.cursor()
#cursor.execute("CREATE TABLE offical(bathroom TINYINT, name  CHAR(50), time CHAR(50))")


user = input()
passw = input()
o= student.studentcreate(user, passw)
name = student.name(o)
room1 = student.whatBathroom(student.whatRoom(o), o)
print(room1)
prediction = int(room1)
time1 = time.localtime()
current_time = time.strftime("%H:%M:%S", time1)
print(current_time)
cursor.execute('INSERT INTO offical VALUES ("{}", "{}", "{}")'.format(room1, name, current_time))
cursor.execute("SELECT * from offical;")
results = cursor.fetchall()
print(results)
