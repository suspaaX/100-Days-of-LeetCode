
'''

680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''



s = "abc"
Output =  False

# s = "abca"
# Output: False


# s = "bebeb"
# Output =  True

# s = "cbbcc"
# Output =  True

s = "aba"
Output =  True

def validPalindrome(s) :

    lst = []
    for i in range(0,len(s)):
        for k in s:
            lst.append()


    pali = s[::-1]
    if s == pali:
        return True

    else:
        return False
        
print((validPalindrome(s)))