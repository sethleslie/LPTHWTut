x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# I removed an extra stop in the later steps to neaten this up
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'" % y

hilarious = False
awful = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % awful

w = "This is the left side of..."
e = " a string with a right side."

print w + e