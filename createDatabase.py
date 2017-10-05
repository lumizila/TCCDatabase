#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","TCC" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS Material")

# Create table as per requirement
sql = """CREATE TABLE Material(
         id INT NOT NULL,
         type CHAR(20),
         author CHAR(100),  
         year INT,
	 url CHAR(100),
	 purpose CHAR(200),
	 audience CHAR(100),
	 colaborators CHAR(100),
	 price FLOAT,
	 language CHAR(100),
	 equipment CHAR(200),
	 headset CHAR(100),
	 headsetPotential CHAR(200),
	 evaluation CHAR(100) )"""

cursor.execute(sql)

# disconnect from server
db.close()
