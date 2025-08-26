"""
Subject: Create 5 types of sorting function and compare the performance.
Conditions:
1. Create a function that generate 1000 words that consisted by alphabets and the length is between 3 to 8 characters.
2. Create sorting functions of Quick, Merge, Insertion, Selection, and Bubble.
3. Create a test function that outputs the results sorted in order of the fastest sort function.
4. Add a sorting option that shows descending or ascending orders of performance result. When running a test function, you must specify parameter values. The default is ascending.

Sorting performance test results: asc)
Quick Sort: 0.000625 sec
Merge Sort: 0.000758 sec
Insertion Sort: 0.008862 sec
Selection Sort: 0.009189 sec
Bubble Sort: 0.017930 sec

"""

import random
import string
import time
import sys

# Create 1000 random words that the length of the word is between 3 to 8
def generate_random_words(n=1000, min_len=3, max_len=8):
    words = []
    for _ in range(n):
        length = random.randint(min_len, max_len)
        word = ''.join(random.choices(string.ascii_letters, k=length))
        words.append(word)
    return words


# Common timer wrapper (Utilized like decorator)
def timed_sort(sort_func, arr):
    start = time.time()
    result = sort_func(arr)
    end = time.time()
    elapsed = end - start
    return result, elapsed


# 1. Selection Sort
def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# 2. Insertion Sort
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# 3. Bubble Sort
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# 4. Merge Sort
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 5. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Performance check function
def test_sort_performance(words, sort="asc"):
    sort_functions = {
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    performance = {}

    for name, func in sort_functions.items():
        times = []
        for _ in range(10):
            _, elapsed = timed_sort(func, words)
            times.append(elapsed)

        times.sort()
        trimmed = times[1:-1]  # Exclude the fastest and slowest result

        # Find a mean value. If list is even, get an average of two values.
        n = len(trimmed)
        if n % 2 == 1:
            median = trimmed[n // 2]
        else:
            median = (trimmed[n // 2 - 1] + trimmed[n // 2]) / 2

        performance[name] = median

    reverse = True if sort == "desc" else False
    sorted_performance = sorted(performance.items(), key=lambda x: x[1], reverse=reverse)
    return sorted_performance


# ㄸㅌ므ㅔㅣㄷ
if __name__ == "__main__":
    # Define a sorting parameter. Default is asc
    sort_order = "asc"
    if len(sys.argv) > 1:
        sort_order = sys.argv[1].lower()  #use the first parameter (asc / desc)

    words = generate_random_words(1000)
    results = test_sort_performance(words, sort=sort_order)

    print(f"Sorting performance test results: {sort_order})")

    for name, median_time in results:
        print(f"{name}: {median_time:.6f} sec")
