# -*- coding: utf-8 -*-
__author__ = 'xy'
#  You are given an array of integers.
# You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
# then multiply this summed number and the final element of the array together.
# Don't forget that the first element has an index of 0.
#
# For an empty array, the result will always be 0 (zero).
#
# Input: A list of integers.
#
# Output: The number as an integer.
#
# Example:
#
# checkio([0, 1, 2, 3, 4, 5]) == 30
#
# checkio([1, 3, 5]) == 30
#
# checkio([6]) == 36
#
# checkio([]) == 0
'''
def checkio(tur):
    if len(tur) == 0:
        return 0
    else:
        sum = 0
        for i in range(0, len(tur), 2):
            sum += tur[i]
        return sum * tur[-1]
'''
# c1
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0
    # 处理隔几位的时候直接用子串比循环要clear
    return sum(array[0::2]) * array[-1]
