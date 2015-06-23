import sys

script, filename = sys.argv

print "We are going to erase %r" % filename
print "If you don't that hit CTRL-C"
print "If you want that, hit RETURN"

raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file!!!"
#target.truncate()

print "Now enter 3 lines"
line1 = raw_input('line1 > ')
line2 = raw_input('line2 > ')
line3 = raw_input('line3 > ')

print "No we write this to a file"

target.write(line1 + '\n')
target.write(line2 + '\n')
target.write(line3 + '\n')

print 'and finally we close it'

target.close()
