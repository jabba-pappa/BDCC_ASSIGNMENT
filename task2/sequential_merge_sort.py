import time
import cProfile

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

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    print(f"Sorted array: {arr}")
    print(f"Execution Time: {end_time - start_time} seconds")

    cProfile.run("merge_sort(arr)")
