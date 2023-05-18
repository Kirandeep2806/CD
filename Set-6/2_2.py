# Without Scanner

import re

pattern = r"^[_a-z][a-z0-9_]*$"
if re.fullmatch(pattern, input("Enter a string : "), flags=re.I):
    print("Valid Identifier")
else:
    print("Invalid Identifier")
