import sqlite3
import csv


def add():
	location = './databases/duplicates_to_identify.sqlite'
	conn = connect(location)

	connection  = conn.cursor()

	# Opening the csv file
	with open('DISTRICT-COUNCIL-ROADNETWORK-Cleaned-csv_.csv') as csvfile:
		# Reading road name from csv file and matching it from 
		# the topology features

		reader = csv.DictReader(csvfile)
		results = {}
		for row in reader:
			id = row['ID Number']
			road_name = row['Road Name']

			t = (road_name)
			if connection is not None:
				connection.execute('SELECT OGC_FID,id_number,road_name,'\
					'road_qlty FROM duplicates_to_identify WHERE road_name'\
					' LIKE (?)', (t,))
				for row in connection:
					
					results[row[0]] = row
				# Iterating again, here the value of connection will be updated
				# but this wont affect anything as we have already stored
				# the past results
				for key,value in results.iteritems():
					insert = id
					connection.execute('UPDATE duplicates_to_identify SET '\
						'id_number = (?) WHERE OGC_FID = (?)', (insert, value[0]))
					
					print 'added',id,'into',value[2]
					# Committing added id
					conn.commit()
			else:
				print "Problem in reading the database"
				break
	# Closing, this will flush all the changes
	conn.close()


def connect(name):
	conn = None
	try:
	    # Connect the database
		conn = sqlite3.connect(name)
	except sqlite3.Error as e:
		print e.args[0]

	return conn


if __name__ == "__main__":
	add()
