import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def calculate_execution_time(arr):
    print("Before sorting: " + str(arr))
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    print("After sorting: " + str(arr))
    return end_time - start_time

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    execution_time = calculate_execution_time(arr)
    print("Execution Time: " + str(execution_time) + " seconds")
