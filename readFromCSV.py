#!/usr/bin/python

import MySQLdb
import csv

# Open database connection
db = MySQLdb.connect("localhost","root","","TCC" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# reading from csv
csvData = csv.reader(file('data.csv'))

# inserting in the database
for row in csvData:
	cursor.execute('INSERT INTO Material( \
			id, type, author, year, \
			url, purpose, audience, \
			colaborators, price, language, \
			equipment, headset, headsetPotential, \
			evaluation) \
			VALUES("%d", "%s", "%s", "%d", \
			"%s", "%s", "%s", "%s", "%f", \
			"%s", "%s", "%s", "%s", "%s")', row)

# disconnect from server
db.commit()
db.close()
