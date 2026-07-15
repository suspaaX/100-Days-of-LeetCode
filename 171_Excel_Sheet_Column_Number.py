'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
'''

columnTitle = "AB"
Output: 28

columnTitle = "W"
Output: 1

def titleToNumber(columnTitle):
    result = 0
    ltr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i,j in enumerate(ltr):
        for k in columnTitle:
            if len(columnTitle) == 1:
                if k == j:
                    return i+1

            elif len(columnTitle) > 1:
                m =26*i+(i+1)


        

    # return i+

print(titleToNumber(columnTitle))