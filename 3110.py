'''
3110. Score of a String
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:


Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.


'''

s = "hello"

Output: 13

# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
# So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# s = "zaz"

# Output: 50

def scoreOfString(s):
    lst = []
    for j in (s):
        lst.append(ord(j))


    lst2 = []
    for k,l in enumerate(s):
        elem = lst[k:k+2]
        if len(elem) == 2:
            d = elem[0]-elem[1]
            if d >=0:
                lst2.append(d)
            if d < 0 :
                lst2.append(d*(-1))
    
    return sum(lst2)

print(scoreOfString(s))    





