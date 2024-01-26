'''


Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True

'''

def near_ten(num):
  if  (num + 2) % 10 == 0 or (num - 2) % 10 == 0:
    return True
  elif (num + 1) % 10 == 0 or (num - 1) % 10 == 0:
    return True
  elif num % 10 == 0:
    return True
  else:
    return False