from sys import argv

script, user_name, character_class = argv # this sets the user name variable in the argument
prompt = '> ' # this makes the raw input slightly more attractive to look at

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt) # asks for user input contributed to name likes

print "I see you're a %r. Do you wish to keep this class?" % (character_class)
character = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)