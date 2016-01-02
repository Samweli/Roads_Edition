import sqlite3
import csv


def add(){
	connection = connect('database/duplicates_to_identify')
	c = connection.cursor()

	with open('DISTRICT-COUNCIL-ROADNETWORK-Cleaned-csv_.csv') as csvfile:

		reader = csv.DictReader(csvfile)
		for row in reader:
			id = row['ID Number']
			road_name = row['Road Name']

			t = (road_name)
			c.execute('SELECT * FROM * WHERE Road Name LIKE ?', t)
			c.fetchone[0]


}

def connect(name){
	conn = sqlite3.connect(name)

	return conn
}