'''
edit by xy


'''

# -*- coding: utf-8 -*-

def checkio(text):
    text=[x.lower() for x in text if x.isalpha()]

    L=[]
    for i in text:
        count = 0;
        for j in text:
            if i==j:
                count+=1
        L.append(count)
    D=dict(zip(text,L))

    d = sorted(D.iteritems(),key=lambda d:d[1],reverse = True)

    if len(d)==1:
        return d[0][0]
    if d[0][1]==d[1][1]:
        if d[0][0]<d[1][0]:
            return d[0][0]
        return d[1][0]
    return d[0][0]

#ans1


import string


def checkio(text):

    """

    We iterate through latyn alphabet and count each letter in the text.

    Then 'max' selects the most frequent letter.

    For the case when we have several equal letter,

    'max' selects the first from they.

    """

    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)
'''

str.count(sub, start= 0,end=len(string))
    sub -- This is the substring to be searched.

    start -- Search starts from this index. First character starts from 0 index. By default search starts from 0 index.

    end -- Search ends from this index. First character starts from 0 index. By default search ends at the last index.
'''

'''
 The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

'''
'''


'''
#ans2


from string import ascii_lowercase as letters

checkio = lambda text: max(letters, key=text.lower().count)

#ans3
from collections import Counter


def checkio(text):

    count = Counter([x for x in text.lower() if x.isalpha()])

    m = max(count.values())

    return sorted([x for (x, y) in count.items() if y == m])[0]




