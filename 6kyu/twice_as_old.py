"""

Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

"""

#solution

def twice_as_old(dad, son):
    count = 0
    
    while dad != 2 * son:
        count+= 1
        dad+= 1
        son+= 1
    return count