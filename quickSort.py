import copy

def quicksort(inputArr):
    array = copy.deepcopy(inputArr)         # creates a copy of the array so the original is not modified
    low = 0
    high = len(array) - 1
    swapCount = quickSortInternal(array, low, high)
    return array, swapCount

def quickSortInternal(array, low, high):
    # calculates the middle index and sets the pivot equal to the value at that index
    pivot = array[int(low + (high-low)/2)]
    swapCount = 0

    i = low
    j = high
    while i <= j:
        #check until all values on the left are less than the pivot
        while array[i] < pivot:
            i += 1
        #check until all values on the right are greater than the pivot
        while array[j] > pivot:
            j -= 1
        #compare values and swap if needed; move iterator on both lists if swapped
        if i <= j:
            array[i], array[j] = array[j], array[i]
            swapCount += 1
            i += 1
            j -= 1
    #recursively calls the same operation on sub lists to the left and right
    #swap count is added in order to account for previous occurances
    if low < j:
        swapCount += quickSortInternal(array, low, j)
    if high > i:
        swapCount += quickSortInternal(array, i, high)

    return swapCount
