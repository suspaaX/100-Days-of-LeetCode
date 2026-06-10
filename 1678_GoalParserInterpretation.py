'''

Code
Testcase
Testcase
Test Result
1678. Goal Parser Interpretation
Easy
Topics
premium lock icon
Companies
Hint
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"

'''


# command = "G()()()()(al)"
# Output =  "Gooooal"

# command = "(al)G(al)()()G"
# Output =  "alGalooG"

command = "G()(al)"
Output =  "Goal"

def interpret(command):
    Goal_Parser = str()

    dict1 = {

        'G':'G',
        ' ':'o',
        '(al)':'al'


        } 

    # for cmd in command:
    #     # print(cmd)
    #     if cmd in dict1:
    #         Goal_Parser = Goal_Parser + dict1.get(cmd)

    # return Goal_Parser
    x = command.split('()')
    print(x)
    for i in x:
        if i in dict1:
            Goal_Parser = Goal_Parser+dict1.get(i)

    print(Goal_Parser)


print(interpret(command))
    
