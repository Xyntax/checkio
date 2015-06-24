# -*- coding: utf-8 -*-
__author__ = 'xy'

#  "Fizz buzz" is a word game we will use to teach the robots about division.
# Let's learn computers.
#
# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.
#
# Input: A number as an integer.
#
# Output: The answer as a string.
#
# Precondition: 0 < number ≤ 1000
def checkio(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return 'Fizz Buzz'
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'

# # c1
# # 清晰明了
# def checkio(number):
#
#     if number % 15 == 0:
#
#         return 'Fizz Buzz'
#
#     if number % 5 == 0:
#
#         return 'Buzz'
#
#     if number % 3 == 0:
#
#         return 'Fizz'
#
#     return str(number)

