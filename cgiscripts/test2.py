

fullname="cina"
email="ada"
comments="faf"
#print """stuff like %s, %s,  %s""", %s (fullname, email, comments)
#invalid syntax at 4th s


#print """stuff like %s, %s,  %s""" % (fullname, email, comments)
#this works


print """stuff like %s, %s,  %s""" , (fullname, email, comments)
