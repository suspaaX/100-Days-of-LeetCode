'''

Code
Testcase
Testcase
Test Result
20. Valid Parentheses
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

'''
s = "(]"

Output = False

# s = "([)]"

# Output: False

# s = "([)]"

# Output =  False

# s = "(){}"

# Output = True

# s = "(]"

# Output = False
# s = "([])"

# s = "()"

# Output: True

# s = "()[]"

# Output = True

# s = "{}"

# Output = True


# s = "([])"

# Output: True


s = "([])"

Output: True

# s = "()"

# Output: True


def isValid(s):

    s1 = s[:]
    wd = str()

    if  '()' in s1:
        k = s1.replace('()','')
        wd = wd+k

    if  '[]' in s1:
        n = s1.replace('[]','')
        wd = wd+n

    if  '{}' in s1:
        o = s1.replace('{}','')
        wd = wd+o

        

    if len(wd) == 0:
        return True
    else:
        return False



print(isValid(s))