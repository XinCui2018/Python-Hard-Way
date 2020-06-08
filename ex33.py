# i = 0
# numbers = []

# while i < 6:
#     print ("At the top i is %d" % i)
#     numbers.append(i)

#     i += 1
#     print ("Numbers now: ", numbers)
#     print ("At the bottom i is %d" % i)

# print ("The numbers: ")
# for number in numbers:
#     print (number)

numbers = []
def new_function (i):
    while i in range(0,6):
        print ("At the top i is %d" % i)
        numbers.append(i)
        i += 1
        print ("Numbers now: ", numbers)
        print ("At the bottom i is %d" % i)
start_point = int(input("> "))
if start_point == 1:
    new_function(start_point)
    print ("The numbers: ")
    for number in numbers:
        print (number)
else:
    print ("The number %d can not call the function." % start_point)

