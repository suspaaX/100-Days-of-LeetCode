'''
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''


word1 = "abcd"
word2 = "pq"
Output =  "apbqcd"

# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d


# word1 = "abc"
# word2 = "pqr"
# Output =  "apbqcr"

word1 = 'ab' 
word2 = 'pqrs'
merged = 'apbqrs'


def mergeAlternately(word1,word2):
    merged_string = ''
    if len(word1) == len(word2):
        for i,j in zip(word1,word2):
            merged_string = merged_string+i+j

    elif len(word1)>len(word2):
        result2 = word2.ljust(len(word1),'0')
        for i,j in zip(word1,result2):
            merged_string = merged_string+i+j
        x = merged_string.replace('0','')
        return x



    elif len(word1)<len(word2):
        result1 = word1.ljust(len(word2),'0')
        for i,j in zip(result1,word2):
            merged_string = merged_string+i+j
        y = merged_string.replace('0','')
        return y

    return(merged_string)
        
print(mergeAlternately(word1,word2))