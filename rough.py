# num = [5]

# def all_num(num):
#     for i in range(0,num[0]):
#         yield i

# print(all_num(num))


# num = [1,4,7,9]
# target  = 1

# if target not in num:
#     print('yes')

# else:
#     print('no')

# num = [0,1,3,5]

# num = [0,0,0]

# for i,v in enumerate(num):
#     print(i)


# nums = [1,2,3,4]

# for i in range(len(nums)-1):
#     print(nums[i:i+2])

# num1 = True
# num2 = 6
# print(num1*num2)


# num = {1:2,3:5}

# for i in num :
#     print(num.get(i))
#     print(i)

# str = 'klg'
# x = 'a'

# if x in str:
#     print('yes')

# else:
#     print('no')


# words1 = ["aaa","aaa","aaa","aaa","aaa","aaa"]
# words2 = ["aa","a","aaa","aaaa","aaaaa"]

# x = "a"

# result = []
# for i,j in enumerate(words1):
#     if x in j:
#         result.append(i)

# print(result)


# words = ["apple", "banana", "cherry"]
# longest = max(words, key=len)

# print(longest)

# nums = [2,4,4,3]
# Output = 3

# majority = max(my_dict,key=my_dict.get)
# print(majority)

# my_dict = {}
# for i in nums:
#     x = nums.count(i)
#     my_dict.update({i:x})

#     key=my_dict.get()

# print(key)



# digits = [4,3,2,1]
# x = [digits[-1]+1]
# digits.pop(-1)

# print(digits,x)

# n = [9]

# x = (n[0]+1)
# result = []
# for i in str(x):
#     result.append(int(i))
# print(result)

# digits = [1,3]

# print(digits[-1])

# print(digits[len(digits)-1]+1)

# str1 = str('a')
# str2 = str('z')

# for i in range(65,91):
#     print(chr(i))


# nums = [0,0,0,0,0]
# # n = 0
# # print(len(n))
# # nums.clear()
# # print(nums)

# # nums = [1,2,3,4,5,0]
# nums = [0,0,0,0,0]

# for elem in nums:
#     if nums[elem] == 0:
#         x =  nums.pop(elem)

# print(x[0])
#     # else:
#     #     print(nums)

# nums = 'abbb'

# print(nums[0:2])
# for i in nums:
#     print(i)

#list split

# x =[1,3,4,7,5]

# result = []

# for i in range(0,len(x),2):

#     result.append(x[i:i+2])


# print(result)


# g =  "G()()()()(al)"

# x = g.split("()")

# print(x)

# for i in x:
#     print(i)

# print(x)


# s = ""
# print(s)

# n = [2,4,6,8,10]

# result = []
# for i in n:
#     if i == 4 or 10:
#         result.append(i)

#     print(result)

# num = [1,4,6]


# mul = 1
# for i in num:
#     mul = mul*i

# print(mul)

# num = [0,0]

# num2 = []

# for i in num:
#     num2.append(i)
# print(num2)

# val = 'aa'
# k = 'aaa'


# if val in k:
#     print('yes')
    


# letters = "abcdefghijklmnopqrstuvwxyz"
# for i in range(1,len(letters)+1):
#     k = letters[5]

# print(k)



# x = [2,5,7]

# mul = 1
# for k in x:
#     mul = mul*k

# print(mul)


ops = ["5","2","C","D","+"]

lst1 = []
lst2 = []

for i in ops:
    if i == 'C' :
        lst2.append(i)
    elif i == 'D' :
        lst2.append(i)
    elif i == '+' :
        lst2.append(i)
    else:
        k = int(i)
        lst1.append(k)

