'''258. Add Digits
Easy
Topics
premium lock icon
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
'''

num = 38
Output =  2

# num = 10
# Output: 0

# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# num = 9
# output = 9

def addDigits(num):

    # num1 = str(num)
    
    # if len(num1) != 1:
    #     num2 = [int(i) for i in str(num)]
    #     sum1 = sum(num2)
    #     num = sum1
        
    # else:
    #     return num
    
    # return sum1
    count = 0
    num1 = str(num)
    while len(num1) ==  1:
        num2 = [int(i) for i in str(num)]
        sum1 = sum(num2)
        sum1 = num
        count = count+1

    return num
    

print(addDigits(num))    