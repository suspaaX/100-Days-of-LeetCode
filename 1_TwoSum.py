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

# nums = [3,3]
# target  = 6   
# Output = [0,1]

# nums = [3,2,3]
# target  = 6
# Output = [0,1]

nums  = [2,7,11,15]
target = 9
Output = [0,1]

def twoSum(nums,target) :
    list1 = []
    for i in range(0,len(nums)):
        list2 = []
        for k in nums:
            list2.append([k,nums[i+1]])
        print(list2)
            # if k != nums[i]:
            #     print(k,nums[i])
        #         list2.append()
        # print(list2)


        
    


print(twoSum(nums,target))






















    # nums2 = [i for i in nums if i<target]

    # answer2 = []
    # if len(nums2) == 2 and sum(nums2) == target:
    #     for i,k in enumerate(nums2):
    #         answer2.append(i)
        
    #     return answer2

    # elif len(nums2) >2:

    #     prs1 = []
        # for i,j in enumerate(nums):
        #     prs2 = []
        #     for k in nums[i:len(nums)]:
        #         prs2.append(nums[i:i+2])
        #     prs1.append(prs2)
        # print(prs1)
            
        # for i in range(0,len(prs)):
        #     if sum(prs[i]) == target:
        #         result = prs[i]
        #         print(result)

        # answer = []
        # for l,m in enumerate(result):
        #     if m in nums:
        #         idx = nums.index(m)
        #         answer.append(idx)
        # return answer