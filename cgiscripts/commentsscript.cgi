#!/usr/bin/python2



#^THat path made it work
print("Content-Type: text/html\n\n")  # html markup follows


#it prints html
# but it won't send db
#will execute by bash but not through the server in anyway



#This will take the comments and send it to the database
import mysql.connector
import web

from mysql.connector import Error
import cgi
import cgitb

#chi and cgitb are for cgi handling
# app = web.application(urls, globals())

cgitb.enable()



conn = mysql.connector.connect(host='localhost', database='alicinamemar', user='root', password='root')
cursor = conn.cursor()





# fullname = "no it really works tho"
# email ="emdhail"
# comments = "comdhments"


form = cgi.FieldStorage()
fullname = form.getvalue('fullname')
email = form.getvalue('email')
comments = form.getvalue('comments')
# ^header error can be from this

sql = """
    INSERT INTO 
        comments 
        (id, name, email, comments, time) 
    VALUES 
        (NULL, %s, %s, %s, CURRENT_TIMESTAMP)
"""
cursor.execute(sql, (fullname, email, comments))
conn.commit()  


print("""
<!DOCTYPE html>
<head>
 <title>Comment Submission Status</title>
    <link rel='stylesheet' type='text/css' href='../main.css'>
    <link rel='stylesheet' href='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>
    	<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js'></script>

""")
print("""
	<!-- Latest compiled JavaScript -->
	<script src='http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js'></script>
</head>
<body>
""")

