'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
nums =[3,3,4]
Output =  3

# nums = [3,2,3]
# Output = 3

nums = [2,2,1,1,1,2,2]
Output =  2



def majorityElement(nums) :
    dict1 = {}
    for i in nums:
        y = nums.count(i)
        dict1.update({i:y})

    lst1 = []
    for key,val in dict1.items():
        x = key,val
        print(x)
        

    

print(majorityElement(nums))