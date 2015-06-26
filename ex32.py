# ha I know, I will mix exercises random smart-ass-ness

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	if fruit[0] in "aeiou":
		print "an %s is a fruit" % fruit
	else:
		print "a %s is a fruit too" % fruit 

for i in change:
	try:
		ii = int(i)
		print "%d =" % ii,
	except ValueError:
	 	print i

elements = []
for i in range(6):
	print "adding %d into list" % i
	elements.append(i)

print elements

# reading pydoc is most useful part of this exercises