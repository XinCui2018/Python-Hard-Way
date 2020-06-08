# print ("Let's practice everything.")
# print ('You\'d need to know\'about escapes with \\ that do\nnewlines and \ttabs.')

# poem = """
# \t The lovely world
# with logic so firmly planted
# cannot discern \nthe needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """
# print ("--------")
# print (poem)
# print ("-------------")

# five = 10 - 2 + 3 - 6
# print ("This should be five: %s" % five)

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates

# start_point = 10000
# # Notice that I use beans rather than jelly_beans in the next line. It still works. 
# # The reason is that inside the function the variable is temporary.
# # When you return it, it can be assigned to the later variable. 
# beans, jars, crates = secret_formula(start_point)

# print ("With a starting point of: %d" % start_point)
# print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

# start_point = start_point / 10

# print ("We can also do that this way:")
# print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))


# print ("Let's practice everything!")
# print ('You\'d need to know \'about the escape with \\ that do\nnew lines and \ttabs!')

# peom = """
# \t\t\t\t\t\t\t\tThis is a peom written by Xin
# The theme of the peom \nis faith and belief
# We need to live with the holy spirit
# \n\t\t Which is from God!
# """
# print ("---------")
# print (peom)
# print ("---------")

# six  = 10 + 2 - 1 -5
# print ("This should be six: %d" %six)

# def new_fomula (start):
#     clothes = start * 10
#     socks = clothes / 2
#     jeans = socks * 13
#     return clothes, socks, jeans

# start_point = 100
# garment, socks, jeans = new_fomula(start_point)

# print ("With the start point: %d" % start_point)
# print ("We have %d garment, %d socks, and %d jeans" % (garment,socks, jeans))

# start_point = start_point/10
# print ("We can also do it in this way.")
# print ("We have %d garment, %d socks, and %d jeans" % new_fomula(start_point))

print ("Let us practice everything.")
print ('You\'d need to know \' about escapes with \\that do \nnewlines and \t tabs.')

poem = """
\t A new poem
Oh my dear lord
I need you to guide me \nto learn Python
You can give me wisdom to master
\n\t\t all the functions in Python.
Amen!
"""
print ("-----------")
print (poem)
print ("-----------")

two = 2 + 4 - 2 * 2
print ("This should be two: %s" %two)

def new_function(start):
    tomatoes = start * 3
    potatoes = tomatoes - 2
    eggplants = potatoes + 4
    return tomatoes, potatoes, eggplants

startpoint = 30
tomatoes, potatoes, eggplants = new_function(startpoint)
print ("With a starting point of: %d" % startpoint)
print ("We'd have %d tomatoes, %d potatoes, and %d eggplants" % (tomatoes, potatoes, eggplants))

startpoint = startpoint/2
print ("We can also do that this way.")
print ("We have %d tomatoes, %d potatoes, and %d eggplants" % new_function(startpoint))
