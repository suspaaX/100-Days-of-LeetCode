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


# s = "ab"
# t = "baab"

# Output: True

# s = "abc"
# t = "ahbgdc"
# Output =  True

s= ""
t = "ahbgdc"
Output =  True


def isSubsequence(s,t): 

    if s is str():
        return True

    else :
        match = [i for i in s]
        
        chq = []
        for i in t :
            if i in match:
                chq.append(i)
        
        lst1 = []
        for i in range(0,len(chq),len(match)):
            lst1.append(chq[i:i+len(match)])


        if match in lst1:
            return True
        else:
            return False
        

print((isSubsequence(s,t)))