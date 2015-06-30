import sys

def gold_room():
	print "this room is full of gold, how much do you take?"
	choice = raw_input('> ')
	try:
		how_much = int(choice)
	except ValueError:
		dead('learn to type a number')
		
	if how_much < 50:
		print "Nice, you are not greedy, you win"
		sys.exit(0)
	else:
		dead("You greedy bastard")

def bear_room():
	print "There is a bear here, he has lots of honey"
	print "The fat bear is in front of another door, how will you move the bear?"
	bear_moved = False
	for _ in xrange(10000):
		choice = raw_input('> ')
		if choice == 'take honey':
			dead('bear slaps your face off')
		elif choice == 'taun bear' and not bear_moved:
			print "bear has moved"
			bear_moved = True
		elif choice == 'taun bear' and bear_moved:\
			dead('bear catches you, you get ucked')
		elif choice == 'open door' and bear_moved:
			gold_room()
		else:
			print "unknown choice, try: 'take honey', 'taun bear' or 'open door'"

def cthulhu_room():
	print "You see the great evil Cthulhu"
	print "You go insane"
	print "Flee for your life or eat your own head?"
	choice = raw_input('> ')
	if 'flee' in choice:
		start()
	elif 'head' in choice:
		dead("your head tastes good")
	else:
		cthulhu_room()

def dead(why):
	print why, 'Good Job!'
	sys.exit(0)

def start():
	print "You are in a dark room"
	print "There is a door to your right and left"
	print "which one do you take"
	choice = raw_input('> ')
	if choice == 'left':
		bear_room()
	elif choice == 'right':
		cthulhu_room()
	else:
		dead('wandering around you fell into a pit')

start()








