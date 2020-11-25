from sys import argv # searches sys for argv

script, from_file, to_file = argv # user defines the argv
indata = open(from_file).read()

print "The input file is %d bytes long." % len(indata)

open(to_file, 'w').write(indata)

print "Alright, all done."