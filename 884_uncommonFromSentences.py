''''
884. Uncommon Words from Two Sentences
Easy
Topics
premium lock icon
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

'''


s1 = "apple apple" 
s2 = "banana"

Output = ["banana"]


# s1 = "this apple is sweet"
# s2 = "this apple is sour"

# Output = ["sweet","sour"]




def uncommonFromSentences(s1,s2) :
    uncommon_words = []
    s1_dup = s1.split(' ')
    s2_dup = s2.split(' ')
    sum1 = s1_dup+s2_dup

    dict1 = {}
    for i in sum1:
        x =sum1.count(i)
        dict1.update({i:x})

   
    rslt = []
    for key,val in dict1.items():  
        x = key,val
        rslt.append(x)

    for i in rslt:
        if i[1] == 1:
            uncommon_words.append(i[0])
    return (uncommon_words)

print((uncommonFromSentences(s1,s2)))