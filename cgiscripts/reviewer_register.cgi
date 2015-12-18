#!/usr/bin/python2
# -*- coding: UTF-8 -*-



#This will take the comments and send it to the database
import mysql.connector
import web

from mysql.connector import Error
import cgi, cgitb

#chi and cgitb are for cgi handling
# app = web.application(urls, globals())

#need to check if others exist

conn = mysql.connector.connect(host='localhost', database='alicinamemar', user='root', password='')
cursor = conn.cursor()

if conn.is_connected():
    print('Connected to MySQL database')

 
# 
# form = cgi.FieldStorage()
# username = form.getvalue('username')
# password = form.getvalue('password')

username = "wow"
password = "sgaga"

check_existence = """
				SELECT username FROM `members` WHERE username='%s'
"""
cursor.execute(check_existence, (username))



#needs to check if user name exists
#needs to tell user if it exists
#if it doesnt exist, need to put it in db


sql = """
    INSERT INTO 
        members 
        (id, username, password) 
    VALUES 
        (NULL, %s, %s)
"""
cursor.execute(sql, ( username, password))


conn.commit()  
cursor.close()
conn.close()

