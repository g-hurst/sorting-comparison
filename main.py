from bubbleSort import bubbleSort
from quickSort import quicksort
from insertionSort import insertionSort
import random

randArr = []
for i in range(30):
    randArr.append(random.randint(0, 1000))

stringArr = ["coconut", "Bananna", "apple", "mango", "cherry", "grape", "kiwi", "bananna"]


sortedArr = insertionSort(randArr)[0]
print("original array: " + str(randArr))
print("sorted   array: " + str(sortedArr))
print("bubble sort required %s swaps" % bubbleSort(randArr)[1])
print("quick sort required %s swaps" % quicksort(randArr)[1])
print("Insertion sort required %s swaps" % insertionSort(randArr)[1])

# sortedArr = bubbleSort(stringArr)[0]
# print("original array: " + str(stringArr))
# print("sorted   array: " + str(sortedArr))
# print("bubble sort required %s swaps" % bubbleSort(stringArr)[1])
# print("quick sort required %s swaps" % quicksort(stringArr)[1])


