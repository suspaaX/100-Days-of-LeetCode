'''
2710. Remove Trailing Zeros From a String

Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

 

Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".
 
'''

num = "51230100"
Output =  "512301"

# num = "123"
# Output =  "123"

def removeTrailingZeros(num):
    if '0' not in  num[0:len(num)]:
        return num
    
    elif '0' in num:
        k = num[::-1]
        int1 = str(int(k))
        int1_rev = int1[::-1]
        return int1_rev

print(removeTrailingZeros(num)) 