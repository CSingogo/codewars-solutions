#left2

"""

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'

"""

#solution

def left2(str):
  
  if len(str) <= 2:
    return str
  else:
    two = str[:2]
    rest = str[2:]
    return rest + two
