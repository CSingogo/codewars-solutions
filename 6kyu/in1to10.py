"""

Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True

"""
#solution

def in1to10(n, outside_mode):
  if (n >= 1 and n <= 10) and not outside_mode:
    return True
  elif (n <= 1 or n >= 10) and outside_mode:
    return True
  else:
    return False