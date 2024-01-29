'''

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

'''

## soluion

def is_isogram(string):
        
    my_list = list(string)
    upper_list = [letter.upper() for letter in my_list]
    
    if len(upper_list) == 0:
        return True
    
    for i in range(0,len(upper_list)):
        for j in range(i + 1, len(upper_list)):
            if upper_list[i] == upper_list[j]:
                return False
    return True