'''

1528. Shuffle String
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

'''

s = "codeleet" 
indices = [4,5,6,7,0,2,1,3]
Output =  "leetcode"


def restoreString(s, indices):
    dict1 = {}
    for i,k in zip(s,indices):
        dict1.update({k:i})
    # print(dict1)
    
    new_ltr = [dict1]
    new_ltr.sort()
    print(new_ltr)



print(restoreString(s, indices))