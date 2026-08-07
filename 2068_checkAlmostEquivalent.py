'''
2068. Check Whether Two Strings are Almost Equivalent

Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.

 

Example 1:

Input: word1 = "aaaa", word2 = "bccb"
Output: false
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.
Example 2:

Input: word1 = "abcdeef", word2 = "abaaacc"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.
Example 3:

Input: word1 = "cccddabba", word2 = "babababab"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.
'''

# word1 = "cccddabba"
# word2 = "babababab"
# Output = True
# Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
# - 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
# - 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
# - 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
# - 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.

word1 = "aaaa"
word2 = "bccb"
Output: False
# Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
# The difference is 4, which is more than the allowed 3.

# word1 = "abcdeef" 
# word2 = "abaaacc"
# Output: True

word1 = "zzzyyy"
word2 = "iiiiii"
Output: False



def checkAlmostEquivalent(word1,word2):

    dict_wd1 = {}
    for i in word1:
        if i in dict_wd1:
            dict_wd1[i] = dict_wd1[i] +1
        else:
            dict_wd1[i] = 1
    print(dict_wd1)

    dict_wd2 = {}   
    for i in word2:
        if i in dict_wd2:
            dict_wd2[i] = dict_wd2[i] +1
        else:
            dict_wd2[i] = 1
    print(dict_wd2)

    result = []
    for key,val in dict_wd1.items():
        if key not in dict_wd2 and val>=4:
            result.append(False)

        elif key in dict_wd2 :
            diff = val - dict_wd2.get(key)
            if 0<diff>=4:
                result.append(False)
            elif diff>0:
                m = diff*(-1)
                if 0<diff>=4:
                    result.append(False)

    for key,val in dict_wd2.items():
        if key not in dict_wd1 and val>=4:
            result.append(False)

        elif key in dict_wd1 :
            diff = val - dict_wd1.get(key)
            if 0<diff>=4:
                result.append(False)
            elif diff>0:
                m = diff*(-1)
                if 0<diff>=4:
                    result.append(False)

    print(result)

                
    if False in result:
        return False
    else:
        return True
    

print(checkAlmostEquivalent(word1,word2))
 

