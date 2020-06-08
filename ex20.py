# it means from the module sys,
# import the function or parameter argv.
from sys import argv

script, input_file = argv
# define a function
# the function name is print_all
def print_all(f):
    # the variable in the function is f in this case, which means a file
    # do not forget to put a colon : at the end of the parenthesis
    # print function needs (). f.read() means you wanna read the content in f
    print (f.read())

# define another function called rewind
def rewind(f):
    # file.seek() sets the file's current position at the offset
    # 0 in this case means the first position of the read/write pointer within the file.
    f.seek(0)
# Each time you do f.seek(0), you are moving to the start of the file.
# Each time you do f.readline(), you are reading a line from the file and moving
# the read head to right after the \n that ends that file.
# The seek() function is dealing in bytes, not lines.  
def print_a_line(line_count, f):
    print (line_count, f.readline())
# What is +=?
# This means X = X + Y is the same as X += Y
current_file = open(input_file)

print ("First, let's print the whole file: \n")

print_all (current_file)

print ("Now, let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

# Inside readline() is code that scans each byte of the file
# until it finds a \n character,
# then stops reading the file to return what is found so far. 
# The file f is responsible for maintaining the current position
# in the file after each readline() call, so that it will keep reading each line.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)