formatter = "%r, %r, %r, %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("你好", "two", "three", "four"))
print (formatter % (True, False, True, False))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "This is a multiple lines.",
    "And the purpose is.",
    "But is did not sing.",
    "How it works."
))