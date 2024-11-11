import random
import time
import matplotlib.pyplot as plt

def generate_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]


def measure_time_ns(func, array):
    start_time = time.perf_counter_ns()
    func(array.copy())  
    end_time = time.perf_counter_ns()
    return end_time - start_time  

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr):
    max_val = max(arr) if arr else 0
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    i = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            arr[i] = num
            i += 1


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def experiment():
    sizes = [10, 100, 1000, 10000, 100000]  
    algorithms = {
        "Selection Sort": selection_sort,
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Counting Sort": counting_sort,
        "Shell Sort": shell_sort
    }
    
    results = {name: [] for name in algorithms.keys()}

    for size in sizes:
        for name, func in algorithms.items():
            array = generate_random_array(size)
            time_taken_ns = measure_time_ns(func, array)
            results[name].append(time_taken_ns)
    
    return sizes, results


sizes, timing_results = experiment()

first_five_algorithms = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
plt.figure(figsize=(10, 6))
for algo in first_five_algorithms:
    plt.plot(sizes, timing_results[algo], marker='o', label=algo)
plt.title("Time Complexity of First Five Sorting Algorithms")
plt.xlabel("Array Size")
plt.ylabel("Time (nanoseconds)")
plt.legend()
plt.yscale("log") 
plt.xscale("log")
plt.show()


last_two_algorithms = ["Counting Sort", "Shell Sort"]
plt.figure(figsize=(10, 6))
for algo in last_two_algorithms:
    plt.plot(sizes, timing_results[algo], marker='o', label=algo)
plt.title("Time Complexity of Last Two Sorting Algorithms")
plt.xlabel("Array Size")
plt.ylabel("Time (nanoseconds)")
plt.legend()
plt.yscale("log")
plt.xscale("log")
plt.show()


plt.figure(figsize=(12, 8))
for algo in timing_results.keys():
    plt.plot(sizes, timing_results[algo], marker='o', label=algo)
plt.title("Comparison of All Sorting Algorithms")
plt.xlabel("Array Size")
plt.ylabel("Time (nanoseconds)")
plt.legend()
plt.yscale("log")
plt.xscale("log")
plt.show()