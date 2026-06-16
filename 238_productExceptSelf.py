nums = [1,2,3,4]
Output =  [24,12,8,6]


def productExceptSelf(nums) :
    idx = []
    for i in range(0,len(nums)):
        idx.append(i)

    result = []
    for i in nums:
        nums.pop(1)
    print(nums)

productExceptSelf(nums)