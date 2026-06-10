'''
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
'''

sentence = "thequickbrownfoxjumpsoverthelazydog"
Output =  True
# Explanation: sentence contains at least one of every letter of the English alphabet.

# sentence = "leetcode"
# Output =  False

def checkIfPangram(sentence) :
    list1 = []
    for i in sentence:
        list1.append(i)

    x =set(list1)
    x2 = (list(x))
    x2.sort()

    x3 = []
    for i in range(97,123):
        x3.append(chr(i))
    x3.sort()


    if x2 == x3:
        return True
    
    else: 
        return False


print(checkIfPangram(sentence))