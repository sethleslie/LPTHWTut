# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun" # naming days
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n Puts text on a new line
	#lets test this below. Yup. That worked \n stands for "new line"

print "Here are the days: ", days # prints string with named string added
print "Here are the months:" + months # why the comma here? Oh thats why. works
	# the same as a + symbol

print """
There's something \ngoing on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" # triple quotes will print anything between them