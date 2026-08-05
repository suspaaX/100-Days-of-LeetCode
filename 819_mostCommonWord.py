'''
819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

'''
paragraph = "a."
banned = []
Output =  "a"



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output = "ball"


# paragraph = "Bob. hIt, baLl"
# banned = ["bob", "hit"]
# Output = "ball" 

def mostCommonWord(paragraph, banned) :
    x = paragraph.casefold()
    x2 = x.split()

    if len(x2)<=1 and len(banned) <= 1:

        for i in x2:
            if i.isalpha():
                return i
            else:
                return i[0:len(i)-1]

    elif len(x2)>=2 :
        str1 = []
        str2 = []
        for i in x2:

            if i.isalpha():
                str1.append(i)
            else:
                str2.append(i[0:len(i)-1])

        lst3 = str1 + str2
        print(lst3)

        dict1 = {}
        for i in lst3:
            if i in dict1:
                dict1[i] = dict1[i] +1
            else:
                dict1[i] = 1
        print(dict1)

        for key,val in dict1.items():
            if val>=2 and  key not in banned:
                return key
            
            else :
                return key


print(mostCommonWord(paragraph, banned))