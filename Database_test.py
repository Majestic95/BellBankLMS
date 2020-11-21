from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database_test.db', echo=True)

Base = declarative_base()

# Creates many-to-many relationship between 'trainee' and 'curriculum' tables below
trainee_curriculum = Table(
	"trainee_curriculum",
	Base.metadata,
	Column("trainee_id", Integer, ForeignKey("trainee.trainee_id"), primary_key=True),
	Column("curriculum_id", Integer, ForeignKey("curriculum.curriculum_id"), primary_key=True),
)

# Creates 'trainee' table with many-to-many relationship ('trainee_curriculum')
class Trainee(Base):
	__tablename__ = "trainee"
	trainee_id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	train_date = Column(Integer)
	position = Column(String)
	curriculums = relationship(
		"Curriculum", secondary=trainee_curriculum, back_populates="trainees"
	)

# Creates 'curriculum' table with many-to-many relationship ('trainee_curriculum')
# and one-to-many relationship ('quiz' and 'module' tables)
class Curriculum(Base):
	__tablename__ = "curriculum"
	curriculum_id = Column(Integer, primary_key=True)
	curriculum_title = Column(String)
	quizzes = relationship("Quiz", backref=backref("Curriculum"))
	modules = relationship("Module", backref=backref("Curriculum"))
	trainees = relationship(
		"Trainee", secondary=trainee_curriculum, back_populates="curriculums"
	)

# Creates 'quiz' table with many-to-one relationship ('curriculum')
class Quiz(Base):
	__tablename__ = "quiz"
	quiz_id = Column(Integer, primary_key=True)
	curriculum_id = Column(Integer, ForeignKey("curriculum.curriculum_id"))
	title = Column(String)
	grade = Column(Integer)
	notes = Column(String)

# Creates 'module' table with many-to-one relationship ('curriculum')
class Module(Base):
	__tablename__ = "module"
	module_id = Column(Integer, primary_key=True)
	curriculum_id = Column(Integer, ForeignKey("curriculum.curriculum_id"))
	title = Column(String)
	grade = Column(Integer)
	notes = Column(String)



Base.metadata.create_all(engine)