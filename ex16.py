# from sys import argv

# script, filename = argv

# print ("We are going to erase %r." % filename)
# print ("If you don't want that, hit CTRL-C (^C).")
# print ("If you do want that, hit RETURN.")

# input("?")

# print ("Opening the file...")
# target = open(filename, 'w')

# print ("Truncating the file. Goodbye!")
# target.truncate()

# print ("Now I am going to ask you for three lines.")

# line1 = input("line 1: ")
# line2 = input("line 2: ")
# line3 = input("line 3: ")

# print ("I am going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# print ("And finally, we close it.")
# target.close()

from sys import argv
script, filename = argv

print ("I am going to open the file %r." % filename)

print ("If you do not want to do that, type CTRL-C")
print ("If you want to do it. Click RETURN")
input ("?")

print ("Open the file.")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I am going to ask you to write 2 lines.")

line1 = input("I am : ")
line2 = input("I come from: ")

print ("I am going to write those 2 lines to the file.")

target.write(line1)
target.write("\n")
target.write(line2)

# txt = open(filename)
# print (txt.read())





