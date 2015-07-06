class Parent(object):
	def method(self):
		print "Parent method"

class Child(Parent):
	def method(self):
		print "Child method before"
		super(Child, self).method()
		print "Child method after"

child = Child()
child.method()


# read PEP8
# read PEP257