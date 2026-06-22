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
    answer = []
    dict1 = dict()
    for i in nums:
        x =nums.count(i)
        dict1.update({i:x})

    for key,val in dict1.items():

        if val == k:
            answer.append(key)

        elif val > k:
            answer.append(key)

    return answer
        
print(topKFrequent(nums,k)) 

