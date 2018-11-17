from random import sample
from string import ascii_uppercase, digits

class Robot(object):

	name = None

	def __init__(self):
		self.reset()

	def reset(self):
		self.name = self._generate_new_name()
	
	def _generate_new_name(self):
		letters = "".join(sample(ascii_uppercase, 2))
		numbers = "".join(sample(digits, 3))
		new_name = u'{}{}'.format(letters, numbers)

		if not self.name:			
			return new_name

		if self.name == new_name:
			return self._generate_new_name()

		return new_name