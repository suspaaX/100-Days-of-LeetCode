'''
692. Top K Frequent Words
Medium
Topics
premium lock icon
Companies
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.


'''
words = ["i","love","leetcode","i","love","coding"] 
k = 2
Output =  ["i","love"]

# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4
# Output = ["the","is","sunny","day"]


def topKFrequent(words,k):
    dict1 = {}
    for i in words:
        if i in dict1:
            dict1[i] = dict1[i] +1
        else:
            dict1[i] = 1


    rslt = []
    for key,val in dict1.items():
        x = val,key
        rslt.append(x)
    
    rslt2 = []
    rslt.sort(reverse=True)
    for rm in rslt:
        rslt2.append(rm[1])


    rml =  rslt2[0:k]


print(topKFrequent(words,k))