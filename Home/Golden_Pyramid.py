'''
edit by xy


'''

# -*- coding: utf-8 -*-

# #blog ans1
# def golden_pyramid_d(triangle):
#     tr = [row[:] for row in triangle]  # copy
#     for i in range(len(tr) - 2, -1, -1):
#         for j in range(i + 1):
#             tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
#     return tr[0][0]

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    tr = [list(x) for x in pyramid]
    i = len(tr) - 2
    while i >= 0:
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
        i -= 1
    return tr[0][0]

# print count_gold((
#         (1,),
#         (2, 1),
#         (1, 2, 1),
#         (1, 2, 1, 1),
#         (1, 2, 1, 1, 1),
#         (1, 2, 1, 1, 1, 1),
#         (1, 2, 1, 1, 1, 1, 9)
#     ))

'''c1
    ===============

    Golden Pyramid

    ===============



    Approach

    --------



    This algorithm is a greedy approach to solving the problem.

    Instead of working forward through the pyramid, we will work backwards.

    The idea is to start in the second to bottom row and select maxium of the

    the next two possible values from the current node and add that value to

    the current node.



    After that we continue to roll up the rows and repeat the process for each

    node in that row.  When we reach the starting node we will have the sum

    of the maximum path.



    *Note*: we are not finding the best path; we are only finding the maxium sum

    from that path.

​

    Code

    ----



    I want a mutable copy of the pyramid to work with.

    Get the number of rows from the **len** function.

    The last row is not in play to start hence **rows-1**

    Also we're working backwards so use the **reversed** function.

    Need to itertate over each item in the row. Note the plus 1, range(0)

    returns an empty list.

    The possible nodes to examine are 1) the on directly below i+1,j

    and the one below and to the right i+1, j+1.  We use the **max**

    function to select the largest one and then add it to the current

    node.



    '''
'''
    py = [list(i) for i in pyramid]

    for i in reversed(range(len(py)-1)):

        for j in range(i+1):

            py[i][j] +=(max(py[i+1][j], py[i+1][j+1]))

​

    return py[0][0]


'''