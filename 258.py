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

# num = 0
# Output: 0

# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

def addDigits(num): 
    sum1 = 0
    if len(str(num)) == 1:
        return num
    
    elif len(sum1)>=2:
        if len(str(num)) <=2 :
            for i in str(num):
                sum1 = sum1+int(i)


print(addDigits(num))    