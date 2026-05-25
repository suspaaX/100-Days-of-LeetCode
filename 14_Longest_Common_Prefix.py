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
    for word in strs:
        for ltr in word:
            if ltr[0:len(ltr)] in word:
                result.append(ltr[0:len(ltr)])
    print(result)


print(longestCommonPrefix(strs))      