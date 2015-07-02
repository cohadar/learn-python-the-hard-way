ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) < 10:
	one_stuff = more_stuff.pop()
	stuff.append(one_stuff)

print stuff

print stuff[-1]
print '#@'.join(stuff[3:6])

colors = list('abcd')
numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Z', 'L', 'K'] 
cards = [(color, number) for color in colors for number in numbers]
print len(cards)
print cards