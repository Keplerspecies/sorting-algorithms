#...the eternally nlogn

def heapSort(toSort):
    def siftDown(start, end):
        child = start * 2 + 1
    
        if child < end:
            if child+1 < end and a[child+1] > a[child]:
                child = child + 1
            if toSort[child] > toSort[start]:
                toSort[child], toSort[start] = toSort[start], toSort[child]
                siftDown(child, end)

    def heapify(toSort):
        current = len(toSort)/2-1
        while current >= 0:
            toSort = siftDown(current, len(a))
            current = current - 1

    heapify(toSort)
    
    end = len(a) - 1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end = end - 1
        siftDown(0, end)
    return toSort 
