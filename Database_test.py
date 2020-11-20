from sqlalchemy import MetaData, create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Creates many-to-many relationship between 'trainee' and 'curriculum' tables below
trainee_curriculum = Table(
	"trainee_curriculum",
	Base.metadata,
	Column("trainee_id", Integer, ForeignKey("trainee.trainee_id")),
	Column("curriculum_id", Integer, ForeignKey("curriculum.curriculum_id")),
)

class Trainee(Base):
	__tablename__ = "trainee"
	trainee_id = Column(Integer, primary_key=True)
	first_name = Column(String(50))
	last_name = Column(String)
	train_date = Column(Integer)
	position = Column(String)
	curriculums = relationship("Curriculum", backref=backref("trainee"))

class Curriculum(Base):
	__tablename__ = "curriculum"
	id = Column(Integer, primary_key=True)
	curriculum_id = Column(Integer, ForeignKey("trainee.trainee_id"))
	curriculum_title = Column(String)
	quizzes = relationship("Quiz", backref=backref("Curriculum"))
	modules = relationship("Module", backref=backref("Curriculum"))

class Quiz(Base):
	__tablename__ = "quiz"
	id = Column(Integer, primary_key=True)
	quiz_id = Column(Integer, ForeignKey("curriculum.quiz_id"))
	title = Column(String)
	grade = Column(Integer)
	notes = Column(String)

class Module(Base):
	__tablename__ = "module"
	id = Column(Integer, primary_key=True)
	module_id = Column(Integer, ForeignKey("curriculum.module_id"))
	title = Column(String)
	grade = Column(Integer)
	notes = Column(String)