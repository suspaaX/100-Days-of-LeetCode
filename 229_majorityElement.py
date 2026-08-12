'''
229. Majority Element II
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

'''
nums = [3,2,3]
Output = [3]

# nums = [1,2]
# Output = [1,2]

# nums = [1]
# Output = [1]

def majorityElement(nums):
    sz = len(nums)/3
    dict1 = {}
    for i in nums:
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1

        result = []
        for key,val in dict1.items():
            if val>sz:
                result.append(key)
    
    return result

print(majorityElement(nums))