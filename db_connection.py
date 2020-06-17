import sqlite3
from Employee import Trainee

conn = sqlite3.connect('trainee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS trainees (
# 			first text,
# 			last text,
# 			start_date integer
# )""")

conn.commit()

trainee = Trainee()


def get_firstname():
	trainee.first = input("Enter your first name: ")


def get_lastname():
	trainee.last = input("Enter your last name: ")


def get_start():
	trainee.start_date = input("Please enter the date you started with the company (in this format: 010120): ")

get_firstname()