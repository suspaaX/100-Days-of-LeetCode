'''

1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


# words = ["cat","bt","hat","tree"]
# chars = "atach"
# Output =  6

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Output =  10


'''
words = ["cat","bt","hat","tree"]
chars = "atach"
Output =  6



# words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
#          "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
#          "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
#          "boygirdlggnh",
#          "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
#          "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
#          "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
#          "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
#          "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
#          "oxgaskztzroxuntiwlfyufddl",
#          "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
#          "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
#          "eeilfdaookieawrrbvtnqfzcricvhpiv",
#          "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
#          "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
#          "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
#          "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob",
#          "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
#          "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]

# chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
# Output = 0
# print(len(chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Output =  10
def countCharacters(words,chars):
    dict1 = {}
    lst1 = []
    for i in range(0,len(words)):
        x = words[i]
        for k in x:
            if k == words[i]:
                m = x.count(k)
                dict1.update({k:m})
                lst1.append(dict1)
    print(dict1)


print(countCharacters(words,chars))