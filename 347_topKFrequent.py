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
nums = [1] 

k = 1

Output = [1]

# nums = [1,2,1,2,1,2,3,1,3,2,3,3,3,3,3]
# k = 2

# Output =  [1,2]


# nums = [1,1,1,2,2,3]
# k = 2

# Output = [1,2]

def topKFrequent(nums,k) :
    if len(nums) == 1:
        return nums
    
    elif len(nums) >1:
        dict1 = {}  
        for i in nums:
            if i in dict1:
                dict1[i] = dict1[i]+1
            else:
                dict1[i] = 1

        lst = []
        for key,val in dict1.items():
            x = val,key
            lst.append(x)

        lst.sort(reverse=True) 

        rslt = []
        for elem in lst[0:k]:
            rslt.append(elem[1])
        return rslt

print(topKFrequent(nums,k)) 

