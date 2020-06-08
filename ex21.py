def add(a, b):
    print ("Adding %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print ("Subtracting %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print ("Multiplying %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print ("Dividing %d / %d" % (a, b))
    return a / b

print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print ("That becomes: ", what, "Can you do it by hands?")

def something (c,d):
    print ("What is %r and %r"% (c,d))
    return c**d
result = something(4, 3)

# print(result)
print (something(result, add(age, subtract(height, weight))))


def calculation (a, b, c, d):
    print("what is %r, %r, %r, and %r" %(a, b, c, d))
    return a + b/c - d
a = 24
b = 34
c =100
d = 1023
result1 = calculation(a, b, c, d)
print(result1)