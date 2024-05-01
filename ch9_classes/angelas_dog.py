class Dog:
	"""A simple attempt to model a dog."""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

eleos_dog=Dog("pepito",2)
print(f"My dog's name is {eleos_dog.name}")

angelas_dog=Dog("fulanito",6)
print(f"My dog's name is {angelas_dog.name}")