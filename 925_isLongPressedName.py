'''925. Long Pressed Name
Easy
Topics
premium lock icon
Companies
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
'''

name = "saeed"
typed = "ssaaedd"
Output: False

# name = "alex"
# typed = "aaleex"
# Output: True


def isLongPressedName(name,typed):
    dict1_typed  = {}
    for ltr in typed:
        if ltr in dict1_typed:
            dict1_typed[ltr] = dict1_typed[ltr] +1
        else:
            dict1_typed[ltr] = 1        

    # print(dict1_typed)

    dict2_name = {}
    for ltr2 in name:
        if ltr2 in dict2_name:
            dict2_name[ltr2] = dict2_name[ltr2] +1
        else:
            dict2_name[ltr2] =1
    # print(dict2_name)

    for d1key,d1val in dict1_typed.items():
        d2_val = dict2_name.get(d1key)
        # print(d1val,d2_val)
        if d1key in dict2_name and d1val>=d2_val:
            print(False)
    else:    
        print(True)

print(isLongPressedName(name,typed))