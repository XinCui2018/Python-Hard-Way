people = 10
cats = 30
dogs = 15

if people < cats:
    print ("Too many cats! The world is doomed!")

if people > cats:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")

if people > dogs:
    print ("The world is dry!")

# increment by operator
dogs += 5
# dogs = dogs + 5

if people >= dogs:
    print ("People are greater than or equal to dogs.")

if people <= dogs:
    print ("People are less than or equal to dogs.")

if people == dogs:
    print ("People are dogs.")

if "1" == "1" and "A" == "B":
    print ("Not possible")
else:
    print ("It is possible")

if True or False:
    print ("Possible")