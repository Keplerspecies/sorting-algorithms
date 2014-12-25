#The 'Why?'
#keeping a counter for giggles

from random import shuffle

def bogoSort(toSort):
    counter = 0

    def isOrdered():
        for i in range(len(toSort)-1):
            if toSort[i]>toSort[i+1]:
                return False
        return True
    
    while not isOrdered():
        counter = counter + 1
        shuffle(toSort)
    
    print counter
    return toSort
