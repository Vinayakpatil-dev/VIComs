from flask import Flask,request,render_template,url_for,redirect
import mysql.connector
from mysql.connector import Error
import smtplib
connection=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Abijith",
    database="vicoms"
    )
cursor=connection.cursor()
app=Flask(__name__)
@app.route('/')
def home_render():
    return render_template("home.html")
@app.route("/employee")
def employee_render():
    return render_template("emp_login.html")
@app.route("/employee",methods=['post'])
def employee():
    regid=request.form["regid"]
    pwd=request.form["pwd"]
    cursor=connection.cursor()
    cursor.execute("select * from employee ;")
    em=cursor.fetchall()
    lem=[]
    users=[]
    for i in em:
        s=[]
        for j in i:
            s.append(j)
        lem.append(s)
    kv_pairs = {}
    for row in lem:
        kv_pairs[row[0]] = row[2]
    for i,j in kv_pairs.items():
        users.append(i)
    if regid in users:
        if kv_pairs[regid]==pwd:
            if 'bkt' in regid:
                return redirect(url_for("employee_cleaning_render"))
            else:
                return render_template("employee_maintaning.html")
        else:
            return "user not found"
    else:
        return "user not found"
@app.route("/employee_cleaning")
def employee_cleaning_render():
    return render_template("employee_cleaner.html")
@app.route("/employee_maintaning")
def employee_maintaning_render():
    return render_template("employee_maintaning.html")

@app.route("/student_page")
def student_render():
    return render_template("login.html")
@app.route("/student_page",methods=['post'])
def student():
    regid=request.form["regid"]
    pwd=request.form["pwd"]
    cursor=connection.cursor()
    cursor.execute(f"select * from students")
    em=cursor.fetchall()
    lem=[]
    users=[]
    for i in em:
        s=[]
        for j in i:
            s.append(j)
        lem.append(s)
    kv_pairs = {}
    for row in lem:
        kv_pairs[row[1]] = row[5]
    for i,j in kv_pairs.items():
        users.append(i)
    if regid in users:
        if kv_pairs[regid]==pwd:
            return render_template ("Main_Page.html")
        else:
            return "incorrect password or username"
    else:
        return "user no found "
@app.route("/main_page")
def main_page():
    return render_template("Main_Page.html")

@app.route("/maintance")
def maintance_render():
    return render_template("maintenance.html")
@app.route("/maintance",methods=['post'])
def maintance():
    name=request.form['name']
    h_block=request.form['block']
    room_no=request.form['room']
    Maintenace_Type=request.form['type']
    cursor.execute(f"insert maintenance values('{name}','{Maintenace_Type}',{room_no},'{h_block}')")
    connection.commit()
    return render_template("Main_Page.html")

@app.route("/room_cleaning")
def room_cleaning_render():
    return render_template("room.html")
@app.route("/room_cleaning",methods=['post'])
def room():
    name=request.form['name']
    h_block=request.form['block']
    room_no=request.form['room']
    slot=request.form['slot']
    cursor.execute(f"insert room_cleaning values('{name}','{slot}',{room_no},'{h_block}')")
    connection.commit()
    return render_template("Main_Page.html")

@app.route("/complaint")
def complain_render():
    return render_template("complaint.html")
@app.route("/complaint",methods=['post'])
def complain():
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("abijith0707@gmail.com","mnng flvn wdqk ierl")
    message=request.form['content']
    s.sendmail("abijith0707@gmail.com","dummymail1616@gmail.com",message)
    s.quit()
    return render_template("Main_Page.html")
@app.route("/sign_up")
def sign_up_render():
    return render_template("signup.html")
@app.route("/sign_up",methods=['post'])
def sign_up():
    try:
        cursor=connection.cursor()
        regid=request.form['regid']
        name=request.form['name']
        block=request.form['block']
        room=request.form['room']
        mail=request.form['mail']
        pwd=request.form['pwd']
        cursor=connection.cursor()
        cursor.execute(f"insert students values ('{name}','{regid}','{mail}','{block}',{room},'{pwd}')")
        connection.commit()
        return render_template("login.html")
    except mysql.connector.errors.IntegrityError:
        return "user exist"
if __name__=="__main__":
    app.run(debug=True)