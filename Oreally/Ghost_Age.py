# -*- coding: utf-8 -*-
__author__ = 'xy'
# CheckIO - O'Reilly Challenge 2 : Ghost Age
# http://checkio.org

# Nicola takes a moment to study the ghosts.
# He is trying to think up a new method to determine just how old these ghosts are.
# He knows that their age is somehow related to their opacity.
# To measure their opacity Nikola uses a scale of 10000 units to 0 units,
# where 10000 is a completely opaque newborn ghost (0 years old) and 0 is completely transparent.
# After some experimenting, Nikola thinks he has discovered the law of ghostly opacity.
# On every birthday, a ghost's opacity is reduced by a number of units
# equal to its age when its age is a Fibonacci number or increased by 1 if it is not.
# Precondition:age < 5000
# 0 < opacity < 10000

# Get Fibonacci number n
def nextFibo(n):
    if n < 2:
        return n
    else:
        return nextFibo(n - 1) + nextFibo(n - 2)


def checkio(limit):
    age = 0
    lastFibo = 1
    indexFibo = 2
    opacity = 10000
    while opacity != limit:  # While I dont found transparency number...
        age += 1
        if age == lastFibo:  # -age if age is a Fibonacci number
            opacity -= age
            indexFibo += 1
            lastFibo = nextFibo(indexFibo)
        else:  # +1 in other case
            if opacity < 10000:  # Keeping opacity value into the limis
                opacity += 1
    return age

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(9995) == 4, "4 years"
    assert checkio(3703) == 4665, "4665 years"

'''
#c1



def checkio(tip):

    MAGIC = (lambda x:x[0]+x[3]*x[4])(list(map(ord,"mAGIC")))

    MORE = (lambda x:x[4]-x[1])(list(map(ord,"mAGIC")))



    spells = [True]+[False]*(MAGIC)

    this, that = 0,1

    while that <=MAGIC:

        spells[that] = True

        this,that = that, this+that

    cut_fingers=[MORE*MAGIC]

    for toad in range(MORE//MORE,MAGIC + MORE//MORE):

        cut_fingers = cut_fingers + [cut_fingers[-1] + (-toad if spells[toad] else MORE//MORE)]

    return cut_fingers.index(tip)


'''