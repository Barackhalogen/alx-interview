#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers 
    representing the Pascal's triangle of n:
    """

    if n <= 0:
        return []

    
    """ initialize an empty resulting array """
    pascal = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ first column is set to 1 as shown """
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li-1][col] + pascal[li-1][col-1])
            else(col == li):
                """ diagonal set to 1, then append """
                pascal[li].append(1)

    return pascal
