'''
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.
 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''
num1 = "456" 
num2 = "77"
Output: "533"


# num1 = "0"
# num2 = "0"
# Output: "0"

# num1 = "111"
# num2 = "123"
# Output: "234"

num1 = "45" 
num2 = "771"
Output: "533"



def addStrings(num1, num2):
    if len(num1) > len(num2):
        nw_num2 = num2.zfill(len(num1))
        x = (nw_num2,num1)

    elif len(num1) < len(num2):
        nw_num1 =  num1.zfill(len(num2))
        y = (nw_num1,num2)
    
    print(y)



print(addStrings(num1, num2))       
