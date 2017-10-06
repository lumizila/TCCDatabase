#!/usr/bin/python

import MySQLdb
import sys

# Open database connection
db = MySQLdb.connect("localhost","root","","TCC" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Read material title
m_title = raw_input("What's the material title?\n")

# Check if Material already exists
dbQuery = "SELECT * FROM Material WHERE title='"+m_title+"'"
cursor.execute(dbQuery)
res = cursor.fetchall()

if (cursor.rowcount != 0):
	print "A material(s) with this name already exists, is it a new one?(yes/no):"
	for row in res:
		print row

	is_new = raw_input("\n")
	if(is_new == "no"):
		engine = raw_input("Whats the search engine used?\n") 
		#TODO
		sys.exit(0)

# Insert new material
m_type = raw_input("Material type:\n")
m_author = raw_input("Author:\n")
m_year = raw_input("Year:\n")
m_institution = raw_input("Institution\n")
m_country = raw_input("Country:\n")
m_url = raw_input("url:\n")
m_engine = raw_input("Search Engine:\n")
m_purpose = raw_input("Purpose:\n")
m_audience = raw_input("Audience:\n")
m_colaborators = raw_input("Colaborators:\n")
m_price = raw_input("Price:\n")
m_language = raw_input("Language:\n")
m_equipment = raw_input("Other equipment used:\n")
m_headset = raw_input("Headset used:\n")
m_potential = raw_input("Headset potential:\n")
m_eval = raw_input("App evaluation:\n")

dbQuery = 'INSERT INTO Material ( \
		type, title, author, year, institution, \
		country, url, searchEngine,  purpose, audience, \
		colaborators, price, language, \
		equipment, headset, headsetPotential, evaluation) \
		VALUES("'+m_type+'","'+m_title+'","'+m_author+'","'+m_year+'",\
		"'+m_institution+'","'+m_country+'","'+m_url+'","'+m_engine+'",\
		"'+m_purpose+'","'+m_audience+'","'+m_colaborators+'",\
		"'+m_price+'","'+m_language+'","'+m_equipment+'","'+m_headset+'",\
		"'+m_potential+'","'+m_eval+'")'

cursor.execute(dbQuery)
db.commit()
db.close()
