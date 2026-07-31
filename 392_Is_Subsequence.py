'''
392. Is Subsequence
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''





# s = "axc"
# t = "ahbgdc"
# Output: False


s = "ab"
t = "baab"

Output: True

# s = "abc"
# t = "ahbgdc"
# Output =  True

# s= ""
# t = "ahbgdc"
# Output =  True

# s = "acb"
# t = "ahbgdc"
# output = False

s = "b"
t = "c"
output = False


def isSubsequence(s,t): 

    ltr = str()
    for i in t:
        if i in s:
            ltr = ltr+i

    if ltr in s:
        return True
    else:
        return False


        

print((isSubsequence(s,t)))