print("""
      
     
<div class='outcontainer'>

<div class='container-fluid'>
<div class='row'>
<div class='col-xs-12'>
	<div class='headercus hidden-xs'>
		 <h2 class='center lightblue_text'>World Congress<small class='lightblue_text'>  CS-IT Conferences</small></h2>
		<nav class='navbar navbar-default'>
		<ul class='nav nav-pills main_menu'>
	
			<li role='presentation'>
				<a href='../html/../index.html' class='nav-brand'>
				<img class='home_icon' alt='Brand' title='Home' src='http://2.bp.blogspot.com/-s8V9Gc7WBpc/U3Hbfxz_GvI/AAAAAAAACns/CN1NRR-Q8P4/s1600/App+terminal.png' /> </a>
			</li>
			
			<!-- credit for icon: http://www.beopensource.com/2014/05/keyboard-shortcuts-within-terminal.html -->
	
			<li role='presentation'>
				<a href='../html/dates.html' >Dates</a></li>
			
			<li role='presentation' class='dropdown'>	
			<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button' aria-haspopup='true' aria-expanded='false'>Conference Information<span class='caret'></span></a> 	
				<ul class='dropdown-menu'>
					<li><a href='../html/about_conf.html'><span class='nested_text'>About the Conference</span></a></li>
					<li><a href='../html/fee.html'><span class='nested_text'>Conference Fee</span></a></li>
					<li><a href='../html/hotel_info.html'><span class='nested_text'>Hotel Information</span></a></li>
					<li><a href='../html/conf_register.html'><span class='nested_text'>Conference Registration</span></a></li>
					<li><a href='../html/program.html'><span class='nested_text'>Conference Program</span></a></li>
					<li><a href='../html/guidelines.html'><span class='nested_text'>Guidelines</span></a></li>
					<li><a href='../html/keynote.html'><span class='nested_text'>Keynote Speakers</span></a></li>
					<li><a href='../html/call.html'><span class='nested_text'>Call for Paper</span></a></li>
					<li><a href='../html/major.html'><span class='nested_text'>Major Areas</span></a></li>
	
				</ul>
			</li>
			
			<li role='presentation'>
				<a href='../html/comments.html' role='button'>Comments</a>
	
			</li>
			<li role='presentation' class='dropdown'>
				<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button'>Reviewer<span class='caret'></span></a>
				<ul class='dropdown-menu'>
					<li><a href='../html/reviewer_login.html' id='reviewerlog_link_wide'> <span class='nested_text' id='reviewerlog_text_wide'>Login</span></a></li>
					<li><a href='../html/reviewer_reg.html' > <span class='nested_text'>Registration</span></a></li>
					<li><a href='../html/submitpaper.html'> <span class='nested_text'>Submit Paper</span></a></li>
				</ul>
			</li>
			
			<li role='presentation' class='dropdown'>
				<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button'>Administration<span class='caret'></span></a>
				<ul class='dropdown-menu'>
					<li><a href='../html/admin_login.html' id='adminlog_link_wide'> <span class='nested_text' id='adminlog_text_wide'>Login</span></a></li>
					<li><a href='../html/admin_manage.html'> <span class='nested_text'>Management</span></a></li>
				</ul>
			</li>
			
		</ul>
	</nav>
		
	</div>	
		
<!--horizontal version		-->
	<div class='headercus visible-xs'>
	<h2 class='center lightblue_text'>World Congress<small class='lightblue_text'>  CS-IT Conferences</small></h2>

	<nav class='navbar navbar-default'>
	<ul class='nav nav-pills nav-stacked main_menu_mob'>

		<li role='presentation'>
			<a href='../html/../index.html' class='nav-brand'>
			<img class='home_icon' alt='Brand' title='Home' src='http://2.bp.blogspot.com/-s8V9Gc7WBpc/U3Hbfxz_GvI/AAAAAAAACns/CN1NRR-Q8P4/s1600/App+terminal.png' /> </a>
		</li>
		
		<!-- credit for icon: http://www.beopensource.com/2014/05/keyboard-shortcuts-within-terminal.html -->

		<li role='presentation'>
			<a href='../html/dates.html' >Dates</a></li>
		
		<li role='presentation' class='dropdown'>	
		<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button' aria-haspopup='true' aria-expanded='false'>Conference Information<span class='caret'></span></a> 	
			<ul class='dropdown-menu'>
				<li><a href='../html/about_conf.html'><span class='nested_text'>About the Conference</span></a></li>
				<li><a href='../html/fee.html'><span class='nested_text'>Conference Fee</span></a></li>
				<li><a href='../html/hotel_info.html'><span class='nested_text'>Hotel Information</span></a></li>
				<li><a href='../html/conf_register.html'><span class='nested_text'>Conference Registration</span></a></li>
				<li><a href='../html/program.html'><span class='nested_text'>Conference Program</span></a></li>
				<li><a href='../html/guidelines.html'><span class='nested_text'>Guidelines</span></a></li>
				<li><a href='../html/keynote.html'><span class='nested_text'>Keynote Speakers</span></a></li>
				<li><a href='../html/call.html'><span class='nested_text'>Call for Paper</span></a></li>
				<li><a href='../html/major.html'><span class='nested_text'>Major Areas</span></a></li>

			</ul>
		</li>
		
		<li role='presentation'>
			<a href='../html/comments.html' role='button'>Comments</a>

		</li>
		<li role='presentation' class='dropdown'>
			<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button'>Reviewer<span class='caret'></span></a>
			<ul class='dropdown-menu'>
				<li><a href='../html/reviewer_login.html' id='reviewerlog_link_mob'> <span class='nested_text' id='reviewerlog_text_mob'>Login</span></a></li>
				<li><a href='../html/reviewer_reg.html' > <span class='nested_text'>Registration</span></a></li>
				<li><a href='../html/submitpaper.html'> <span class='nested_text'>Submit Paper</span></a></li>
			</ul>
		</li>
		
		<li role='presentation' class='dropdown'>
			<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button'>Administration<span class='caret'></span></a>
			<ul class='dropdown-menu'>
				<li><a href='../html/admin_login.html' id='adminlog_link_mob'> <span class='nested_text' id='adminlog_text_mob'>Login</span></a></li>
				<li><a href='../html/admin_manage.html'> <span class='nested_text'>Management</span></a></li>
			</ul>
		</li>
		
	</ul>
	</nav>
	</div>


""")
if conn.is_connected():
    print("""
    <h1 class="page-header">Comment submitted.</h1>
     <p> <button><a href="../html/comments.html">here</a></button></p>
    
    
    </div>
    </div>
    </div>
    </div>
    </body>
    </html>
    """)
else:
    print("""
    <h1 class="page-header">Database error, <b>comment was not submitted.</b></h1>
     <p>If you are not redirected, click <button><a href="../html/comments.html">here</a></button></p>
    
    
    </div>
    </div>
    </div>
    </div>
    </body>
    """)
cursor.close()
conn.close()

print('''Status: 303 See Other
Location: ../html/comments.html
Pragma: no-cache
Content-Type: text/html
''')


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
