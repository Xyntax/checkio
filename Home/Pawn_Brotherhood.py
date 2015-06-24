# -*- coding: utf-8 -*-
__author__ = 'xy'


def safe_pawns(tur):
    count = 0
    for each in tur:
        # print each
        if each[1] == 1:
            continue
        if each[0] == 'a':
            if chr(ord(each[0]) + 1) + str(int(each[1]) - 1) in tur:
                count += 1
                continue
        if each[0] == 'h':
            if chr(ord(each[0]) - 1) + str(int(each[1]) - 1) in tur:
                count += 1
                continue
        if chr(ord(each[0]) + 1) + str(int(each[1]) - 1) in tur or chr(ord(each[0]) - 1) + str(int(each[1]) - 1) in tur:
            count += 1
    return count

'''
#c1
#没有判断边界情况，因为并不会出现越界的error
def safe_pawns(pawns):

    answer = 0

    for pawn in pawns :

        if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns : answer +=1

    return answer


'''

print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
