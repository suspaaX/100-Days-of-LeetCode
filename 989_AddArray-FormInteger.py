'''
989. Add to Array-Form of Integer
Easy
Topics
premium lock icon
Companies
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

'''



# num = [2,1,5]
# k = 806
# # Explanation: 215 + 806 = 1021
# Output =  [1,0,2,1]

# num = [2,7,4]
# k = 181
# Output =  [4,5,5]
# Explanation: 274 + 181 = 455

num = [1,2,0,0]
k = 34
Output = [1,2,3,4]
# Explanation: 1200 + 34 = 1234

def addToArrayForm(num,k) :

    num1 = str(num)
    set1 = set(num)
    numstr1 = str(set1)
    print(numstr1)

    nums = ''
    for i in range(0,len(num)):
        pass








print(addToArrayForm(num,k))
        
