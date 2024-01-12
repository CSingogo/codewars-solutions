"""

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

"""

#solution

def front_back(s):
    if len(s) == 0:
        return ""
    
    first = s[0]
    last = s[-1]

    if len(s) == 2:
        return last + first
    elif len(s) == 1:
        return first
    else:
        mid = s[1:len(s)-1]
        return last + mid + first
