#!/usr/bin/env python3
"""
AdaptSort: A Hybrid Sorting Algorithm
Author: Khushi Goyal
"""

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, left, right):
    mid = (left + right) // 2
    candidates = [(arr[left], left), (arr[mid], mid), (arr[right], right)]
    candidates.sort(key=lambda x: x[0])
    return candidates[1][1]

def random_pivot(arr, left, right):
    import random
    return random.randint(left, right)

def partition(arr, left, right, pivot_idx):
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_val:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def detect_runs(arr):
    """
    Detect ascending runs for potential stable merges.
    Returns list of (start, end) indices of runs.
    """
    runs = []
    n = len(arr)
    if n <= 1:
        runs.append((0, n - 1))
        return runs
    start = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            runs.append((start, i - 1))
            start = i
    runs.append((start, n - 1))
    return runs

def stable_merge_runs(arr, runs):
    """
    Merge runs stably if they cover a large fraction of the array.
    This function is a simplified placeholder.
    """
    # Implementation detail for stable merges omitted for brevity.
    pass

def adapt_sort(arr, left, right, T=16, pivot_choice='median3'):
    """
    Core AdaptSort recursion: partition-based for subarrays > T, insertion for subarrays ≤ T.
    Pivot choice can be 'median3' or 'random'.
    """
    n = right - left + 1
    if n <= T:
        insertion_sort(arr, left, right)
        return
    if pivot_choice == 'median3':
        pivot_idx = median_of_three(arr, left, right)
    else:
        pivot_idx = random_pivot(arr, left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)
    adapt_sort(arr, left, pivot_idx - 1, T, pivot_choice)
    adapt_sort(arr, pivot_idx + 1, right, T, pivot_choice)

def adapt_sort_main(arr, T=16, use_run_detection=False, pivot_choice='median3'):
    """
    Public entry point for AdaptSort, optionally using run detection to unify partial merges.
    """
    if use_run_detection:
        runs = detect_runs(arr)
        total_run_len = sum((r[1] - r[0] + 1) for r in runs)
        if total_run_len > 0.5 * len(arr):
            # If runs cover more than half the array, merge them stably
            stable_merge_runs(arr, runs)
            return arr
    adapt_sort(arr, 0, len(arr) - 1, T, pivot_choice)
    return arr
