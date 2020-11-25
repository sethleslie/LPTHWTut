from sys import argv # tells python to take an argument from the system

script, filename = argv # sets the variables of the argument
# and how many arguments there are

txt = open(filename) # opens a text file 

print "Here's your file %r:" % filename # tells you the file has been retrieved
print txt.read() # prints the text contents of the file opened

print "Type the filename you wish to open:" # prints the question
file_again = raw_input("> ") # asks for file to be opened Should work with any file in folder

txt_again = open(file_again) # opens new specified file

print "Here's your file %r:" % (file_again)
print txt_again.read() # prints text of new file

# using only raw_input() allows you to change what you need inside the argument.

txt.close()