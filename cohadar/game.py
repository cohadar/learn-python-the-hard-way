"""Classes for a Game."""


class Room(object):
	"""Room is something you can walk in and out of.

	It has a name and a description. 
	It also has a dictionary of "paths" to other rooms.
	"""

	def __init__(self, name, description):
		"""create a room with a name and description and no paths"""
		self.name = name
		self.description = description
		self.paths = {}

	def add_paths(self, paths):
		"""Blah blah blah."""
		self.paths.update(paths)

	def go(self, direction):
		"""Go go go, fire in the hole!"""
		return self.paths.get(direction, None)

	def __repr__(self):
		"""Ha, this is very useful in test debugging."""
		return "Room(name=%s)" % self.name
		