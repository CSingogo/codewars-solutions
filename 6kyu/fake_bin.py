'''

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

'''

def fake_bin(x):
    str = ''
    for i in range(0,len(x)):
        if int(x[i]) < 5:
            str += '0'
        elif int(x[i]) >= 5:
            str += '1'
    return str