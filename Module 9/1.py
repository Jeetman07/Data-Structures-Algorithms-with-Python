# Homework: Data Structures & Algorithms with Python - Module 9 Sorting
# Name: [Your Name]

import random
import time

# Step 1: Create a data structure with 300 elements
data = [random.randint(1, 1000) for _ in range(300)]

# Step 2: Define sorting algorithms

# 1️⃣ Selection Sort
def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
                
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# 2️⃣ Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# 3️⃣ Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# Step 3: Measure time and print results

# Selection Sort
start = time.time()
sorted_selection = selection_sort(data)
end = time.time()
print("Selection Sort Time:", round(end - start, 6), "seconds")
print("Selection Sort Result (first 20 elements):", sorted_selection[:20], "...")

# Merge Sort
start = time.time()
sorted_merge = merge_sort(data)
end = time.time()
print("Merge Sort Time:", round(end - start, 6), "seconds")
print("Merge Sort Result (first 20 elements):", sorted_merge[:20], "...")

# Quick Sort
start = time.time()
sorted_quick = quick_sort(data)
end = time.time()
print("Quick Sort Time:", round(end - start, 6), "seconds")
print("Quick Sort Result (first 20 elements):", sorted_quick[:20], "...")