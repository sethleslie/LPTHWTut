def Adventure(level, skill, food):
	print "You're a level %d rogue!" % level
	print "You've reached an archery level of %d!" % skill
	print "You have %d serves of food." % food
	print "Welcome to the DUNGEON!\nAnd may the GODS be with you.\n"

Adventure(12, 11, 10)
# THIS IS HOW INT( WORKS!!!!!
print "Let's try using raw_input!"
your_class = int(raw_input("Choose your rogue level:"))
your_skill = int(raw_input("Choose your archery level:"))
your_food = int(raw_input("How many serves of food will you bring?"))

Adventure(your_class, your_skill, your_food)


Adventure(10+3, 11-4, 2*8)

print "Oh my gosh! You leveled up!!!"
print "Let's view your new stats:"

Adventure(your_class + 1, your_skill + 5, your_food / 2)