import sys

def print_all(current_file):
	print current_file.read()

def rewind(current_file):
	current_file.seek(0)

def print_a_line(line_num, current_file):
	print "[%d]%s"%(line_num, current_file.readline()),

script, filename = sys.argv
f = open(filename)

print "First print everything"
print_all(f)

rewind(f)
print "Than print 3 lines"
line = 0

line += 1
print_a_line(line, f)
line += 1
print_a_line(line, f)
line += 1
print_a_line(line, f)

f.close()
