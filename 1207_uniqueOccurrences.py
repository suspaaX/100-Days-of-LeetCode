'''
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''


arr = [1,2,2,1,1,3]
Output =  True

# arr = [1,2]
# Output =  False

# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output = True

# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

def uniqueOccurrences(arr) :

    dict1 = dict()
    for i in arr:
        x = arr.count(i)
        dict1.update({i:x})
        x = dict1.values()

    result = len(x)-len(set(x))

    if result == 0:
        return True
    elif result > 0:
        return False
        


print(uniqueOccurrences(arr))   