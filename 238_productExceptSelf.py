nums = [1,2,3,4]
Output =  [24,12,8,6]


def productExceptSelf(nums) :
    product = []
    mul1 = 1
    for i in range(0,len(nums)):
        print(nums[i],nums)
        if nums[i] in nums:
            x = nums.pop(i)
            product.append(x)
    print(product)
                

productExceptSelf(nums)