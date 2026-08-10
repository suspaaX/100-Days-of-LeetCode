'''
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
'''

low = 3
high = 6
Output: 3

# low = 8
# high = 10
# Output = 1

# low = 0
# high = 10
# Output = 5

# low = 800445804
# high = 979430543
# Output = 5


def countOdds(low, high):

    diff  = high+1 - low

    if low%2 == 0 and  diff%2 == 0:
        return (int(diff/2))
    
    elif low%2 == 0 and  diff%2 != 0:
        return (int((diff-1)/2))
    
    elif low%2 != 0 and diff%2 == 0:
        return int((diff)/2)
        
    elif low%2 != 0 and diff%2 != 0:
        return int((diff+1)/2)


print(countOdds(low, high))