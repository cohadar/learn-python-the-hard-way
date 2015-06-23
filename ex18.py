def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

print_two(3, 4)
print_two(*['list', 'unwind'])

