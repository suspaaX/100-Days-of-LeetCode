
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
# Output: True

s = "aba"
Output =  True

s = "bebeb"
Output =  True

s = "cbbcc"
Output =  True


def validPalindrome(s) :
    sd = [i for i in s]

    if s[:] == s[::-1]:
        return True

    elif s[:] != s[::-1]:
        lst = []
        skip = 0
        str1 = ''
        for i in range(0,len(s)):
            if i != skip:
                str1= str1+s[i]
                lst.append(str1)
                # skip = skip+1


        print(lst)
                


            


        # for i in lst:
        #     if i == i[::-1]:
        #         return True
        # else:
        #     return False

        
print(validPalindrome(s))