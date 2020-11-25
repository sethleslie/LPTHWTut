# create the function.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the function numbers directly:"
# run the function with numbers in place of the args
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# define some variables
amount_of_cheese = 10
amount_of_crackers = 50
#call the function using defined variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do maths inside too:"
# use the function with numbers and math in place of the args
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
#use both variables and math in place of the args
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)