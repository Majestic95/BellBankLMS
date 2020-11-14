import sqlite3

class Database():

	def __init__(self, db):
		"""Init method which returns active connection when instantiated"""

		sql_create_trainees_table = """ CREATE TABLE IF NOT EXISTS trainees (
											id 			integer 	PRIMARY KEY,
											firstname 	text 		NOT NULL,
											lastname 	text 		NOT NULL,
											traindate 	integer,
											position 	text,
											FOREIGN KEY (id)
											);"""


		sql_create_modules_table = """CREATE TABLE IF NOT EXISTS modules (
											id 			integer 	PRIMARY KEY,
											title		text		NOT NULL,
											grade 		integer,
											);"""


		sql_create_curriculums_table = """CREATE TABLE IF NOT EXISTS curriculums (
											id 			integer		PRIMARY KEY,
											title 		text		NOT NULL,
											levelid		integer
											);"""


		try:
			conn = c