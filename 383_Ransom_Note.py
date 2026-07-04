'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''

ransomNote = "aa"
magazine = "aab"
Output =  True

# ransomNote = "aakkk"
# magazine = "ab"
# Output = False


# ransomNote = "aa"
# magazine = "ab"
# Output: False


# ransomNote = "a"
# magazine = "b"
# Output: False


# ransomNote = "a"
# magazine = "b"
# Output: False

# ransomNote = "abaa"
# magazine = "baaa"
# Output: True

# ransomNote = "aa"
# magazine = "ab"
# Output: False


def canConstruct(ransomNote, magazine):
    k = list(ransomNote)
    k.sort()
    l = list(magazine)
    l.sort()
    
    if set(l).issubset(set(k)):
        return True
    else :
        return False



print(canConstruct(ransomNote,magazine))