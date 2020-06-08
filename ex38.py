ten_things = "Apples Oranges Crows Telephone Light Sugar"
print ("Wait, there is not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
# print (stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# the function len() returns the length of the string.
while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop() removes and returns last value from the list or the given index value
    print ("Adding: ", next_one)
    stuff.append(next_one) #append() adds a single item to the end of the existing list
    print ("There is %d items now." % len(stuff))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1]) # oranges
print (stuff[-1]) # whoa! fancy
print (stuff.pop())

# '---'.join(stuff) is join('---', stuff); '---'.join(stuff) reads join stuff with '---' between them; join('---', stuff) means call join with '---' and stuff.
print ('---'.join(stuff)) # what? cool!
# ' # '.join(stuff[3:5]) is join ' # ' between element 3 and element 4, it does not include element 5. It is similar to how range (3,5) would work.
print (' # '.join(stuff[3:5]))  # super stellar!

#OOP is object-oriented programming