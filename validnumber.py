
import re

pattern = re.compile(r'[7-9]\d{9}$')
number = input()

if pattern.match(number):
    print('Valid number')
else:
    print('invalid number')