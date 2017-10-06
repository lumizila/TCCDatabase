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
	query = []
	for el in row:
		query.append(str(el))
	print(query)
	dbQuery = ('INSERT INTO Material( \
			id, type, title, author, year, institution, \
			country, url, searchEngine,  purpose, audience, \
			colaborators, price, language, \
			equipment, headset, headsetPotential, \
			evaluation) \
			VALUES("'+query[0]+'","'+query[1]+'","'+query[2]+'", \
			"'+query[3]+'","'+query[4]+'","'+query[5]+'","'+query[6]+'", \
			"'+query[7]+'","'+query[8]+'","'+query[9]+'","'+query[10]+'", \
			"'+query[11]+'","'+query[12]+'","'+query[13]+'","'+query[14]+'", \
			"'+query[15]+'","'+query[16]+'","'+query[17]+'")')

	cursor.execute(dbQuery)

#	cursor.execute('INSERT INTO Material( \
#			id, type, title, author, year, institution, \
#			country, url, searchEngine,  purpose, audience, \
#			colaborators, price, language, \
#			equipment, headset, headsetPotential, \
#			evaluation) \
#			VALUES("%s", "%s", "%s", "%s", \
#			"%s", "%s", "%s", "%s", "%s", "%s", \
#			"%s", "%s", "%s", "%s", "%s")', query)

#			VALUES("%d", "%s", "%s", "%s", \
#			"%s", "%s", "%s", "%s", "%s", "%s", \
#			"%s", "%s", "%s", "%s", "%s")', m_id, m_type, m_title, m_author, m_year, m_institution, m_country, m_url, m_search, m_purpose, m_audience, m_colaborators, m_price, m_language, m_equipment, m_headset, m_potential, m_evaluation)


# disconnect from server
db.commit()
db.close()
