'''
2490. Circular Sentence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of each word in the sentence is equal to the first character of its next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

Example 1:

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.
Example 2:

Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.
Example 3:

Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.
 
'''

sentence = "Leetcode is cool"
Output = False

# sentence = "leetcode exercises sound delightful"
# Output: True
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.



sentence = "leetcode"
Output: True
# Explanation: The words in sentence are ["eetcode"].
# - eetcode's last character is equal to eetcode's first character.
# The sentence is circular.
# "

# sentence = 'leetcode exercises sound delightful'
# Output: True
# Explanation: The words in sentence are ["Leetcode", "is", "cool"].
# - Leetcode's last character is not equal to is's first character.
# The sentence is not circular.

# sentence =  "ldQBylHEGvGRjNmwudJoFDAxKnDWYEJxJQCbfqscXvTpENcbruhYFWRtmGNMAWLCpgPtFsJupyREAMyizsIEWiSdHaByXjtYDjrKAZRHaPeKKQjYzigWzRwQwrRvOWyrJztubqgTI LFZvzZCevRaCsOrooUyodWmhBradcVrOemxMoDmZChaQafsdMW WfpCxGbbBuQWYqiBfRygxfoFsypNrqYpjPzmerTjiOXhGSxNCOinHvMdFUwfLotWehtFnrcIuOBlTVVfVyCHZxCNifuCTdpFwYkIMjEaATwJhJtToAUsRLchtCakFplLkTyPulPZxTSTCQeKZPztPe XqznYjBzTZyYnddwtiD sBy qw w"
# Output: False

# sentence =  "Leetcode eisc cool"
# Output: False

# sentence = "a a ba"
# Output: False

def isCircularSentence(sentence): 
    splt = sentence.split()

    if len(splt) == 1 and splt[0][0] == splt[0][-1]:
        return True
    
    elif len(splt) >= 2:    
        lst = []
        for i in range(len(splt)-1):

            if splt[i][-1] == splt[i+1][0] and splt[-1][-1] == splt[0][0] :
                    lst.append(True)
            else:
                lst.append(False)


        if False not in lst:
            return True
        else:
            return False
        
    else:
        return False
      


print(isCircularSentence(sentence))