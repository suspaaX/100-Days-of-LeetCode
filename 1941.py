'''
1941. Check if All Characters Have Equal Number of Occurrences
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

 

Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

'''

s = "aaabb"
Output: False

# s = "abacbc"
# Output: True



# s = "tveixwaeoezcf"
# Output: False


def areOccurrencesEqual(s):
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1

    lst = []
    for i,j in dict1.items():
        lst.append(j)

    if len(set(lst)) == 1:
        return True
    else:
        return False


print(areOccurrencesEqual(s))
        