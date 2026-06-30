'''
2418. Sort the People

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

'''
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
Output =  ["Bob","Alice","Bob"]

# names = ["Mary","John","Emma"]
# heights = [180,165,170]
# Output = ["Mary","Emma","John"]


def sortPeople(names, heights):
    lst = []
    for n,h in zip(names,heights):
        x = (h,n)
        lst.append(x)
        lst.sort()

    lst2 = []
    for k in lst:
        x2 = k[1]
        lst2.append(x2)
    lst2.reverse()
    return (lst2)


print(sortPeople(names, heights))

        