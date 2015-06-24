# -*- coding: utf-8 -*-
__author__ = 'xy'


class Check(object):
    def __init__(self, **kw):
        pass

    def __cmp__(self):
        return True

    def __eq__(self):
        return True

    def __ne__(self):
        return True

    def __lt__(self):
        return True

    def __gt__(self):
        return True

    def __le__(self):
        return True

    def __ge__(self):
        return True

    def __call__(self):
        return True

    def __str__(self):
        return "42"

    def __repr__(self):
        print True


def checkio(anything):
    return Check

checkio("checkio('Hello') < 'World'")
print checkio('Hello') < 'World'
