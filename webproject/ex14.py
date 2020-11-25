from sys import argv

script, user_name = argv
prompt = '>>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "Let's make you a character."
print "Choose your class... \n\t*Thief \n\t*Knight \n\t*Mage"
C_Class = raw_input(prompt)

print "Okay %r, choose your weapon... \n\t*Dagger \n\t*Sword \n\t*Staff" % C_Class
weapon = raw_input(prompt)

print "Choose your home town... \n\t*Bogsville \n\t*Skull Tower \n\t*Castle Nip"
home_town = raw_input(prompt)

print """
Alight, so %r, you're a %r.
You wield a %r ferociously.
You set off on your journey from
your homestead of %r. Good Luck!!!
""" % (user_name, C_Class, weapon, home_town)