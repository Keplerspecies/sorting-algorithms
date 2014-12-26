#...the partition exchange

from random import randint

def quickSort(toSort):

    lastIndex = len(toSort) -1
    if len(toSort) <= 1:
        return toSort
    
    pivotIndex = randint(0, len(toSort)-1)
    toSort[lastIndex], toSort[pivotIndex] = toSort[pivotIndex], toSort[lastIndex]
    curIndex = 0
    
    for i in range(0, len(toSort)):
        if toSort[i] < toSort[lastIndex]:
            toSort[i], toSort[curIndex] = toSort[curIndex], toSort[i]
            curIndex = curIndex +1
    toSort[curIndex], toSort[lastIndex] = toSort[lastIndex], toSort[curIndex]

    return quickSort(toSort[:curIndex]) + [toSort[curIndex]] + quickSort(toSort[curIndex+1:])
