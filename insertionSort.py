import copy

def insertionSort(inputArr):
    array = copy.deepcopy(inputArr)                                 #creates a copy of the array so the original is not modified
    length = len(array)                                             #gets the length of the array
    swapCount = 0
    for i in range(1, length):                                      #sorts through the entire array
        key = array[i]                                              #stores the original value in the key varriable
        j = i-1                                                     #j is one position to the left of the key
        while j >= 0 and key < array[j]:                            #loop that shifts elements until the key is in position
            array[j+1] = array[j]                                   #line that shifts element one to the right
            j -= 1                                                  #decraments position
            swapCount += 1                                          #incraments the swapcount
        array[j+1] = key                                            #puts the key into the proper position
    return array, swapCount
