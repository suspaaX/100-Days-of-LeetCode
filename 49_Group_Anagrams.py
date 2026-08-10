'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

'''

strs = ["eat","tea","tan","ate","nat","bat"]

Output =  [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(strs) :   
    all_dict1 = []
    for i in strs:

        dict2 = {}
        for m in i:
            if m in  dict2:
                dict2[m] = dict2[m] +1
            else:
                dict2[m] = 1

            rslt = []
            for key,val in dict2.items() :
                if m in key:
                    rslt.append(i)

            print(rslt)

        









groupAnagrams(strs) 