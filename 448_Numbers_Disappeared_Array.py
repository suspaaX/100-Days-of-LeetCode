'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

'''


# nums = [1,1]
# Output =  [2]

# nums = [2,2]
# Output =  [1]


# nums = [3,4]
# Output =  [1,2]

# nums = [1,1,2,2]
# output = [3,4]

nums = [4,3,2,7,8,2,3,1]
Output =  [5,6]



def findDisappearedNumbers(nums):
    nums.sort()
    dis_num = []
    for i in range(1,nums[-1]):
        dis_num.append(i)
    print(nums,dis_num)
        



print(findDisappearedNumbers(nums))