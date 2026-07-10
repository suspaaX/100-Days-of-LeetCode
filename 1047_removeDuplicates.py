'''
1047. Remove All Adjacent Duplicates In String

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
'''

s = "abbaca"
Output =  "ca"


def removeDuplicates(s):
    for i in s:
        k = 2*i
        print(k,s)
        if k in s[0:len(s)]:
            m = s.replace(k,'')
            if k in m:
                n = m.replace(k,'')
                return n



print(removeDuplicates(s))