
'''
283. Move Zeroes
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

nums = [0,1,0,3,12]
Output =  [1,3,12,0,0]

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    new_lst1 = []
    new_lst2 = []
    for i in nums:
        if i != 0:
            new_lst1.append(i)
        else :
            new_lst2.append(i)

    result = new_lst1+new_lst2

    return result

print(moveZeroes(nums))