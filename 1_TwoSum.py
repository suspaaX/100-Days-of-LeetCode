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


# nums = [3,2,4]
# target  = 7
# Output = [0,2]


nums = [3,3]
target  = 6   
Output = [0,1]

# nums  = [2,7,11,15]
# target = 9
# Output = [0,1]

def twoSum(nums,target) :


    lst1 = []
    for i in range(0,len(nums)):
        for k2 in nums[i+1:len(nums)]:
            x = [nums[i],k2]
            if sum(x) == target:
                lst1.append(x)

    lst2 = []
    for n in lst1[0]:
        k = nums.index(n)
        lst2.append(k)

    return lst2









print(twoSum(nums,target))

















