from sys import argv # searches sys for argv
from os.path import exists # imports exists from os.path

script, from_file, to_file = argv # user defines the argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too. How? indata = open(from_file).read()
indata = open(from_file).read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(indata)

# open(to_file, 'w').write(indata)

print "Alright, all done."