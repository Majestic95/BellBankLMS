from importlib import resources

from sqlalchemy import and_, create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import asc, desc, func

from Database_test import Trainee, Curriculum, Quiz, Module

from treelib import Tree


def get_quizzes_by_curriculum(session, ascending=True):
	"""Get a list of curriculums and the number of quizzes they contain
	Args:
		session: database session to use
		ascending: direction to sort the results
	Returns:
		List: list of curriculums sorted by number of quizzes contained
	"""
	if not isinstance(ascending, bool):
		raise ValueError(f"Sorting value invalid: {ascending}")

	direction = asc if ascending else desc

	return (
		session.query(
			Curriculum.curriculum_title,
			func.count(Quiz.title).label("total_quizzes")
		)
		.join(Curriculum.quizzes)
		.group_by(Curriculum.curriculum_title)
		.order_by(direction("total_quizzes"))
	)


def add_new_trainee(session, first_name, last_name, train_date, position=None):
	"""Adds a new trainee to the system"""

	# Check if trainee exists
	trainee = (
		session.query(Trainee)
		.filter(Trainee.first_name == first_name, Trainee.last_name == last_name)
		.one_or_none()
	)

	# Does the trainee already exist?
	if trainee is not None:
		print("Error. Trainee exists.")
		return

	# Create the new trainee if needed
	if trainee is None:
		trainee = Trainee(first_name=first_name, last_name=last_name, train_date=train_date, position=position)
		print("Trainee successfully added.")

    # Commit to the database
	session.add(trainee)
	session.commit()


def add_new_curriculum(session, curriculum_title):
	"""Adds a new curriculum to the system"""

	# Check if curriculum exists
	curriculum = (
		session.query(Curriculum)
		.filter(Curriculum.curriculum_title == curriculum_title)
		.one_or_none()
	)

	# Does the curriculum already exist?
	if curriculum is not None:
		print("Error. Curriculum exists.")
		return

	# Create the new curriculum if needed
	if curriculum is None:
		curriculum = Curriculum(curriculum_title = curriculum_title)
		print("Curriculum successfully added.")

    # Commit to the database
	session.add(curriculum)
	session.commit()


def add_new_quiz(session, curriculum_title, quiz_title, quiz_grade, quiz_notes=None):
	"""Adds a new quiz to the system"""

	# Check if quiz exists
	quiz = (
		session.query(Quiz)
		.filter(Quiz.title == quiz_title)
		.one_or_none()
	)

	# Does the quiz already exist?
	if quiz is not None:
		print("Error. Quiz exists.")

	# Create the new quiz if needed
	if quiz is None:
		quiz = Quiz(title = quiz_title, grade = quiz_grade, notes = quiz_notes)
		print("Quiz successfully added.")

	# Get the curriculum
	curriculum = (
		session.query(Curriculum)
		.filter(Curriculum.curriculum_title == curriculum_title)
		.one_or_none()
		)

	# Do we need to create the curriculum?
	if curriculum is None:
		curriculum = Curriculum(curriculum_title = curriculum_title)
		session.add(curriculum)

	print(curriculum.curriculum_id)

	# Initialize the curriculum relationships
	quiz.curriculums.append(curriculum)
	session.add(quiz)

	# Commit to the database
	session.commit()


def get_trainees(session):
	"""Get a list of trainee objects sorted by last name"""
	return session.query(Trainee).order_by(Trainee.last_name).all()


def get_curriculums(session):
	"""Get a list of curriculum objects sorted by curriculum title"""
	return session.query(Curriculum).order_by(Curriculum.curriculum_title).all()


def get_quizzes(session):
	"""Get a list of quiz objects sorted by quiz title"""
	return session.query(Quiz).order_by(Quiz.title).all()


def output_trainee_hierarchy(trainees):
	"""
	Outputs the trainee information in a hierarchical manner
	:param trainees:		the collection of root trainee objects
	:return:				None
	"""
	trainees_tree = Tree()
	trainees_tree.create_node("Trainees", "trainees")
	for trainee in trainees:
		trainee_id = f"{trainee.first_name} {trainee.last_name}"
		trainees_tree.create_node(trainee_id, trainee_id, parent="trainees")
	# Output hierarchy trainees data
	trainees_tree.show()


def output_curriculum_hierarchy(curriculums):
	"""
	Outputs the curriculum information in a hierarchical manner
	:param curriculum:		the collection of root curriculum objects
	:return:				None
	"""
	curriculums_tree = Tree()
	curriculums_tree.create_node("Curriculums", "curriculums")
	for curriculum in curriculums:
		curriculum_id = f"{curriculum.curriculum_title}"
		curriculums_tree.create_node(curriculum_id, curriculum_id, parent="curriculums")
	# Output hierarchy curriculum data
	curriculums_tree.show()


def output_quiz_hierarchy(quizzes):
	"""
	Outputs the quiz information in a hierarchical manner
	:param quiz:			the collection of root quiz objects
	:return:				None
	"""
	quizzes_tree = Tree()
	quizzes_tree.create_node("Quizzes", "quizzes")
	for quiz in quizzes:
		quiz_id = f"{quiz.title}"
		quizzes_tree.create_node(quiz_id, quiz_id, parent="quizzes")
	# Output hierarchy quiz data
	quizzes_tree.show()


def main():
	"""Main entry point of the program"""

	# # Connect to the database using SQLAlchemy
	# with resources.path(
	# 	"project.data", "database_test.db"
	# ) as sqlite_filepath:
	engine = create_engine("sqlite:///database_test.db")

	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()

	# Get the number of quizzes within each curriculum
	quizzes_by_curriculum = get_quizzes_by_curriculum(session, ascending=False)
	for row in quizzes_by_curriculum:
		print(row)
	print()

	print("Quizzes to curriculums generated.")

	# add_new_trainee(
	# 	session,
	# 	first_name="Austin",
	# 	last_name="Noyes",
	# 	train_date='010615',
	# 	position="CSCTrainer",
	# 	)

	# add_new_curriculum(
	# 	session,
	# 	curriculum_title="CSC Level 1 Training",
	# 	)

	add_new_quiz(
		session,
		# curriculum_title won't be string entry, it will have GUI drop-down for user selection
		curriculum_title="CSC Level 1 Training",
		quiz_title="Checkpoint 1",
		quiz_grade="100",
		quiz_notes="This quiz went really well! You have made excellent progress!"
		)

	# Output hierarchical trainees data
	trainees = get_trainees(session)
	output_trainee_hierarchy(trainees)

	curriculums = get_curriculums(session)
	output_curriculum_hierarchy(curriculums)

	quizzes = get_quizzes(session)
	output_quiz_hierarchy(quizzes)

if __name__ == "__main__":
	main()