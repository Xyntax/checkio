# -*- coding: utf-8 -*-
__author__ = 'xy'
'''
 Sophia's drones are not soulless and stupid drones;
 they can make and have friends. In fact, they already are working for
  the their own social network just for drones! Sophia has received the
   data about the connections between drones and she wants to know more
    about relations between them.

We have an array of straight connections between drones.
 Each connection is represented as a string with two names of friends separated by hyphen.
  For example: "dr101-mr99" means what the dr101 and mr99 are friends.
  Your should write a function that allow determine more complex connection between drones.
   You are given two names also. Try to determine if they are related through common bonds
    by any depth.

For example: if two drones have a common friends or friends who have common
friends and so on.

'''

def check_connection(network, first, second):
    _dict = {}
    n = 0
    for each in network:
        couple = each.split('-')
        if couple[0] in _dict and couple[1] not in _dict:
            _dict[couple[1]] = _dict.get(couple[0])
        elif couple[1] in _dict and couple[0] not in _dict:
            _dict[couple[0]] = _dict.get(couple[1])
        elif couple[0] in _dict and couple[1] in _dict:
            for i in _dict:
                if _dict.get(i) == _dict.get(couple[1]):
                    _dict[i] = _dict.get(couple[0])
        else:
            _dict[couple[0]] = n
            _dict[couple[1]] = n
        n += 1
    if _dict.get(first) == _dict.get(second):
        return True
    return False
# print check_connection(("dr101-mr99","mr99-out00","dr101-out00","scout1-scout2","scout3-scout1","scout1-scout4","scout4-sscout","sscout-super",),"scout2","scout3")
print check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),"dr101","mr99")

'''
# c1

def check_connection(network, first, second):

    setlist = []

    for connection in network:

        s = ab = set(connection.split('-'))

        # unify all set related to a, b

        for t in setlist[:]: # we need to use copy

            if t & ab:       # check t include a, b

                s |= t

                setlist.remove(t)

        setlist.append(s)    # only s include a, b

    return any(set([first, second]) <= s for s in setlist)


'''

'''
# creative1

def check_connection(network, first, second):

    a = [set(i.split("-")) for i in network]

    b = []

    for j in a:

        for i in a:

            if len(j & i) > 0:

                j |= i

        if j not in b:

            if first in j and second in j:

                return True

            b.append(j)

    return False


'''

'''
#s1

def check_connection(net, fst, snd):

    net = [(f, t) for f,t in map(lambda s: s.split(sep='-'), net)]

    netd = dict()

    for el in net:

        netd[el[0]] = netd.setdefault(el[0], []) + [el[1]]

        netd[el[1]] = netd.setdefault(el[1], []) + [el[0]]

    (stack, visited) = (set(netd[fst]), set([fst]))

    while stack != set():

        e = stack.pop()

        if e == snd:

            break

        if e not in visited:

            visited.add(e)

            stack.update(netd[e])

    else:

        return False

    return True


'''