#!/usr/bin/python

import MySQLdb
import sys

def rawInput(text):
	print(text)
	contents = []
	s = ""
	while True:
		try:
			line = raw_input("")
			line.replace("\n", " ")
		except EOFError:
			return s.join(contents)
		contents.append(line)
		print(contents)
		print("press ctrl+D to stop reading")

# Open database connection
db = MySQLdb.connect("localhost","root","","TCC" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Read material title
m_title = rawInput("What's the material title?")

# Check if Material already exists
dbQuery = "SELECT * FROM Material WHERE title='"+m_title+"'"
cursor.execute(dbQuery)
res = cursor.fetchall()

if (cursor.rowcount != 0):
	print "A material(s) with this name already exists, is it a new one?(yes/no):"
	for row in res:
		print row

	is_new = rawInput("\n")
	if(is_new == "no"):
		engine = raw_input("Whats the search engine used?\n") 
		#TODO
		sys.exit(0)

# Insert new material
m_type = rawInput("Material type:")
m_author = rawInput("Author:")
m_year = rawInput("Year:")
m_institution = rawInput("Institution")
m_country = rawInput("Country:")
m_url = rawInput("url:")
m_engine = rawInput("Search Engine:")
m_purpose = rawInput("Purpose:")
m_audience = rawInput("Audience:")
m_colaborators = rawInput("Colaborators:")
m_price = rawInput("Price:")
m_language = rawInput("Language:")
m_equipment = rawInput("Other equipment used:")
m_headset = rawInput("Headset used:")
m_potential = rawInput("Headset potential:")
m_eval = rawInput("App evaluation:")

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
