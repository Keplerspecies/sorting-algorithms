#...the von neumann

def mergeSort(toSort):
    
    def merge(first, second):
        combined = []
        firstPointer = secondPointer = 0
        while(firstPointer < len(first) and secondPointer < len(second)):
            if(first[firstPointer] < second[secondPointer]):
                combined.append(first[firstPointer])
                firstPointer = firstPointer + 1
            else:
                combined.append(second[secondPointer])
                secondPointer = secondPointer + 1
        while(firstPointer < len(first)):
            combined.append(first[firstPointer])
            firstPointer = firstPointer + 1
        while(secondPointer < len(second)):
            combined.append(second[secondPointer])
            secondPointer = secondPointer + 1
        return combined
    
    if(len(toSort) <= 1):
        return toSort
    
    return merge(mergeSort(toSort[:(len(toSort)/2)]), mergeSort(toSort[(len(toSort)/2):]))
