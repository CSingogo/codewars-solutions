'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

'''

def abbrev_name(name):
    name = name.upper()
    listt = list()
    listt = name.split(' ')
    first = listt[0]
    second = listt[1]
    return first[0] + '.' + second[0]