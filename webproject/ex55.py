name = 'Seth M. Leslie'
age = 35 # not a lie
height = 71 # inches
weight = 163 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
print "For casting they use kilograms and centimeters."
print "So %s inches is %s centimeters and %s pounds is %s Kilos." % (
	height, height * 2.54, weight, weight * 0.45)