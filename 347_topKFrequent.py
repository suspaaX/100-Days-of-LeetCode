'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

'''
# nums = [1] 

# k = 1

# Output = [1]

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

Output =  [1,2]


# nums = [1,1,1,2,2,3]
# k = 2

# Output = [1,2]

def topKFrequent(nums,k) :
    dict1 = {}
    for i in nums:
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1

    

    # lst = []
    # for key,val in dict1.items():
        

print(topKFrequent(nums,k)) 

