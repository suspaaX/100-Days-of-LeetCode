'''
1668. Maximum Repeating Substring
Easy
Topics
premium lock icon
Companies
Hint
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc". 
'''
sequence = "ababc"
word = "ba"
Output: 1

sequence = "ababc" 
word = "ab"
Output: 2

sequence = "ababc"
word = "ac"
Output: 0





# "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
sequence = "aaaba aaaba aabaaaabaaaabaaaabaaaaba"
word = "aaaba"
Output: 5



def maxRepeating(sequence,word):
    lst = []
    for i,j in enumerate(sequence):
        if word in sequence:
            lst.append(i)
    print(lst)























        

print(maxRepeating(sequence,word))