'''
1556. Thousand Separator
Easy
Topics
premium lock icon
Companies
Hint
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"

'''
n = 1234
Output =  "1.234"

n = 9875679
Output =  "987"

def thousandSeparator(n):
    n1 = str(n)
    k = (n1[-4:-1])
    print(k)
    m = n1.split(n1[0:2],'.')
    print(m)

thousandSeparator(n)