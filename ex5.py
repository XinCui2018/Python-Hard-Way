name = "Xin Cui"
age = 25 # not a lie
height = 177 #cm
weight = 70 # kg
eyes = "black"
teeth = "white"
hair = "black"

print ("Let's talk about %s." % name)
print ("He is %d cm tall." % height)
print("He is %d kg heavy." % weight)
print("He's got %s eyes and %s hair." % (eyes,hair))
print("printing this %r no matter what.")

inches = 1
centimeters = 1
convert = centimeters * 2.54
print (inches)
print (centimeters)
print ("%d inches equals to %r centimeters." % (inches, convert)) # %r prints no matter what

print(round(1.49999))
print(round(1.500000001))