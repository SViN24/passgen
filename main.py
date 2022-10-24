#!/usr/bin/python3
import random
import string
import sys

arguments = sys.argv[1:]

length = 8

#initialize combination string
combination = ""

#remove various ascii types from sample
if "--no-low" not in arguments:
    combination += string.ascii_lowercase
if "--no-high" not in arguments:
    combination += string.ascii_uppercase
if "--no-digit" not in arguments:
    combination += string.digits
if "--no-punk" not in arguments:
    combination += string.punctuation

if "-l" in arguments:
    index_pos = arguments.index("-l")
    
    #Check if length value exists (-1 is for adjustment's sake)
    if index_pos + 1 > len(arguments) - 1:
        sys.exit("No number included")
    #Check if value is interger
    if not arguments[index_pos + 1].isdigit():
        sys.exit("Length needs to be a number")
    #Cast to to interget and store
    length = int(arguments[index_pos + 1])
    
    # interger checks
    if length > 256:
        sys.exit("Length too large (Max is 256)")
    if length <= 0:
        sys.exit("Length value invalid")
    

# error handle
if not combination:
    sys.exit("Sample size is zero, can't make password.")

#separate and sample to create password
temp = random.choices(combination,k = length)

password = "".join(temp)
print(password)
