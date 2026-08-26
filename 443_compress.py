'''
443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After modifying the input array in-place, the first 6 characters of chars should be ["a","2","b","2","c","3"].
Example 2:

Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of chars should be ["a"].
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
After modifying the input array in-place, the first 4 characters of chars should be ["a","b","1","2"].
'''


# chars = ["a"]
# Output: 1

# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: 4

# chars = ["a","a","a","b","b","a","a"]
# Output: 4

chars = ["a","a","b","b","c","c","c"]
Output: 6

def compress(chars):

    '''
    dict1 = {}
    for i in chars:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1

    lst =  []
    for key,val in dict1.items():
        lst.append(key)
        if val >1:
            lst.append(str(val))

    lst2 = []
    for k in lst:
        if len(k) == 1:
            lst2.append(k)
        elif len(k)>1:
            for m in k:
                lst2.append(str(m))

    chars[:] = lst2 
    return len(chars)
   
    '''
    for i,j in enumerate(chars):
        for k in chars:
            if k in chars[i:len(chars)]:
                print(k,i)


print((compress(chars)))