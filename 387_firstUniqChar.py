'''
387. First Unique Character in a String
Easy
Topics
premium lock icon
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1


'''

s = "leetcode"

Output: 0

s = "aabb"

Output = -1

# s = "loveleetcode"

# Output = 2


def firstUniqChar(s):
    dict1 = {}
    for i in  s:
        if i in dict1:
            dict1[i] = dict1[i] +1
        else:
            dict1[i] = 1

    lst = []
    for key,val in dict1.items():
        if val == 1:
            m = s.index(key)
            lst.append(m)
    print(lst)

    if len(lst) >=1:
        return lst[0]
    elif len(lst) == 0:
        return -1
        
print(firstUniqChar(s))