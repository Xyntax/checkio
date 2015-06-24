'''
edit by xy


'''

# -*- coding: utf-8 -*-

def checkio(data):
    s=''
    if data>=1000:
        M=data//1000
        data=data%1000
        for i in range(M):
            s+='M'
    if data>=500:
        D=data//500
        data=data%500
        s+='D'
    if data>=100:
        for i in range(data//100):
            s+='C'
        data=data%100
    if data>=50:
        for i in range(data//50):
            s+='L'
        data=data%50
    if data>=10:
        for i in range(data//10):
            s+='X'
        data=data%10
    if data>=5:
        s+='V'
        data-=5
    for i in range(data):
        s+='I'
    return s

print checkio(3888)

#1
def checkio(number):

    'return roman numeral using the specified integer value from range 1...3999'

    roman = ''

    romanmappings = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 

                     40: "XL", 50: "L", 90: "XC", 100: "C", 

                     400: "CD", 500: "D", 900: "CM", 1000: "M" }                     

    for intVal in sorted(romanmappings.keys(), reverse=True):

        while number >= intVal:

            roman += romanmappings[intVal]

            number -= intVal

    return roman

    

​

#2
def checkio(number):

    'return roman numeral using the specified integer value from range 1...3999'

    

    bases=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

    letters=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    

    string=''

    

    for base, letter in list(zip(bases,letters)):

        root=number//base

        string+=''.join(letter for i in range(0,root))

        number-=root*base

    

    return string

#3 speedy


def checkio(x):

    a,r="",{}

    for i in range(3):

        p,(j,c,d)=10**i,"IVXLCDM"[2*i:][:3]

        r.update({p:j,5*p:c,4*p:j+c,9*p:j+d,10*p:d})

    for k in reversed(sorted(r)):

        a+=x//k*r[k]

        x%=k

    return a


