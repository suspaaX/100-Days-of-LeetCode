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

# ransomNote = "bg"
# magazine =  "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
# Output = True

# ransomNote = "az"
# magazine =  "ab"
# Output = True

# ransomNote = "fihjjjjei"
# magazine =  "hjibagacbhadfaefdjaeaebgi"
# Output = False

# ransomNote = "aakkk"
# magazine = "ab"
# Output = False

def canConstruct(ransomNote, magazine):
    dict1 = {}
    for i in ransomNote:
        if i in dict1:
            dict1[i] = dict1[i] +1
        else:
            dict1[i] = 1

    dict2 = {}
    for k in magazine:
        if k in dict2:
            dict2[k] =dict2[k]+1
        else:
            dict2[k] =1

    lst1 = []
    for key,val in dict1.items():
        if key in dict2 and val<=dict2.get(key):
            lst1.append(True)
        else:
            lst1.append(False)

    if False in lst1:
        return False
    else:
        return True


print(canConstruct(ransomNote,magazine))    