from bubbleSort import bubbleSort
from quickSort import quicksort
from insertionSort import insertionSort
from heapSort import heapSort
import random

randArr = []
for i in range(30):
    randArr.append(random.randint(0, 1000))

stringArr = ["coconut", "Bananna", "apple", "mango", "cherry", "grape", "kiwi", "bananna"]


sortedArr = heapSort(randArr)[0]
print("original array: " + str(randArr))
print("sorted   array: " + str(sortedArr))
print("bubble sort required %s swaps" % bubbleSort(randArr)[1])
print("quick sort required %s swaps" % quicksort(randArr)[1])
print("insertion sort required %s swaps" % insertionSort(randArr)[1])
print("heap sort required %s swaps" % heapSort(randArr)[1])

#sorting strings (this is a WIP at the moment)
# sortedArr = bubbleSort(stringArr)[0]
# print("original array: " + str(stringArr))
# print("sorted   array: " + str(sortedArr))
# print("bubble sort required %s swaps" % bubbleSort(stringArr)[1])
# print("quick sort required %s swaps" % quicksort(stringArr)[1])


