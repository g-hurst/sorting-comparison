import copy

def bubbleSort(inputArr):
    array = copy.deepcopy(inputArr)                             #creates a copy of the array so the original is not modified
    length = len(array)                                         #gets the length of the array
    swapCount = 0
    for i in range(length-1):                                   #sorts through the entire array
        for j in range (0, length - i - 1):                     #sorts through the remaining elements from the last position
            if array[j] > array[j+1]:                           #checks to see if the next elemet is greater than the current one
                array[j], array[j+1] = array[j+1], array[j]     #swaps the position of the two elements
                swapCount += 1                                  #incraments the swapcount
    return array, swapCount
