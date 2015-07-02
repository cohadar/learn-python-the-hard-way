# seriously "is-a" and "has-a." for the milionth time, how is this the core of oop?

class Person(object):
	def __init__(self, name):
		self.name = name


class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

e1 = Employee('Mighty', 10000000)


# it seems the super function only works for new style classes