import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Merge function to merge two halves
def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[middle + 1 + j]

    # Merge the temporary arrays back into arr[left..right]
    i = 0  # Initial index of the first subarray
    j = 0  # Initial index of the second subarray
    k = left  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Merge sort function
def merge_sort(arr, left, right):
    if left < right:
        # Find the middle point
        middle = left + (right - left) // 2

        # Sort first and second halves
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)

        # Merge the sorted halves
        merge(arr, left, middle, right)

# Test the merge sort on the array [5, 2, 4, 7, 1, 3, 2, 6]
arr = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
