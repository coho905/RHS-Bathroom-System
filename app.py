from flask import Flask, request, render_template
import student
import mariadb
import time
import datetime
conn = mariadb.connect(user="riverbend", password="riverbend", host="161.35.112.169", port=3306, database="riverbend")
cursor = conn.cursor()
# Declare a Flask app
app = Flask(__name__)
#cursor.execute("CREATE TABLE people90(bathroom TINYINT)")


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # If a form is submitted
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0
    b6 = 0
    b7 = 0
    b8 = 0
    room = 0
    if request.method == "POST":

        # Unpickle classifier

        # Get values through input bars
        if 'b1' in request.form:
            user = request.form.get("username")
            passw = request.form.get("password")
            o = student.studentcreate(user, passw)
            print(1)
            room = int(student.whatBathroom(student.whatRoom(o), o))
            # Put inputs to dataframe
            print(1)
            print(type(room))
            if room == 1:
                print(1)
                if b1 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b1 = b1+1
                else:
                    print("too full")
            elif room == 2:
                if b2 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b2 = b2+1
                else:
                    print("too full")
            elif room == 3:
                if b3 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b3=b3+1
                else:
                    print("too full")
            elif room == 4:
                print(1)
                print(b4)
                if b4 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute('INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b4=b4+1
                else:
                    print("too full")
            elif room == 5:
                if b5 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b5=b5+1
                else:
                    print("too full")
            elif room == 6:
                if b6 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b6=b6+1

                else:
                    print("too full")
            elif room == 7:
                if b7 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                    b7=b7

                else:
                    print("too full")
            elif room == 8:
                if b8 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                else:
                    print("too full")
            elif room == -1:
                print(1)
                if b1 < 5:
                    prediction = int(room)
                    time1 = time.localtime()
                    current_time = time.strftime("%H:%M:%S", time1)
                    print(current_time)
                    cursor.execute(
                        'INSERT INTO bathroom VALUES ("{}", "{}", "{}")'.format(student.name(o), room, current_time))
                    cursor.execute("SELECT * from bathroom;")
                    results = cursor.fetchall()
                    print(results)
                else:
                    print("too full")
        elif "b2" in request.form:
            user = request.form.get("username")
            passw = request.form.get("password")
            o = student.studentcreate(user, passw)
            room = student.whatBathroom(student.whatRoom(o), o)
            # Put inputs to dataframe
            prediction = room
            cursor.execute('DELETE FROM bathroom WHERE name="{}";'.format(student.name(o)))
            cursor.execute("SELECT * from bathroom;")
            results = cursor.fetchall()
            print(results)

        message = "Hello, use bathroom # " + str(room)

    else:
        message = ""

    return render_template("website.html", msg = message)



app.run(debug=True)
