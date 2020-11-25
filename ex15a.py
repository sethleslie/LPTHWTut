print "Welcome to Seth's file reader."
print "First we're going to open a file."

file = raw_input("""
	You may choose from the following two files:
	ex15_sample.txt
	or
	ex15_sample2.txt
	>>>
	""")
	
txt = open(file)

print "Here's your file %r." % file

print txt.read()