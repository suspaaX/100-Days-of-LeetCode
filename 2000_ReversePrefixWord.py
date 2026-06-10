'''
2000. Reverse Prefix of Word
Easy
Topics
premium lock icon
Companies
Hint
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

 

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".


'''
# word = "abcdefd" 
# ch = "d"
# Output = "dcbaefd"

word = "abcd" 
ch = "z"
Output =  "abcd"

# word = "xyxzxe"
# ch = "z"
# Output = "zxyxxe"

def reversePrefix(word,ch):
    resulting_string = ''
    if ch in word:
        idx = word.index(ch)

        lst1 = []
        for i in word[0:idx+1]:
            lst1.append(i)



        lst2 = []
        for k in word[idx+1:len(word)]:
            lst2.append(k)



        sum1 = (lst1[::-1]+lst2)

        for i in sum1:
            resulting_string = resulting_string+i

        return resulting_string


    else:
        return word



print(reversePrefix(word,ch))




