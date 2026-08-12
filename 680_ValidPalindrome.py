
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

s = "cbbcc"
Output =  True

# s = "aba"
# Output =  True

def validPalindrome(s) :
    m = s[::-1]
    
    if s == m:
        return True
    elif s!=m:
        lst2 = []
        for i,j in enumerate(s):
            m =i,j
            lst2.append(m)
        print(lst2)

        lst  = []
        str1 = ''
        for l in lst2:
            # print(l[1])
            if l[0] not in lst2[0]:
                str1 = str1+l[1]
                lst.append(str1)
        print(lst)   

        
print(validPalindrome(s))