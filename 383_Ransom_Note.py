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

ransomNote = "abaa"
magazine = "baaa"
Output: True

ransomNote = "aa"
magazine = "ab"
Output: False

# ransomNote = "bg"
# magazine =  "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
# Output = True

# ransomNote = "az"
# magazine =  "ab"
# Output = True

# ransomNote = "fihjjjjei"
# magazine =  "hjibagacbhadfaefdjaeaebgi"
# Output = False


def canConstruct(ransomNote, magazine):
    dict1 = {}
    set1 = set(ransomNote)
    for st1 in set1:
        n1 = ransomNote.count(st1)
        dict1.update({st1:n1})


    dict2 = {}
    set2 = set(magazine)
    for st2 in set2:
        n2 = magazine.count(st2)
        dict2.update({st2:n2})
 
    for  m,n in dict1.items():
        if m in dict2 and n <= dict1.get(m):
            return False
        else:
            return True

print(canConstruct(ransomNote,magazine))