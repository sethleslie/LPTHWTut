tabby_cat = "\tI'm tabbed in." # \t tabbes the line
persian_cat = "I'm split\non a line" # \n drops to a new line
backslash_cat = "I'm \\ a \\ cat." # \\ adds a \ into the text
# \ backslash works as an escape to add instruction inside the string
fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
""" # this could also be writted \n\t* Cat Food \n\t* Fishies right?? Yes!!!

print """
Seth's new list: \n\t* Catfood \n\t* Fishies
""" # don't forget to close the """!!!

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "This is with an %r."
print " Seth says he %r something, but I don't belive it." % "\"saw\""
# %r will print how you write it in the file, while %s prints what you want to see

print "But this is with an %s."
print " Seth says he %s something, but I don't belive it." % "\"saw\""

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
		