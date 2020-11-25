

x = "It's fleece was white as %s"
y = 'shit'

print "Mary had a little lamb." # makes a string of text
print x % 'snow' # a string with the word snow in it
print "And everywhere that Mary went." # adds a string of text
print "." * 10 # Adds a string and then prints it ten times consecutively

print x % y

end1 = "C" # names C
end2 = "h" # names H etc
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

z = """
	Seth is really hungry. Right now he feels like a %s
	but it'll make hime feel %s.
	""" # this is what I was looking for to make this work!!!
	
w = "Seth is really hungry. Right now he feels like a %s \nbut it'll make him feel %s."
	
print z % (end1 + end2 + end3+ end4 + end5 + end6 # this worked!!!
	+ end7 + end8 + end9 + end10 + end11 + end12, y)

print w % (end1 + end2 + end3+ end4 + end5 + end6
	+ end7 + end8 + end9 + end10 + end11 + end12, y)

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3+ end4 + end5 + end6, # a comma adds a space but
	# continues same line
print end7 + end8 + end9 + end10 + end11 + end12 # + adds all the strings together