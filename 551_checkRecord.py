'''

551. Student Attendance Record I

You are given a string s representing an attendance record for a student where each character 
signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

 

Example 1:

Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
Example 2:

Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

'''
s = "PPALLL"
Output = False

s = "PPALLP"
Output = True

def checkRecord(s):  
    k = [] 
    dict1 = {} 
    for i in s:
        x1 = s.count(i) 
        dict1.update({i:x1})

    c1 = dict1.get('A')
    c2 = dict1.get('L')
    print(c1,c2)

    # for k in dict1.items():
    #     if k = c1
    #     if c1>2 and c2<=2:
    #         return True
    #     else:
    #         return False



print(checkRecord(s))  