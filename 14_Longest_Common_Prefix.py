'''

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
strs = ["flower","flow","flight"]
Output = "fl"



def longestCommonPrefix(strs):
    result = []
    cmn = [i for i in strs[0]]


    for ltr in strs[1:len(strs)]:
        print(ltr,cmn)
        if ltr in cmn:
            result.append(ltr)

    str1 = ""
    for i in result:
        str1 = str1+i
    

    return str1

print(longestCommonPrefix(strs))      