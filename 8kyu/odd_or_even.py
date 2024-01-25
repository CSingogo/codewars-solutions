'''

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"

'''

def odd_or_even(arr):
    if arr == []:
        return 'even'
    else:
        sum = 0
        
        for num in arr:
            sum = sum + num
        return 'even' if sum % 2 == 0 else 'odd'