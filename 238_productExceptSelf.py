nums = [1,2,3,4]
Output =  [24,12,8,6]

nums = [-1,1,0,-3,3]
Output = [0,0,9,0,0]

nums = [0,0]
output = [0,0]

# nums = [1,1]
# output = [1,1]



def productExceptSelf(nums) :
    import math
    lst2 = []
    for i in range(0,len(nums)):
        lst = []
        for k in nums:
            if k != nums[i]:
                lst.append(k)
        lst2.append(lst)
    
    result = []
    for k in lst2:
        res = math.prod(k)
        result.append(res)

    return result


print(productExceptSelf(nums))