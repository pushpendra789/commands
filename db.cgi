#!/usr/bin/python2
import cgi
import cgitb
import commands
import mysql.connector 

connection = mysql.connector.connect(host='localhost',database='adhoc',user='root',password='redhat')
cur = connection.cursor()
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

email = data.getvalue("cmd1")
print(email)
print "<br/>"

username = data.getvalue("cmd2")
print(username)
print "<br/>"

password = data.getvalue("cmd3")
print(password)
print "<br/>"

repassword = data.getvalue("cmd4")
print(password)
print "<br/>"




cur.execute("INSERT INTO dockers(email,username,password,repassword) VALUES(%s,%s,%s,%s)", (email,username,password,repassword))
connection.commit()
#fetching  database
cur.execute("select *   from dockers")
print  cur.fetchall()
connection.close()
