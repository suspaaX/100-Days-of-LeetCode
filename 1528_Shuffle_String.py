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

# s = "abc"
# indices = [0,1,2]
# Output: "abc"

def restoreString(s, indices):
    new_dict = {}
    for i,j in zip(s,indices):
        new_dict.update({j:i})
        
    shuffled_string = str()
    for i in range(0,len(s)):
        if i in new_dict:
            shuffled_string = shuffled_string + new_dict.get(i)

    return shuffled_string

print(restoreString(s, indices))