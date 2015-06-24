# -*- coding: utf-8 -*-
__author__ = 'xy'

'''
 Our robots are always working to improve their linguistic skills. For this mission,
  they research the latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by
white-spaces and punctuation marks. Numbers are not considered words in this mission
(a mix of letters and digits is not a word either).
You should count the number of words (striped words) where the vowels with consonants
 are alternating, that is; words that you count cannot have two consecutive vowels or
consonants. The words consisting of a single letter are not striped -- do not count those.
Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

Example:

checkio("My name is ...") == 3

checkio("Hello world") == 0

checkio("A quantity of striped words.") == 1, "Only of"

checkio("Dog,cat,mouse,bird.Human.") == 3


'''

'''
#xy

VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
import string

def checkio(text):
    text = '_'+text+'  '
    count = 0
    isvowel = 2
    flag = False
    i = 0
    while i < len(text) - 2:
        if text[i] not in string.letters + string.digits:
            if text[i+1] in string.letters + string.digits:
                if text[i+2] not in string.letters + string.digits:
                    i = i + 2
                    continue
                else:
                    if flag:
                        count += 1
                    isvowel = 2
                    flag = True

        else:
            if text[i] in string.digits:
                flag = False
            if text[i] in VOWELS:
                if isvowel == 1:
                    flag = False
                isvowel = 1
            if text[i] in CONSONANTS:
                if isvowel == 0:
                    flag = False
                isvowel = 0
        i += 1

    if flag:
        count += 1
    return count

print checkio('1st 2a ab3er root rate')

'''

# c1

'''

用到的方法->Python3
str.upper()
str.replace('c', ' ')
str.split(' ') -> return a list
str.isalpha()
str.find('cc')

'''
VOWELS = "AEIOUY"

CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

PUNCTUATION = ",.!?"


def checkio(text):

    # 统一变成大写，能减少大小写全有时候的查询次数
    text = text.upper()

    # 将标点统一变成空格
    for c in PUNCTUATION:
        text = text.replace(c, " ")

    # 将两种字母都替换
    for c in VOWELS:
        text = text.replace(c, "v")

    for c in CONSONANTS:
        text = text.replace(c, "c")

    # words直接变成了 list
    words = text.split(" ")
    # print words
    count = 0

    for word in words:

        # 注意可以对一个str判断isalpha()，ph3+用isalpha()，ph2用 in string.letters
        if len(word) > 1 and word.isalpha():

            # 精髓，如果找到cc或vv则不对
            if word.find("cc") == -1 and word.find("vv") == -1:
                count += 1

    return count


print checkio('hello woe for a py')
'''
# f2


def checkio(text, transition=(

0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,192,192,192,192,

192,192,192,192,192,192,192,192,192,192,192,192,96,96,96,96,96,96,96,96,96,96,

192,192,192,192,192,192,192,576,288,288,288,576,288,288,288,576,288,288,288,288,

288,576,288,288,288,288,288,576,288,288,288,576,288,192,192,192,192,192,192,576,

288,288,288,576,288,288,288,576,288,288,288,288,288,576,288,288,288,288,288,576,

288,288,288,576,288,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,

192,192,192,192,192,192,96,96,96,96,96,96,96,96,96,96,192,192,192,192,192,192,

192,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,

96,192,192,192,192,192,192,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,96,

96,96,96,96,96,96,96,96,96,192,192,192,192,192,192,192,192,192,192,192,192,192,

192,192,192,192,192,192,192,192,96,96,96,96,96,96,96,96,96,96,192,192,192,192,

192,192,192,576,288,288,288,576,288,288,288,576,288,288,288,288,288,576,288,288,

288,288,288,576,288,288,288,576,288,192,192,192,192,192,192,576,288,288,288,576,

288,288,288,576,288,288,288,288,288,576,288,288,288,288,288,576,288,288,288,576,

288,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,

192,192,96,96,96,96,96,96,96,96,96,96,192,192,192,192,192,192,192,384,96,96,96,

384,96,96,96,384,96,96,96,96,96,384,96,96,96,96,96,384,96,96,96,384,96,192,192,

192,192,192,192,384,96,96,96,384,96,96,96,384,96,96,96,96,96,384,96,96,96,96,96,

384,96,96,96,384,96,192,192,192,192,192,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,96,

96,96,96,96,96,96,96,96,0,0,0,0,0,0,0,96,480,480,480,96,480,480,480,96,480,480,

480,480,480,96,480,480,480,480,480,96,480,480,480,96,480,0,0,0,0,0,0,96,480,480,

480,96,480,480,480,96,480,480,480,480,480,96,480,480,480,480,480,96,480,480,480,

96,480,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,96,96,96,96,96,96,96,96,96,

0,0,0,0,0,0,0,384,96,96,96,384,96,96,96,384,96,96,96,96,96,384,96,96,96,96,96,

384,96,96,96,384,96,0,0,0,0,0,0,384,96,96,96,384,96,96,96,384,96,96,96,96,96,

384,96,96,96,96,96,384,96,96,96,384,96,0,0,0,0,0,192,192,192,192,192,192,192,

192,192,192,192,192,192,192,192,192,96,96,96,96,96,96,96,96,96,96,192,192,192,

192,192,192,192,96,480,480,480,96,480,480,480,96,480,480,480,480,480,96,480,480,

480,480,480,96,480,480,480,96,480,192,192,192,192,192,192,96,480,480,480,96,480,

480,480,96,480,480,480,480,480,96,480,480,480,480,480,96,480,480,480,96,480,192,

192,192,192,192

)):

    striped = state = 0

    for byte in text.encode():

        state = transition[state + byte]

        if not state:

            striped += 1

    return striped + (state == 480 or state == 384)





'''
