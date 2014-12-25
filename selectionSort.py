#...more like shmeshmection shmort

def selectionSort(toSort):
    for i in range(len(toSort)):
        minLoc = i
        for j in range(i+1,len(toSort)):
            if toSort[j]<toSort[i]:
                minLoc = j
        toSort[i], toSort[minLoc] = toSort[minLoc], toSort[i]
    return toSort
