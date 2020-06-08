people = 16
cars = 7
buses = 15

if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can not decide.")

if buses > cars:
    print ("That is too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can not decide.")

if people > buses:
    print ("Alright, let us just take buses.")
else:
    print ("Fine, let us stay home then.")

if buses > cars and people < buses:
    print ("Let us take buses.")
elif buses > cars and not people < buses:
    print ("I do not know what to do.")
else:
    print ("Let us take cars.")