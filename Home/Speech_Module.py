FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"




def checkio(number):

    s=''

    n=str(number)

    if len(n)==3:

        if not n[0]=='0':

            s+=FIRST_TEN[int(n[0])-1]+' '+HUNDRED

        n=n[1:]

    if len(n)==2:

        if not n[0]=='0':

            if n[0]=='1':

                return (s+' '+SECOND_TEN[int(n[1])] ).strip()

            else:

                s=s+' '+OTHER_TENS[int(n[0])-2]

        n=n[1:]

    if len(n)==1:

        if not n[0]=='0':

            s=s+' '+FIRST_TEN[int(n[0])-1]

    return s.strip()

'''
strip() 表示去掉string首尾空格
str.split(',')
'''

print checkio(149)

#c1
def checkio(i):

    if i < 20:

        result = 'zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')[i]

    elif i < 100:

        result = ',,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')[i//10]

        if i % 10:

            result += ' ' + checkio(i % 10)#递归是亮点！

    elif i < 1000:

        result = checkio(i // 100) + ' hundred'

        if i % 100:

            result += ' ' + checkio(i % 100)

    return result

#c2

'''
divmod(9,2) return(4, 1) 返回一个turple，（地板除，余数）

str.join(turple/list) 用str将turple中的各个元素链接成一个字符串  str='-'  str.join([a,b,c])=='a-b-c'

print("{1:^10} {0:10}".format("age","name"))
{0} {1}标记数据，其中{0}对应的是'age'，{1}->'name'
:
^表示输出时右对齐 不加表示左对齐
10表示限制输出宽度 若此宽度小于字符串的实际宽度，以实际宽度输出。

'''

def checkio(number):

    hundreds, remainder = divmod(number, 100)

    tens, units = divmod(remainder, 10)

    # construct the 4 possible parts of the result and filter out the empty ones

    return ' '.join(filter(None,

                           ['{0} hundred'.format(UNITS[hundreds]) if hundreds else '',

                            TENS[tens-2] if tens > 1 else '',

                            OVER_TEN[units] if tens == 1 else '',

                            UNITS[units] if (tens != 1 and units) or not number else '']))



