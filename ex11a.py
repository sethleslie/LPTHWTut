print "What is your name?"
my_name = raw_input()
print """
	Hello, %s, it's nice to meet you.
	Thank you for using our ultrafast
	ultra teck, high speed delivery service!
	\n\tI'm now going to ask you a few simple questions
	Don't worry.
	This is not a test.
	Have a glass of water if it will help.
	""" % my_name
	
print "How old are you?"
my_age = raw_input()
print "How tall are you?"
my_height = raw_input()
print """
	Do you prefer
	Long walks
	or
	Horror movies?
	"""
preference1 = raw_input()

print """
	Italian
	or
	Mexican?
	"""
preference2 = raw_input()

print """
	Inner
	or
	Outtie?
	"""
	
preference3 = raw_input()

print """
	Thank you. Shall we begin?
	"""

preference4 = raw_input()

sex_bot_age = str(int(my_age) - 5)

print """
	%s, your new %s tall
	%s SUPER SEXBOT will arrive in 3 days
	She enjoys %s
	will have a custom %s bellybutton
	and will look approximately %s years old
	minus 5 years. I haven't learnt
	how to put a named variable
	into a maths formular yet...
	THANK YOU FOR USING SETH's
	SEXBOT DELIVERY SERVICE!!!
	BOOYA!!!!
	""" % (my_name, my_height, preference2, preference1, preference3, sex_bot_age)
	
	