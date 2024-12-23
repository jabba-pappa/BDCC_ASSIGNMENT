import time
import threading
import cProfile

# Merge function to combine sorted halves
def merge(left_half, right_half):
    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # Append any remaining elements
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    return merged

# Parallel merge sort using threading
def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Split the array into halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = []
    right_sorted = []

    # Create threads for parallel sorting
    left_thread = threading.Thread(target=lambda: left_sorted.append(parallel_merge_sort(left_half)))
    right_thread = threading.Thread(target=lambda: right_sorted.append(parallel_merge_sort(right_half)))

    # Start the threads
    left_thread.start()
    right_thread.start()

    # Wait for both threads to finish
    left_thread.join()
    right_thread.join()

    # Merge the sorted halves
    return merge(left_sorted[0], right_sorted[0])

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)

    # Measure execution time
    start_time = time.time()
    sorted_arr = parallel_merge_sort(arr)
    end_time = time.time()

    print("Sorted Array:", sorted_arr)
    print(f"Execution Time: {end_time - start_time} seconds")

    # Profile the parallel merge sort
    cProfile.run("parallel_merge_sort(arr)")
