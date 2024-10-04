from typing import List

######### Scenarios ##########
# Best : an already sorted array
# Average : array with random numbers
# Worst : array with descending order


### Time Complexity ###
# Best : O(n)
# Average : O(n²)
# Worst : O(n²)
### Idea ###
# Compare the current element at index i to its predecessors.
# If the current element is smaller, swap it with element greater than it and before it in order
def insertion_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array


### Time Complexity ###
# Best : O(n²)
# Average : O(n²)
# Worst : O(n²)
### Idea ###
# Finding the minimum element from the unsorted part and put it at the beginning
def selection_sort(array: List[int]) -> List[int]:
    sorted_array = []
    for i in range(len(array)):
        min_val = min(array)
        min_idx = array.index(min_val)
        del array[min_idx]
        sorted_array.append(min_val)
    return sorted_array


### Time Complexity ###
# Best : O(n²)
# Average : O(n²)
# Worst : O(n²)
### Idea ###
# Compare each element in the array with its successor and swap the two elements if they are not in proper order
def bubble_sort(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array


### Time Complexity ###
# Best : O(n log n)
# Average : O(n log n)
# Worst : O(n²)
### Idea ###
# Pick an element as pivot and partition the given array around the picked pivot.
# Each element after the pivot must be greater and elements before it are lesser.
def quick_sort(array: List[int], first_idx: int, last_idx: int):
    if first_idx < last_idx:
        pivot = i = first_idx
        j = last_idx
        while i < j:
            while array[i] < array[pivot] and i < last_idx:
                i += 1
            while array[j] > array[pivot]:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        array[pivot], array[j] = array[j], array[pivot]
        quick_sort(array, first_idx, j - 1)
        quick_sort(array, j + 1, last_idx)


### Time Complexity ###
# Best : O(n log n)
# Average : O(n log n)
# Worst : O(n log n)
### Idea ###
# Find the middle point to partition the array into two halves, then call merge_sort for each half.
# Merge the two sorted halves.
def merge_sort(array: List[int], low: int, mid: int, high: int):
    n1, n2 = mid - low + 1, high - mid
    array1, array2 = [0] * n1, [0] * n2
    for i in range(n1):
        array1[i] = array[low + i]
    for j in range(n2):
        array2[j] = array[mid + 1 + j]
    i, j, k = 0, 0, low
    while i < n1 and j < n2:
        if array1[i] <= array2[j]:
            array[k] = array2[j]
            i += 1
        else:
            array[k] = array1[i]
            j += 1
        k += 1
    while i < n1:
        array[k] = array1[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = array2[j]
        j += 1
        k += 1


def partition(array: List[int], low: int, high: int):
    if low < high:
        mid = (low + (high - 1)) // 2
        partition(array, low, mid)
        partition(array, mid + 1, high)
        merge_sort(array, low, mid, high)
