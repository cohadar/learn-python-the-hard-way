import sys

script, filename = sys.argv
txt = open(filename)

print "Your filename is %r" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input('> ')
txt_again = open(file_again)
print txt_again.read()
