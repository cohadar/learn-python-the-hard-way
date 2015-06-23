import sys

script, user_name = sys.argv
prompt = '> '

print 'Hi %s, I\'m the %s script.' % (user_name, script)
print "blah blah"

print 'Do you like me %s?' % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me,
you live in %r. Not sure where that is.
And tou have %r computer. Nice.
""" % (likes, lives, computer)
