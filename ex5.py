name = 'Slim Shady'
age = 35  # noone gieves a fuck
height = 74  # inches ffs, learn some fucking metric system
weight = 180  # kilos, hehe
eyes = 'Bullshit'
teeth = "Red"
hair = 'Pink'

print "Let's talk about sex baby %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually you are a fat ass."
print "He's got %s eyes abd %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky if you never saw a text editor before, blah
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

inches_to_centimeters = 2.54
pounds_to_kilograms = 0.45359237

import math
print "%1.8e" % math.pi
print "%.9g" % math.pi
print "%1.16e" % math.pi
print "%.17g" % math.pi

print "%-10d%-10d" % (75, 67)
print "%010d %010d" % (75, 67)
print "%#10d %#10d" % (75, 67)
print "% 10d % 10d" % (75, -67)

print "This {} is {} silly {} stupid".format(3, math.pi, 'njak')

print round(math.pi)
