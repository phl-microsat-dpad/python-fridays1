# Reference: http://www.tutorialspoint.com/python/index.htm
#            http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python

###########################################################
# Two modes: Interactive and Script Programming
###########################################################

###########################################################
# Identifiers
#       - names for variables, functions, class, modules, etc. Starts with A-Z, a-z or underscore
#       - (convention) Class names start with uppercase letter
#       - (convention) Single leading underscore means private
#       - (convention) Two leading underscores mean strongly private
#       - (convention) Two leading underscores also ending with two underscores is language defined
###########################################################

###########################################################
# No Brackets! Just Indentations
###########################################################

if True:
    # Lines with similar number of spaces are called blocks
    print "Hello"
    print "World"

else:
    print "False"


###########################################################
# Multi-Line Statements - use '\'
###########################################################

x = 1 + \
    2 + \
    3

print "Result of multi-line statement: %s" % x


###########################################################
# Quotations: '', "", or """"""
###########################################################

mutilinestring = """
This is a multiline string
asdfasdfasdo
asdfasdfasdf
"""

print mutilinestring


###########################################################
# Variables
###########################################################

x1 = 100        # This is an integer
x2 = 100.0      # This is a float
x3 = "String"   # This is a string

print x1
print x2
print x3


######################
# Multiple Assignment
######################

m1 = m2 = m3 = 1

print m1
print m2
print m3


##########################
# Standard Data Types
#   - Numbers
#   - Strings
#   - List
#   - Tuple
#   - Dictionary
##########################

# LISTS
list1 = ["Test", 1234, 1234.5, "Hello world"]
print list1
print list1[0]
print list1[1:3]
print list1[2:]

# TUPLES - "Read-only lists, cannot be updated"
list1 = ("Test", 1234, 1234.5, "Hello world")
print list1
print list1[0]
print list1[1:3]
print list1[2:]

# DICTIONARIES
dict1 = {}
dict1['first'] = "This is the first element"
dict1[2] = "This is the second element"
print dict1
print dict1.keys()


###########################################################
# DATA TYPE CONVERSIONS
# int(), long(), float(), str()
###########################################################


###########################################################
# OPERATORS
# +, -, *, /, %, **(power), //(floor division)
###########################################################


###########################################################
# Assignment operators
# =, +=, *=, etc.
###########################################################


###########################################################
# Logical Operators
# and, or, not
###########################################################


###########################################################
# Membership Operators
# in, not in
###########################################################


###########################################################
# Identity Operators
# is, is not
###########################################################

###########################################################
# The IF statement
###########################################################

if x is None:
    print "X is None"
elif x == 1:
    print "X is 1"
else:
    print "X is neither None nor 1"


###########################################################
# LOOPS
###########################################################

i = 0
while i < 5:
    print i
    i += 1

for i in xrange(0, 10):
    print i


rows = ["Item 1", "Item 2", "Item 3"]
for row in rows:
    print row


###########################################################
# FUNCTION DEFINITIONS
###########################################################
def firstfunction(param1, params=None, name="default name"):
    "This is my first function"
    print "I want to print %s" % param1
    return True

firstfunction("THIS PRINTABLE STRING", name="Benjie")


###########################################################
# MODULE
###########################################################
from sample_module import print_name
print_name("Benjie")

# or...

import sample_module
sample_module.print_name("Jiao")


# MORE ON MODULES NEXT SESSION!
