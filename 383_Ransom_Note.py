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

def canConstruct(ransomNote, magazine):
    list1 = []
    for i in range(0,len(ransomNote)):
        if i%2 == 0:
            list1.append(ransomNote[i:i+2])
        elif i%2 != 0 :
            list1.append(ransomNote[i:i+2])

    print(list1)
    
    for k in list1:
        # print(k,magazine)
        if k in magazine:
            return True
    else:
        return False





print(canConstruct(ransomNote,magazine))