'''
47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

nums = [1,1,2]
Output = [[1,1,2],[1,2,1],[2,1,1]]

nums = [1,2,3]
Output =  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permuteUnique(nums) :
    result = []
    for i in range(0,len(nums)):
        for k in nums:
            # x = list(k)
            print(k)
    #         y = [i for i in nums[i+1:len(nums)]]
    #         m = x+y
    #         result.append(m)

    # print(result)
permuteUnique(nums) 