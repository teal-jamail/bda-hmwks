# ── PART 1: multiprocess.Process
import time
import multiprocessing as mp 

def task(name, seconds):
    print(f"Task {name} started")
    time.sleep(seconds)
    print(f"Task {name} finished")

if __name__ == "__main__":
    # serial sections runs directly
    start = time.perf_counter()

    task("A", 2)
    task("B", 2)

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f}s")

# parallel section
    start2 = time.perf_counter()
    p1 = mp.Process(target=task, args=("A", 2))
    p2 = mp.Process(target=task, args=("B", 2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end2 = time.perf_counter()
    print(f"parallel time: {end2 - start2:.2f}s")

# python3 hmwk_solutions/exercise-04-01.py