'''
1662. Check If Two String Arrays are Equivalent
Easy
Topics
premium lock icon
Companies
Hint
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

'''
word1 = ["ab", "c"]
word2 = ["a", "bc"]
Output =  True


word1 = ["a", "cb"]
word2 = ["ab", "c"]
Output = False


word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
Output: True

def arrayStringsAreEqual(word1,word2) :
    wd1 = ""
    wd2 = ""
    for i in word1:
        wd1 = wd1+i
    
    for k in word2:
        wd2 = wd2+k
        
    if wd1 == wd2:
        return True
    
    else:
        return False

print(arrayStringsAreEqual(word1,word2))