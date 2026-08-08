'''
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
'''




# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".

pattern = "abba"
s = "dog cat cat fish"

Output =  False

# pattern = "aaaa"
# s = "dog cat cat dog"

# Output = False

# pattern = "aba"
# s ="cat cat cat dog"       
# Output = False

# pattern = "aba"
# s = "dog cat cat"    
# Output = False

pattern = "abba"
s = "dog cat cat dog"
Output =  True

pattern = "abc"
s = "b c a"
Output =  True


def wordPattern(pattern, s) :
    x = s.split()

    dict1 = {}
    for i in x:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1

    print(dict1)

(wordPattern(pattern, s))
        