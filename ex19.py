# make sure to use def when you create a new function;
# the name of the function is New_function is this case;
# in the parethesis, we need to use comma to seperate the variables in the function
# Do not forget the colon after the end )
def new_function(cheese_count, boxes_of_crackers):
    # the functions are intented 4 spaces
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man it is enough for the party!")
    print ("Get the blanket.\n")

print ("We can just give the function numbers directly!")
new_function (20, 30)

print ("OR, we can use variables from our script:")
cheese_count = 20
boxes_of_crackers = 50
new_function(cheese_count, boxes_of_crackers)

print ("We can even do math inside too:")
new_function(10 + 5, 30 + 15)

print ("And we can combine the two, variables and math")
new_function(cheese_count + 10, boxes_of_crackers + 20)