'''
1704. Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

'''
# s = "textbook"
# Output: False


# s = "book"
# Output =  True

s = "MerryChristmas"
Output = False



def halvesAreAlike(s) :
    vowel =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    half = int(len(s)/2)

    x = s[0:half]
    x2 = s[half:len(s)]


    lst1 = []
    for k1 in vowel:
        if k1 in x:
            ct1 = x.count(k1)
            lst1.append(ct1)

    lst2 = []
    for k2 in vowel:

        if k2 in x2:
            ct2 = x2.count(k2)
            lst2.append(ct2)

    
    if sum(lst1) == sum(lst2):
        return True
    else:
        return False

        
print(halvesAreAlike(s))
