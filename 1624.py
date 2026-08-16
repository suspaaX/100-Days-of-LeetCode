'''
1624. Largest Substring Between Two Equal Characters
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

'''

s = "cbzxy"
Output =  -1

s = "abca"
Output = 2

# s = "scayofdzca"
# Output = 6

s = "mgntdygtxrvxjnwksqhxuxtrv"
print(len(s))
Output = 6

def maxLengthBetweenEqualCharacters(s):

    lst = []
    dict1 = {}
    for i,j in enumerate(s):
        if j in s[i+1:len(s)]:
            idx = s.index(j,i+1)
            if j in dict1:
                dict1[j] = idx
            else:
                dict1[j] = idx
            
            wd = s[i:dict1.get(j)+1]
            lst.append(wd)
    print(lst)  

    result = []
    for k in lst:
        m = k[1:len(k)-1]
        result.append(len(m))

    return max(result)



print(maxLengthBetweenEqualCharacters(s))