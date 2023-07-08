"""
This regular expresion matches a string that contains a number with exactly two decimal places. 
"""

import re

pattern = re.compile(r'^\d+\.\d{2}$')

def match_string(string):
  if pattern.match(string):
    return True
  else:
    return False

print(match_string("1.23")) #True output
print(match_string("1.234")) #False output
