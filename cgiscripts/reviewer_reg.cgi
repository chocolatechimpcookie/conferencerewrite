#!/usr/bin/python2
# -*- coding: UTF-8 -*-
print("Content-Type: text/html\n\n")  # html markup follows



#This will take the comments and send it to the database
import mysql.connector
import web

from mysql.connector import Error
import cgi, cgitb


cgitb.enable()


#work to be done
# 2) strip sql and html






print("""
<!DOCTYPE html>
<head>
 <title>Reviewer Registration</title>
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
					<li><a href='reviewer_login.cgi' id='reviewerlog_link_wide'> <span class='nested_text' id='reviewerlog_text_wide'>Login</span></a></li>
					<li><a href='../html/reviewer_reg.html' > <span class='nested_text'>Registration</span></a></li>
					<li><a href='submitpaper.cgi'> <span class='nested_text'>Submit Paper</span></a></li>
				</ul>
			</li>
			
			<li role='presentation' class='dropdown'>
				<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button'>Administration<span class='caret'></span></a>
				<ul class='dropdown-menu'>
					<li><a href='admin_login.cgi' id='adminlog_link_wide'> <span class='nested_text' id='adminlog_text_wide'>Login</span></a></li>
					<li><a href="admin_manage.cgi"> <span class='nested_text'>Management</span></a></li>
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
				<li><a href='reviewer_login.cgi' id='reviewerlog_link_mob'> <span class='nested_text' id='reviewerlog_text_mob'>Login</span></a></li>
				<li><a href='../html/reviewer_reg.html' > <span class='nested_text'>Registration</span></a></li>
				<li><a href='submitpaper.cgi'> <span class='nested_text'>Submit Paper</span></a></li>
			</ul>
		</li>
		
		<li role='presentation' class='dropdown'>
			<a class='dropdown-toggle' data-toggle='dropdown' href='#' role='button'>Administration<span class='caret'></span></a>
			<ul class='dropdown-menu'>
				<li><a href='admin_login.cgi' id='adminlog_link_mob'> <span class='nested_text' id='adminlog_text_mob'>Login</span></a></li>
				<li><a href="admin_manage.cgi"> <span class='nested_text'>Management</span></a></li>
			</ul>
		</li>
		
	</ul>
	</nav>
	</div>


""")


#   weird syntax   
# 
# cursor.execute(check_existence, username)
#    =>  483                     "Wrong number of arguments during string formatting")
# cursor.execute(check_existence, (username))
#   ^pushes down to con.commit


#  says cursor.rowcount is not callible
# matches = cursor.rowcount
#why is row count = -1
# if not(cursor.fetchall()):
#     print "Empty"           >> Create user
# else:
#     print "something inside" >>dont create user


#Also note, checking if con.is_connected after  cursor.execute messes it up for some reason, it returns false but it'll still send data to mysql


conn = mysql.connector.connect(host='localhost', database='alicinamemar', user='root', password='root')
if conn.is_connected():
    cursor = conn.cursor()
    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    
    check_existence = """
        SELECT username FROM members WHERE username = %s
    """

    cursor.execute(check_existence, (username,))

    if not(cursor.fetchall()):
        sql = """
        INSERT INTO 
            members 
            (id, username, password) 
        VALUES 
            (NULL, %s, %s)
        """
        cursor.execute(sql, (username, password))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        print("""
        <h1 class="page-header"><b>Registration was completed.</b></h1>
         <p><button><a href="../html/reviewer_reg.html">Click to redirect.</a></button></p>
         
        </div>
        </div>
        </div>
        </div>
        </body>
        """)        
    else:
        print("""
        <h1 class="page-header">That username has already been chosen: <b>registration was not completed.</b></h1>
         <p><button><a href="../html/reviewer_reg">Click here to redirect.</a></button></p>
        
        
        </div>
        </div>
        </div>
        </div>
        </body>
        """)

        cursor.close()
        conn.close()
else:
    print("""
    <h1 class="page-header">Database error, <b>registration was not completed.</b></h1>
     <p><button><a href="../html/reviewer_reg.html">Click here to redirect</a></button></p>
    
    
    </div>
    </div>
    </div>
    </div>
    </body>
    """)
