import sys
import os

script, from_file, to_file = sys.argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file); indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % os.path.exists(to_file)
raw_input("ENTER to continue, CTRL-C to cancel")

out_file = open(to_file, 'w')
out_file.write(indata)


in_file.close()
out_file.close()

print "Done."
