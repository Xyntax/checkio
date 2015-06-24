'''
edit by xy


'''

# -*- coding: utf-8 -*-

def checkio(L):
    win = 'D'
    if L[0][0]==L[1][1]==L[2][2] or L[0][2]==L[1][1]==L[2][0] :
        if L[1][1] == 'X':
            win = 'X'
        elif L[1][1] == 'O':
            win = 'O'
    else:
        for i in range(3):
            if L[i][0]==L[i][1]==L[i][2]=='X':
                    win = 'X'
            if L[i][0]==L[i][1]==L[i][2]=='O':
                    win = 'O'
        for j in range(3):
            if L[0][j]==L[1][j]==L[2][j]=='X':
                    win = 'X'
            if L[0][j]==L[1][j]==L[2][j]=='O':
                    win='O'

    return win
#c1
'''
将各个方向的棋子拼在一串，并检查有没有‘XXX’或者‘OOO’
'''

def checkio(result):

    rows = result

    cols = map(''.join, zip(*rows))

    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))

    lines = rows + list(cols) + list(diags)

​

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

#c2


# From Daniel Dou with love...

​'''
本解法打破了turple的局限，讲9个位置编号，并按1-9的编号在一个str中排列棋子，只要按胜利的序列遍历一下这9个位置即可
'''
def checkio(board):

    # First we put everything together into a single string

    x = "".join(board)
'''
这是把turple或者list直接变成str
'''
    

    # Next we outline the 8 possible winning combinations. 

    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]
'''
列举8种可能性
'''
    

    # We go through all the winning combos 1 by 1 to see if there are any

    # all Xs or all Os in the combos

    for i in combos:

        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":#这里直接用 str in str2可以直接判断，注意

            return x[int(i[0])]

    return "D" 


