'''
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

'''
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
Output: 2
# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7

def countConsistentStrings(allowed, words):
    prs2 = []
    for i in words:
        if set(i).issubset(set(allowed)):
            prs2.append(i)

    return len(prs2)  
            

print(countConsistentStrings(allowed, words))

'method1'
        # prs2 = []
        # for i in words:
        #     x2 = [k for k in i]
        #     prs2.append(x2)

        # lst1 = []
        # for k in prs2:
        #     if set(k).issubset(set(allowed)):
        #         lst1.append(k)
        # return len(lst1)     
        # 


'method2'
    # num = 0
    # for i in words:
    #     if set(i).issubset(set(allowed)):
    #         num = num+1

    # return num

                