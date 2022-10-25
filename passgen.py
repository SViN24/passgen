#!/usr/bin/python3
"""
    passgen - a password generator
    Copyright (C) 2022  SViN <svin@dismail.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import random
import string
import sys
import argparse

#initialize combination string
combination = ""

#argument parsing starts here
parser = argparse.ArgumentParser(description = "passgen - a simple password generator by SViN <svin@dismail.de>")
parser.add_argument("--no-low", help="No lowercase characters"
                    ,action="store_true")
parser.add_argument("--no-up", help="No uppercase characters"
                    ,action="store_true")
parser.add_argument("--no-digit", help="No digits"
                    ,action="store_true")
parser.add_argument("--no-punk", help="No punctuation"
                    ,action="store_true")
parser.add_argument("-l", "--length", default=8,
                    type=int, help="Change size of the output(Max is 256)")
args = parser.parse_args()

#removal/addition of strings in the sum
if not args.no_low:
    combination += string.ascii_lowercase  
if not args.no_up:
    combination += string.ascii_uppercase
if not args.no_digit:
    combination += string.digits
if not args.no_punk:
    combination += string.punctuation

# length handling
if args.length:
    length = args.length
     
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
