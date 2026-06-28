nums = [1,2,3,4]
Output =  [24,12,8,6]

# nums = [-1,1,0,-3,3]
# Output = [0,0,9,0,0]

# nums = [0,0]
# output = [0,0]

# nums = [1,1]
# output = [1,1]



def productExceptSelf(nums) :
    list1 = []

    for i in range(0,len(nums)):
        mul = 1
        for k in nums:
            if k  !=  nums[i]:
                print(k)
    #             mul = mul*k
    #     list1.append(mul)

    # return list1

print(productExceptSelf(nums))