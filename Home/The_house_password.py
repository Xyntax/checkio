'''
edit by xy


'''

# -*- coding: utf-8 -*-

checkio = lambda s:not(
        len(s)<10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
        )
#记住这四个方法直接判断元素类型
