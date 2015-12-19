 #!/usr/bin/env python
 # -*- coding: UTF-8 -*-
# print "Content-Type: text/plain;charset=utf-8"


#This will take the comments and send it to the database
import mysql.connector
import web

from mysql.connector import Error
import cgi, cgitb

#chi and cgitb are for cgi handling
# app = web.application(urls, globals())

cgit.enable()

conn = mysql.connector.connect(host='localhost', database='alicinamemar', user='root', password='root')
cursor = conn.cursor()

if conn.is_connected():
    print('Connected to MySQL database')



# fullname = "this works"
# email ="emdhail"
# comments = "comdhments"


form = cgi.FieldStorage()
#fullname = form.getvalue('fullname')
person_title = form.getvalue('person_title')
firstname = form.getvalue('lastname')
lastname = form.getvalue('lastname')
organization = form.getvalue('organization')
address = form.getvalue('address')
telephone = form.getvalue('telephone')
email = form.getvalue('email')
attendeetype = form.getvalue('attendeetype')
# ^header error can be from this

#sql = """
#    INSERT INTO 
#        comments 
#        (id, name, email, comments, time) 
#    VALUES 
#        (NULL, %s, %s, %s, CURRENT_TIMESTAMP)
#"""
#cursor.execute(sql, (fullname, email, comments))
sql = """
    INSERT INTO
        registrationlist
        (`id`, `title`, `firstname`, `lastname`, `org`, `address`, `telephone`, `email`, `attendeetype`, `timestamp`)
    VALUES
        (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', CURRENT_TIMESTAMP);
"""

cursor.execute(sql, (person_title, firstname, lastname, organization, address, telephone, email, attendeetype))

conn.commit()  
cursor.close()
conn.close()

# sql = """INSERT INTO `comments` (`id`, `name`, `email`, `comments`, `time`) VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP)""" % (fullname, email, comments)
# # the syntax of the passing is correct  for inserting a table, so why wont this work




#sql = """INSERT INTO `comments` (`id`, `name`, `email`, `comments`, `time`) VALUES (NULL, fullname, email, comments, CURRENT_TIMESTAMP)"""

# Traceback (most recent call last):
#   File "/opt/lampp/htdocs/conferencerewrite/cgiscripts/commentsscript.cgi", line 50, in <module>
#     if cursor.execute(sql):
#   File "/usr/lib/python2.7/dist-packages/mysql/connector/cursor.py", line 494, in execute
#     self._handle_result(self._connection.cmd_query(stmt))
#   File "/usr/lib/python2.7/dist-packages/mysql/connector/connection.py", line 683, in cmd_query
#     statement))
#   File "/usr/lib/python2.7/dist-packages/mysql/connector/connection.py", line 601, in _handle_result
#     raise errors.get_exception(packet)
# mysql.connector.errors.ProgrammingError: 1054 (42S22): Unknown column 'fullname' in 'field list'

#python doesn't pass variables inside strings by name





#sql = """INSERT INTO `comments` (`id`, `name`, `email`, `comments`, `time`) VALUES (NULL, "fullname", "email", "comments", CURRENT_TIMESTAMP)"""
#^this one works
#it won't take the variables, even when they are strings outside of the code. the question if they'll do my html variables

#TWO Errors
#the server
#passsing

#sql = """CREATE TABLE anooog1 (COL1 INT, COL2 INT )"""
#this ^ works

#sql = """CREATE TABLE %s (COL1 INT, COL2 INT )""" % ("anooog1") 
#this works

#sql = """CREATE TABLE ? (COL1 INT, COL2 INT )""" % (anooog1) 
#this causes an error

#anooog1 = "thing"
#sql = """CREATE TABLE %s (COL1 INT, COL2 INT )""" % (anooog1) 
#this works too


# anooog1 = "thing"
# sql = """CREATE TABLE thiga (%s INT, COL2 INT )""" % (anooog1) 
# this works too

#cursor.execute(sql)

#cursor.execute("""INSERT INTO `comments` (`id`, `name`, `email`, `comments`, `time`) VALUES (NULL, %s, %s, %s, CURRENT_TIMESTAMP)""" % (fullname, email, comments))
#This causes an error too, 


#Commit must be called

#the script is running and it inserted the table before

# if __name__ == "__main__":
#     app.run()
