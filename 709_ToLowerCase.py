'''
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"

'''



s = "Hello"
Output =  "hello"

s = "here"
Output =  "here"

s = "LOVELY"
Output = "lovely"

def toLowerCase(s) :
    output = str()
    for ltr in s:
        x = ltr.lower()
        output = output+x

    return output


print(toLowerCase(s))