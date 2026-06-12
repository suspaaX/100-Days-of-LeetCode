'''
557. Reverse Words in a String III
Easy
Topics
premium lock icon
Companies
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

'''

s = "Let's take LeetCode contest"
Output =  "s'teL ekat edoCteeL tsetnoc"


def reverseWords(s) :
    x = s.split()

    str1 = ''
    for i in x:
        rvsr = i[::-1]
        str1 = str1+rvsr+str(' ')

    return str1[0:len(str1)-1]

print(reverseWords(s))