import sqlite3
def db_init():

  	db = sqlite3.connect('temp.db')
  	db.execute('''
  	DROP TABLE IF EXISTS `measures`;
  	''')
  	db.execute('''CREATE TABLE IF NOT EXISTS measures (
  	    meas_time INT PRIMARY KEY,
  	    temp NUMERIC,
  	    humidity NUMERIC,
  	    pressure NUMERIC
  	);''')
  	
	
