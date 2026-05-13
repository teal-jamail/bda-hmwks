import multiprocessing as mp
import time


def task(name, seconds):
    print(f"Task {name} started")
    time.sleep(seconds)
    print(f"Task {name} finished")


def serial_runner():
    print("\n--- Serial Execution ---")
    start = time.perf_counter()

    task("A", 2)
    task("B", 2)

    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")


def parallel_runner():
    print("\n--- Parallel Execution ---")
    start = time.perf_counter()

    p1 = mp.Process(target=task, args=("A", 2))
    p2 = mp.Process(target=task, args=("B", 2))

    p1.start()
    p2.start()

    # Join ensures we measure full task completion, not just process startup.
    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Parallel time: {end - start:.2f}s")


if __name__ == "__main__":
    serial_runner()
    parallel_runner()
