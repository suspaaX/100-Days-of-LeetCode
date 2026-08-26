'''

Code
Testcase
Testcase
Test Result
1572. Matrix Diagonal Sum
Easy
Topics
premium lock icon
Companies
Hint
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5

'''


mat = [ [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
Output: 8



mat = [[5]]
Output: 5

# mat = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# Output: 25

def diagonalSum(mat):
    if len(mat) == 1 :
        return mat[0][0]
    
    elif len(mat)>1 and len(mat)%2 == 0 :
        rslt = 0
        for i,j in enumerate(mat):    
            sum1 = mat[i][i]
            sum2 = mat[i][-1-i]
            rslt = rslt + sum1 + sum2 
        return rslt 

    elif len(mat)>1 and len(mat)%2 != 0:
        k = (len(mat)//2)
        k2 = mat[k][k]
        rslt = 0
        for i,j in enumerate(mat):    
            sum1 = mat[i][i]
            sum2 = mat[i][-1-i]
            rslt = rslt + sum1 + sum2
        return rslt - k2


            
print(diagonalSum(mat))