from sqlalchemy import and_, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import asc, desc, func


def main():
	"""Main entry point of the program"""

	# Connect to the database using SQLAlchemy
	with resources.path(
		"project.data", "database_test.db"
	) as sqlite_filepath:
		engine = create_engine(f"sqlite:///{sqlite_filepath}")

	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()


def add_new_trainee(session, firstName, lastName, trainDate, position):
	"""Adds a new trainee to the system"""

	# Check if trainee exists
	trainee = (
		session.query(Trainee)
		.filter(Trainee.first_name == firstName, Trainee.last_name == lastName)
		.one_or_none()
	)

	# Does the trainee already exist?
	if trainee is not None:
		print("Error. Trainee exists.")
		return

	# Create the new trainee if needed
	if trainee is None:
		trainee = Trainee(first_name=firstName, last_name=lastName, train_date=trainDate, position=position)
		print("Trainee successfully added.")

	session.add(trainee)