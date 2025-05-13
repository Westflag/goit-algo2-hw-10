import random
import time
import matplotlib.pyplot as plt
import numpy as np

# --- QuickSort Implementations ---

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # middle element as pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

# --- Performance Measurement ---

def measure_execution_time(sort_function, array, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = array.copy()
        start = time.perf_counter()
        sort_function(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return np.mean(times)
if __name__ == '__main__':
    array_sizes = [10_000, 50_000, 100_000, 500_000]
    randomized_times = []
    deterministic_times = []

    for size in array_sizes:
        test_array = [random.randint(0, 1000000) for _ in range(size)]
        rand_time = measure_execution_time(randomized_quick_sort, test_array)
        det_time = measure_execution_time(deterministic_quick_sort, test_array)
        randomized_times.append(rand_time)
        deterministic_times.append(det_time)
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

    # --- Visualization ---
    plt.figure(figsize=(8, 6))
    plt.plot(array_sizes, randomized_times, label="Рандомізований QuickSort")
    plt.plot(array_sizes, deterministic_times, label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
