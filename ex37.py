# Insanity! I wonder if anyone ever finished this tutorial in the way author imagined.

class MyContextManager(object):
	def __init__(self, value):
		self.value = value
	def __enter__(self):
		if self.value == "raise_on_enter":
			raise ValueError(repr(self.value))
		print "__enter__", self.value
		return self.value
	def __exit__(self, typ, value, traceback):
		if self.value == "raise_on_exit":
			raise ValueError(repr(self.value))
		print "__exit__ type=%r, value=%r, traceback=%r" % (typ, value, traceback)
		#return True
	def njakz():
		pass

with MyContextManager("ok") as njak:
	print 'inside', njak

# with MyContextManager("raise_on_enter") as njak:
# 	print 'inside', njak

# with MyContextManager("raise_on_exit") as njak:
# 	print 'inside', njak

# with MyContextManager("raise_from_inside") as njak:
# 	raise ValueError(njak)


# Be careful with @contextmanager, yield must be in try-finally
from contextlib import contextmanager

###############################################################################
@contextmanager
def yourContextManager(value):
	# save
	pass
	try:
		# yield inner
		pass
	finally:
		# restore
		pass

for ii in xrange(10):
	print ii

assert ii == 9, "lol, where is your scope python"

###############################################################################
#Nested functions
def njak(a, b):
	def zrak(a, b):
		return a + b
	return zrak(a, b) * 2

exec 'print "njak", njak(3, 4)'

###############################################################################
my_global = 33

def inc_global():
	global my_global
	my_global += 1

inc_global()
print my_global

###############################################################################
class Jan:
	haha = 37   # class global variables should be either read-only 
	tricks = [] # or lists/dicts
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def janMethod(self, a, b):
		return a + b
	def febMethod(self):
		return "february" + str(self.a) + str(self.b)

jan1 = Jan(3, 4)
jan2 = Jan(5, 6)

j1f = jan1.febMethod
j2f = jan2.febMethod

print j1f(), j2f()

jan1.haha += 1 # two instances of haha in the += operator do NOT point to the same object!!!
print jan1.haha, Jan.haha, jan2.haha

jan1.tricks.append('aaa')
jan2.tricks.append('bbb')
print jan1.tricks
print jan1.__class__

class Feb(Jan):
	def __init__(self, a):
		Jan.__init__(self, a, 77)

feb1 = Feb(33)

print feb1.febMethod()

###############################################################################
class MarError(BaseException):
	pass
	# def __init__(self, a, b):
	# 	self.a = a
	# 	self.b = b
	# 	self.args = (a, b)
	# def __str__(self):
	# 	return "muhaha" + self.a + self.b

try:
	raise MarError(45, 67)
except MarError as instance:
	print instance.args
	print instance

# do not override exception __init__ without args and __str__ override


###############################################################################
def squares():
	i = 1
	while True:
		yield i * i
		i += 1

###############################################################################
from functools import wraps

def square_result(func):
	@wraps(func)
	def inner(*args, **kwargs):
		result = func(*args, **kwargs)
		return result * result
	return inner

def add2(a, b):
	""" my add2 function"""
	return a + b

decorated = square_result(add2)
print decorated(3, 4)
print decorated.__doc__
