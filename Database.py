import sqlite3

class Database:
	def conn(self):
		print("Database : connection method called")
		con = sqlite3.connect("trainees.db")
		cur = con.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Trainees(
								)')