# use %d and show the number 10
x = "There are %d types of people." % 10
# string
binary = "binary"
do_not = "don't"
# print a string with 2 string variable. Do not forget the percent mark % between the string and the variable.
# Also, two variables should be in the parenthesis. 
y = "Those who knows %s and those who %s." % (binary, do_not)

print (x)
print (y)
# %r means print no matter what inside of the variable
print("I said : %r" % x)
# %s means print the variable but only the string part. If you want to print '' as well, you need to type '%s'
print("I also said: '%s'" % y)

# This is a boolean function, which means this joke is not hilarious. 
hilarious = False
# %r is very important in this command. Without it , you will get an error. 
joke_evaluation = "Isn't that joke so funny?! %r"
# The variable name is after %. It actually means False. 
print(joke_evaluation % hilarious)

# The codes below show how to add two strings together.
# We can define a variable as a string by using "". 
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)