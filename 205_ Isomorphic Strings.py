'''

Code
Testcase
Testcase
Test Result
205. Isomorphic Strings
Easy
Topics
premium lock icon
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true
'''



s = "f11"
t = "b23"

# Output: False


s = "paper"
t = "title"

Output: True




s = "a"
t = "a"

Output: True



# s = "ab"
# t = "ab"

# Output: True

# s = "badc"
# t = "baba"

# Output: False


# s = "ab"
# t = "aa"

# Output: False
s = "egg"
t = "add"

Output: True 

def isIsomorphic(s,t) :


    # if len(set(s)) == len(set(t)):
    #     return True
    
    # elif len(s) > 2 and len(t) > 2:

    #     dict1 = {}
    #     for i,j in zip((s),(t)):
    #         dict1.update({i:j})
    #     # print(dict1)

    #     new_wd = ''
    #     for i in s:
    #         # print(i,dict1)
    #         val = dict1.get(i)
    #         if i in dict1 and val not in i:
    #             new_wd = new_wd+val

    #         # elif i in dict1 :
    #         #     new_wd = new_wd+val

    #     print(new_wd)

    #     if new_wd == t:
    #         return True
    #     else:
    #         return False

    # else:
    #     return False

    dict1 = {}
    for i in zip(s,t):
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1

    print(dict1)

        






print(isIsomorphic(s,t))
        