import copy

def mergeSort(inputArr):
    array = copy.deepcopy(inputArr)   #creates a copy of the array so the original is not modified
    return mergeSortInternal(array)

def mergeSortInternal(array):
    swapCount = 0
    #checks the size of the array (this also stops the recursion)
    if len(array) > 1:
        #splits the array into a left and right array
        midIndex = len(array) // 2
        leftArr = array[:midIndex]
        rightArr = array[midIndex:]

        #recursivly calls mergesort to split the array into smaller chunks
        #incraments swapcount with the number of swaps that heppened in the recursion
        swapCount += mergeSortInternal(leftArr)[1] 
        swapCount += mergeSortInternal(rightArr)[1]

        #iterators for traversing arrays
        i = j = k = 0

        while i < len(leftArr) and j < len(rightArr):
            #adds the value from the leftArr to array and incraments index and swapcount
            if leftArr[i] < rightArr[j]:
                array[k] = leftArr[i]
                i += 1
                swapCount += 1
            else:
                #adds the value from the rightArr to array and incraments index and swapcount
                array[k] = rightArr[j]
                j += 1
                swapCount += 1
            #incraments the position in array
            k += 1

        #copy any of the remaining values in leftArr
        while i < len(leftArr):
            array[k] = leftArr[i]
            i += 1
            k += 1
            swapCount += 1
        #copy any of the remaining values in rightArr
        while j < len(rightArr):
            array[k] = rightArr[j]
            j += 1
            k += 1
            swapCount += 1
    return array, swapCount
