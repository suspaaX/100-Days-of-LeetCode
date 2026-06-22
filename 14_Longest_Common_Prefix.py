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
    chk = [i for i in strs[0]]
    x = strs[0][0],strs[1][0],strs[2][0]
    if (chk[0] == x):
        result.append(chk[0])
    print(result)





print(longestCommonPrefix(strs))      