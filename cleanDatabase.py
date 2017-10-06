#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","TCC" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# clean the entire table Material
dbQuery = "DELETE FROM Material;"
cursor.execute(dbQuery)

# closing database connection
db.commit()
db.close()
