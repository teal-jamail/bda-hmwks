import multiprocessing as mp
import random
import time


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def generate_and_sort_numbers(n=10000):
    numbers = [random.random() for _ in range(n)]
    bubble_sort(numbers)


def serial_runner(runs=3):
    start = time.perf_counter()

    for _ in range(runs):
        generate_and_sort_numbers()

    end = time.perf_counter()
    return end - start


def parallel_runner(runs=3):
    start = time.perf_counter()

    # Track processes so we can join all of them before stopping the timer.
    processes = []
    for _ in range(runs):
        p = mp.Process(target=generate_and_sort_numbers)
        p.start()
        processes.append(p)

    # join() blocks until each child process completes.
    for p in processes:
        p.join()

    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    serial_time = serial_runner(runs=3)
    parallel_time = parallel_runner(runs=3)

    print(f"Serial time: {serial_time:.2f}s")
    print(f"Parallel time: {parallel_time:.2f}s")
