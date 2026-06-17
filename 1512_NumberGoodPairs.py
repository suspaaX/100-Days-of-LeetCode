'''
1512. Number of Good Pairs
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

'''

nums = [1,2,3,1,1,3]
Output: 4

# nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# nums = [1,2,3,4]
# Output: 6

def numIdenticalPairs(nums):
    l2 = []
    for i in range(0,len(nums)):
        x = (nums[i:len(nums)])
        l1 = []
        for k in x:
            l1.append(x[0:2])
    l2.append(l1)

    print(l2)


print(numIdenticalPairs(nums))