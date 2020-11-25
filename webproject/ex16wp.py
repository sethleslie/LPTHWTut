from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file."

string = "%s, \n%s, \n%s, \n" % (line1, line2, line3)

target.write(string)

print "Now past Seth wants us to open the file."
print "Are you ready?"
raw_input("?")

target = open(filename, 'r')
print target.read()

print "And it's always good form to close the file."
target.close()