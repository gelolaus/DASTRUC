"""
Created by Angelo John Benedict Laus of SF231
Created on May 16, 2024
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n - i - 1):
            print('---')
            print(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)

def insertionSort(array):
    print(array)
    for a in range(1, len(array)):
        b = a
        while b > 0 and array[b] < array[b-1]:
            array[b-1],array[b]=array[b],array[b-1]
            b -= 1
            print(array)

Input = [int(x) for x in input("Enter values to sort (separated by a comma): ").split(', ')]
print(Input)

Algorithm = int(input("\nSort using?\n1. Bubble Sort\n2. Insertion Sort\n\nAnswer: "))

match Algorithm:
    case 1:
        print("Step by step process:\n")
        bubbleSort(Input)
        print("\nThe sorted values are:", Input)
        
    case 2:
        print("Step by step process:\n")
        insertionSort(Input)
        print("\nThe sorted values are:", Input)

# References: Video lesson provided by instructor.