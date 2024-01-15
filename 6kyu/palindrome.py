# palindrome

"""

This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true

"""
#solution

palindrome = lambda str : str.split() == str[::-1].split()

print(palindrome("A man, a plan, a canal: Panama"))
    