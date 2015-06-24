'''
edit by xy


'''

# -*- coding: utf-8 -*-

def count_neighbours(grid, row, col):
    count = 0
    if col == 0 and row == 0:
        if grid[0][1] == 1:
            count += 1
        if grid[1][0] == 1:
            count += 1
        if grid[1][1] == 1:
            count += 1
    elif row == 0 and col == len(grid[0]) - 1:
        if grid[row][col - 1] == 1:
            count += 1
        if grid[row + 1][col] == 1:
            count += 1
        if grid[row + 1][col - 1] == 1:
            count += 1
    elif row == len(grid) - 1 and col == 0:
        if grid[row][col + 1] == 1:
            count += 1
        if grid[row - 1][col] == 1:
            count += 1
        if grid[row - 1][col + 1] == 1:
            count += 1
    elif row == len(grid) - 1 and col == len(grid[row]) - 1:
        if grid[row - 1][col] == 1:
            count += 1
        if grid[row][col - 1] == 1:
            count += 1
        if grid[row - 1][col - 1] == 1:
            count += 1
    elif row == len(grid) - 1:
        if grid[row][col - 1] == 1:
            count += 1
        if grid[row][col + 1] == 1:
            count += 1
        if grid[row - 1][col] == 1:
            count += 1
        if grid[row - 1][col - 1] == 1:
            count += 1
        if grid[row - 1][col + 1] == 1:
            count += 1
    elif row == 0:
        if grid[row][col - 1] == 1:
            count += 1
        if grid[row][col + 1] == 1:
            count += 1
        if grid[row + 1][col] == 1:
            count += 1
        if grid[row + 1][col - 1] == 1:
            count += 1
        if grid[row + 1][col + 1] == 1:
            count += 1
    elif col == len(grid[row]) - 1:
        if grid[row - 1][col] == 1:
            count += 1
        if grid[row + 1][col] == 1:
            count += 1
        if grid[row][col - 1] == 1:
            count += 1
        if grid[row - 1][col - 1] == 1:
            count += 1
        if grid[row + 1][col - 1] == 1:
            count += 1
    elif col == 0:
        if grid[row - 1][col] == 1:
            count += 1
        if grid[row + 1][col] == 1:
            count += 1
        if grid[row][col + 1] == 1:
            count += 1
        if grid[row - 1][col + 1] == 1:
            count += 1
        if grid[row + 1][col + 1] == 1:
            count += 1

    else:
        if grid[row - 1][col - 1] == 1:
            count += 1
        if grid[row - 1][col] == 1:
            count += 1
        if grid[row - 1][col + 1] == 1:
            count += 1
        if grid[row][col - 1] == 1:
            count += 1
        if grid[row][col + 1] == 1:
            count += 1
        if grid[row + 1][col] == 1:
            count += 1
        if grid[row + 1][col - 1] == 1:
            count += 1
        if grid[row + 1][col + 1] == 1:
            count += 1
    return count


print count_neighbours(((0, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)), 3, 0)



# ans1


def count_neighbours(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))

    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))

    return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]


# ans2


def count_neighbours(grid, row, col):
    rs, cs = [slice(max(0, x - 1), x + 2) for x in (row, col)]

    return sum(e for r in grid[rs] for e in r[cs]) - grid[row][col]


# ans3


def count_neighbours(grid, row, col):
    N, M = len(grid), len(grid[0])

    NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    return sum(0 <= row + i < N and 0 <= col + j < M and grid[row + i][col + j]

               for i, j in NEIGHBOURS)
