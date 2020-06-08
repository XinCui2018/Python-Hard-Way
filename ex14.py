# from sys import argv

# script, user_name = argv
# prompt = '> '

# print ("Hi %s, I'm the %s script." % (user_name, script))
# print ("I'd like to ask you a few questions.")
# print ("Do you like me %s?" % user_name)
# likes = input(prompt)

# print ("Where do you live %s?" % user_name)
# lives = input(prompt)

# print ("What kind of computer do you have?")
# computer = input(prompt)

# print ("""
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is. 
# And you have a %r computer. Nice.
# """ % (likes, lives, computer))

from sys import argv

script, user_name = argv

prompt = '> '

print ("Hi %s, this is the %s script." %(user_name, script))
print ("Can I ask you some questions?")
print ("Do you like me, %s?" % user_name)
likes = input(prompt)

print ("Where do you live, %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you use?")
computer = input(prompt)

print ("""
Alright, you said %r about liking me.
You live in %r, do not know where that is.
You have a %r computer. It is awesome.
""" % (likes, lives, computer))
