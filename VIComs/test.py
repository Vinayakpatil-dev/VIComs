import mysql.connector
from flask import request
connection=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Abijith",
    database="vicoms"
)
cursor=connection.cursor()
regid=request.form["regid"]
pwd=request.form["pwd"]
cursor=connection.cursor()
cursor.execute("select * from employee ;")
em=cursor.fetchall()
lem=[]
for i in em:
    s=[]
    for j in i:
        s.append(j)
        lem.append(s)
    kv_pairs = {}
for row in lem:
    kv_pairs[row[0]] = row[5]