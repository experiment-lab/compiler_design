import re

identifier = input("Enter a identifier : ")

pattern = '^[A-Za-z_][A-Za-z0-9_]*'

if re.search(pattern,identifier):
    print("Valid")
else:
    print("Not valid")
