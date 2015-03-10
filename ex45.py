'''
#=============================================================================
#     FileName: ex45.py 
#         Desc: class 
#       Author: Honglong Wu
#        Email: wuhonglong@genomics.cn
#      Version: 0.0.1
#      Created: 11/03/2015
#      History:
#=============================================================================
'''

#-*- coding: utf-8 -*-

## Animal is an object
class Animal(object):
	pass

# Dog
class Dog(Animal):

	def __init__(self, name):
		# annotate
		self.name = name

# Cat
class Cat(Animal):

	def __init__(self, name):
		# annotate
		self.name = name

# person
class Person(object):
	
	def __init__(self, name):
		#
		self.name = name
	
		# person has a pet
		self.pet = None
	
# 
class Employee(Person):
	
	def __init__(self, name, salary):
		#
		super(Employee, self).__init__(name)
		#
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

