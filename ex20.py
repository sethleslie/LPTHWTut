# Tells the system to import an argument
from sys import argv
# user defines the argv ie. ex20.py Test.txt
script, input_file = argv

#creates a function to read and print the defined file
def print_all(f):
	print f.read()

# This function will return to the first byte of the file
def rewind(f):
	f.seek(0)

#creates a function to read and print specific lines from the file
def print_a_line(line_count, f):
	print line_count, f.readline()

#defines the variable "current_file" and uses the "open" command
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# runs the print_a_line function using a number variable
# to determine which line to print from the current_file variable
current_line = 1
print_a_line(current_line, current_file)

# adds onto the previous number to print the next line
current_line = current_line + 1
print_a_line(current_line, current_file)

# += is a contraction of c_l = c_l +1
# OR x = x + y becomes x += y
current_line += 1
print_a_line(current_line, current_file)