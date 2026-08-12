'''
1351. Count Negative Numbers in a Sorted Matrix
Easy
Topics
premium lock icon
Companies
Hint
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

'''

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8

grid = [[3,2],[1,0]]
Output: 0

def countNegatives(grid) :
    lst2 = []
    for i in grid:
        for k in i:
            if  k < 0 :
                lst2.append(k)
                
    return len(lst2)

print(countNegatives(grid))