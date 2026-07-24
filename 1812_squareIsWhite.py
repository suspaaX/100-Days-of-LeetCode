'''1812. Determine Color of a Chessboard Square

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

 

Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false
'''

coordinates = "c7"
Output: False

# coordinates = "h3"
# Output = True

coordinates = "a1"
Output: False

coordinates = "d2"
Output: False


coordinates = "e1"
Output: False

# coordinates = "e2"
# Output: True

def squareIsWhite(coordinates):
    dict1 = {
            'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8
            }


    for i in coordinates:
        pos = coordinates[1]
        idx = coordinates[0]
        if idx in dict1:
            val = dict1.get(idx)

    print(pos,val)

    if val%2!= 0 and int(pos)%2 != 0:
        return False
    elif val%2 == 0 and int(pos)%2 == 0:
        return False
    else:
        return True



print(squareIsWhite(coordinates))