'''
edit by xy


'''

# -*- coding: utf-8 -*-

def checkio(data):
    data=sorted(data)#########
    if len(data)%2==1:
        return (data[(len(data)-1)//2])
    return (data[len(data)//2-1]+data[len(data)//2])/2.0

print checkio([3,1,2,3,5])

print checkio([1,2,3,4,5,6])
#ans

def checkio(data):

    data.sort()#########

    i = len(data)

    if (i//2)*2 < i:

        return data[i//2]

    else:

        return (data[i//2-1]+data[(i//2)])/2

    #replace this for solution

#ans1
def checkio(data):
    off = len(data)//2
    data.sort()
    med = data[off] + data[-(off+1)]
    return med/2
#比较偏的算法，将奇数与偶数统一化处理，机智

