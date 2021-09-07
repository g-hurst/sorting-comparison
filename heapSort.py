import copy

def heapSort(inputArr):
    array = copy.deepcopy(inputArr)       #creates a copy of the array so the original is not modified
    n = len(array)
    swapCount = 0

    #creates a maxheap starting from the last non leaf node
    for i in range(n // 2 - 1, -1, -1):
        swapCount += heapify(array, n, i)
    #extracts elements
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        swapCount += heapify(array, i, 0) + 1     #increases swapcount from the swap above and from reheaping
    
    return array, swapCount


#used to heapify a subtree rooted at index i
def heapify(arr, length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    swapCount = 0

    #check if left child index is in arr and left child > root
    if left < length and arr[left] > arr[largest]:
        largest = left
    #checks if rignt child index is in arr and right child > root
    if right < length and arr[right] > arr[largest]:
        largest = right
    #swaps the root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swapCount += 1

        #recursivly calls heapyify in order to order the rest of the heap and adds to the swapcount
        swapCount += heapify(arr, length, largest)  
    return swapCount