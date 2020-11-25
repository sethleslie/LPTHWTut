from sys import argv # tells python to look for files in system as defined by argv

script, filename = argv # defines the files

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)." # ^C tracesback, or cancels module
print "If you do want that, hit RETURN."

raw_input("?") # a simple return will move on to next stage

print "Opening the file..."
target = open(filename, 'w') # w opens file in write mode

print "Truncating the file. Goodbye!"
target.truncate() # truncate empties the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) # target opens file in write mode and adds script
target.write("\n") # target opens file in write mode and adds escape \n
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close() # closes the file