'''
edit by xy


'''

# -*- coding: utf-8 -*-

def checkio(data):
    a=b=c=False

    if len(data)<10:
        return False
    for i in data:
        if i>='a' and i<='z':
            a=True
        if i>='A' and i<='Z':
            b=True
        if i>='0' and i<='9':
            c=True
    if a and b and c:
        return True
    return False
#ans

def checkio(data):

    import string

    return len(data) >= 10 and [i for i in data if i in string.digits] and [i for i in data if i in string.ascii_uppercase] and [i for i in data if i in string.ascii_lowercase]

​

​

#ans2
import re

​

def checkio(data):

​

    #replace this for solution

    return re.match("[a-zA-Z0-9]+", data) and len(data) > 9 and re.search("[a-z]", data) and re.search("[A-Z]", data) and re.search("[1-9]", data)

​

#ans3


import re

​

def checkio(data):    

    if len(data) < 10:

        return False        

    data = re.sub("[a-z]+", "l", data)

    data = re.sub("[A-Z]+", "u", data)

    data = re.sub("[0-9]+", "d", data)

    return set(data) == set("dull")

#ans4

def checkio(data):

    return not(len(data)<10 or data.isalpha() or data.isdigit() or data.islower() or data.isupper())

​



​



​


