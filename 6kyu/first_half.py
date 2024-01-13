# FIRST HALF

"""

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

"""

#solution

first_half = lambda str : str[:len(str) / 2]
  
