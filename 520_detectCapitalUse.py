'''
520. Detect Capital
Easy
Topics
premium lock icon
Companies
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false

'''
word = "Fla"
Output = False

word = "USA"
Output = True

word = 'g'
output = False

def detectCapitalUse(word) :
    small  = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    f = word[0]
    s = word[1:len(word)]

    if word[0] in cap and set(s).issubset(set(cap)):
        return True
    elif word[0] in cap and set(s).issubset(set(small)):
        return True
    elif word[0] in small and set(s).issubset(set(small)):
        return True
    else:
        return False
    

print(detectCapitalUse(word))