#...the classic
#O(n^2)
def bubbleSort(toSort):
    for i in range(len(toSort)-1,0,-1):
        for j in range(i):
            if toSort[j]>toSort[j+1]:
                toSort[j+1], toSort[j] = toSort[j], toSort[j+1]
    return toSort
