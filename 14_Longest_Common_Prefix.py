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
    cmn = []
    for i in  strs:
        # print(i[0],strs[0][-1])
        print(strs[0][0],i[0])
        if strs[0][0] == i[0]:
            cmn.append(strs[0][0])
    print(cmn)





print(longestCommonPrefix(strs))      