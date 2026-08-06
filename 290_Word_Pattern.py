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

# pattern = "abc"
# s = "b c a"
# Output =  True


def wordPattern(pattern, s) :
    ssplt = s.split()

    dict1 = {}
    for i,j in zip(pattern,ssplt):
        dict1.update({i:j})

    print(dict1)

    # slst1 = []
    # for i in ssplt:
    #     if i in dict1.values():
    #         slst1.append(i)

    
    # sresult = ''
    # for i in slst1:
    #     sresult = sresult+i
    # print(pattern,sresult)

    # if pattern == sresult:
    #     return True
    # else:
    #     return False


(wordPattern(pattern, s))
        