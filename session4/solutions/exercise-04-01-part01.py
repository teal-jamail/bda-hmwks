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

    # TODO: call generate_and_sort_numbers() runs times
    # Note: while this TODO is not filled, timing is not meaningful.
    ...

    end = time.perf_counter()
    return end - start


def parallel_runner(runs=3):
    start = time.perf_counter()

    # Keep references to processes so we can join them later.
    processes = []

    # TODO: create runs processes
    # TODO: start each process
    # TODO: wait for each process to finish
    # Note: while this TODO is not filled, timing is not meaningful.
    ...

    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    serial_time = serial_runner(runs=3)
    parallel_time = parallel_runner(runs=3)

    print(f"Serial time: {serial_time:.2f}s")
    print(f"Parallel time: {parallel_time:.2f}s")
