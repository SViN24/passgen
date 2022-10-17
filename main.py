#!/usr/bin/python3
import random
import string
import sys

arguments = sys.argv[1:]

length = 8
if "-l" in arguments:
    index_pos = arguments.index("-l")
    #TODO: need to think of a way to make this work better ,it does not reuse characters in the password(random.sample counts)
    #TODO: check for int
    length = int(arguments[index_pos + 1])
    

#initialize combination string
combination = ""

#add various ascii types in string
if "--no-low" not in arguments:
    combination += string.ascii_lowercase
if "--no-high" not in arguments:
    combination += string.ascii_uppercase
if "--no-digit" not in arguments:
    combination += string.digits
if "--no-punk" not in arguments:
    combination += string.punctuation

# error handle
if not combination:
    sys.exit("Sample size is zero, can't make password.")

#separate and sample to create password
temp = random.sample(combination,length)

password = "".join(temp)
print(password)
