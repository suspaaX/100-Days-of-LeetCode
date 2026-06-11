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

    rev = []
    # result = ''
    x = s.split()
    for i in x:
        j = i[::-1]
        rev.append(j)
        "#".join(rev)

    # for i in rev:
    #     result = result + i

    # return str().join(result)
    return rev

print(reverseWords(s))