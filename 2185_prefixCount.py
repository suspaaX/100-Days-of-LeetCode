'''
2185. Counting Words With a Given Prefix

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
'''

words = ["pay","attention","practice","attend"]
pref = "at"
Output: 2

words = ["leetcode","win","loops","success"]
pref = "code"
Output: 0

def prefixCount(words,pref) :
    lst = []
    for i,j in enumerate(words):
        if pref[0:len(pref)] in j[0:len(pref)]:
            lst.append(i)
            
    return len(lst)

print(prefixCount(words,pref))