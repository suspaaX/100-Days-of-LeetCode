'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

'''

# num1 = "2"
# num2 = "3"
# Output: "6"

num1 = "123"
num2 = "456"
Output: "56088"



def multiply(num1,num2):
    
    for i,j in zip(num1,num2):
        c = (int(i)*int(j))
        print(c)


multiply(num1,num2)    