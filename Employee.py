class Trainee:

	def __init__(self, first='', last='', start_date=000000):
		self.first = first
		self.last = last
		self.start_date = start_date


	@property
	def email(self):
		first_letter = first[0]
		return '{}.{}@bell.bank'.format(self.first_letter, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def __repr__(self):
		return "Trainee('{}', '{}', {})".format(self.first, self.last, self.start_date)