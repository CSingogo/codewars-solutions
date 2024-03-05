'''
Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.
'''

def combat(health, damage):
    diff = health - damage
    if diff >= 0:
        return diff
    else:
        return 0