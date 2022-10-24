# passgen
a password generator

#### Usage
Requires **Python3**

to run simply do 
`./passgen.py`

it also accepts the following command line arguments
```
-l          Control length(Max=256,default=8)

--no-low    No lowercase characters
--no-up     No uppercase characters
--no-digit  No digits
--no-punk   No punctuation
```

for example to generate a password with legth of 16 and no punctuation/uppercase)

```./passgen.py --no-punk -l 16 --no-up```
