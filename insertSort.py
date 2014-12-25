#...the short and sweet

def insertSort(toSort):
    for i in range(len(toSort)):
        while i > 0 and toSort[i] < toSort[i-1]:
            toSort[i], toSort[i-1] = toSort[i-1], toSort[i]
            i = i-1
    return toSort
