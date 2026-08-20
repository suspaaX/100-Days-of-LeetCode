'''
896. Monotonic Array
Easy
Topics
premium lock icon
Companies
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false

'''

nums = [1,2,2,3]
Output =  True

# nums = [1,3,2]
# Output =  False


def isMonotonic(nums):
    new_lst = [i for i in nums]
    new_lst2= [i for i in nums]

    new_lst.sort()
    new_lst2.sort(reverse=True)

    result = []
    if new_lst == nums:
        result.append(True)

    elif new_lst2 == nums:
        result.append(True)

    else:
        result.append(False)
        
    for k in result:
        if True not in result:
            return False
        else:
            return True

print(isMonotonic(nums))