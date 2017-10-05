#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
db = MySQLdb.connect("localhost","root","","TCC" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# query to read from DB
dbQuery = 'SELECT * FROM Material;'
cursor.execute(dbQuery)
res = cursor.fetchall()

# writing to csv
csvFile = csv.writer(open("data.csv", "wb"))
for row in res:
	csvFile.writerow(row)

# disconnect from server
db.close()

