# -*- coding: utf-8 -*-
__author__ = 'xy'


def golf(n):
 while 1:
  n+=1
  for i in range(2,n):
   if str(n)==str(n)[::-1]and n%i!=0:return n

print golf(13)


#


golf=lambda x:[x for x in range(x+1,9**6)if str(x)[::-1]==str(x)and all(x%c for c in range(2,x))][0]

