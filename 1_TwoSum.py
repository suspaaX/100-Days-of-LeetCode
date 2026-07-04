'''

1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

nums = [3,2,4]
target = 6
Output =  [1,2]


nums = [3,2,3]
target  = 6
Output = [0,2]

nums  = [2,7,11,15]
target = 9
Output = [0,1]

# nums = [3,3]
# target  = 6   
# Output = [0,1]

def twoSum(nums,target) :
    lst1 = []
    for i in range(0,len(nums)):
        for k2 in nums[i+1:len(nums)]:
            x = (nums[i],k2)
            lst1.append(x)



    for sum1 in lst1:
        if sum(sum1) == target:
            correct = sum1

    rst = []
    rst2 = []
    for k in correct:
        if k in nums:
            x = nums.index(k)
            x2 = nums.index(k,1)
    rst.append(x)
    rst2.append(x2)
    return rst,rst2


print(twoSum(nums,target))

















