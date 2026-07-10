'''
1844. Replace All Digits with Characters
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

You must perform an operation shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with the result of the shift(s[i-1], s[i]) operation.

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

Note that shift(c, x) is not a preloaded function, but an operation to be implemented as part of the solution.

 

Example 1:

Input: s = "a1c1e1"
Output: "abcdef"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
Example 2:

Input: s = "a1b2c3d4e"
Output: "abbdcfdhe"
Explanation: The digits are replaced as follows:
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'

'''

s = "a1c1e1"
Output =  "abcdef"
# print(len(Output))

# s = "a1b2c3d4e"
# Output =  "abbdcfdhe"
# print(len(Output))

s = "v0g6s4d"
Output =  "vvgmswd"
# print(Output)


def replaceDigits(s):
    lst = []
    for i in range(0,len(s)):
        for k in s[i+1:len(s)]:
            print(k)
        # print(m)



print(replaceDigits(s))
        





























'''    idx = []
    lst1 = []
    ch = str()
    for i in range(0,len(s)):
        if i%2 != 0:
            idx.append(i)
        elif i%2 == 0:
            lst1.append(s[i])

    lst2 = []
    l = 'abcdefghijklmnopqrstuvwxyz'   
    for i in range(0,len(l)):
        for k in idx:
            if k == i:
                lst2.append(l[i])

    if len(lst1) != len(lst2):
        lst2.append(' ')
    elif len(lst2) != len(lst1):
        lst1.append(' ')
        
    for l1,l2 in zip(lst1,lst2):
        ch = ch+l1+l2
        x = ch.replace(' ','')
  
    return x
'''