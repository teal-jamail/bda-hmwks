# ── PART 1 Warm-up: multiprocess.Process ──────────────────────────────

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

    p1.start() # both started before either is joined
    p2.start()

    p1.join() 
    p2.join() # wait for both

    end2 = time.perf_counter()
    print(f"parallel time: {end2 - start2:.2f}s")

# ── PART 1: multiprocess.Process ──────────────────────────────────────────
# ── Instead of calling task("A", 2) direct wrap in Process object
#    tells python to 'run this in a seperate process'
# ── Then start() both process before either finished (run same time)
# ── then join() waits for both to complete b4 stop timer
# ── create process → start process → join process

# ── target=task passes function itself as an instruction
# ── target=task() would call the function in main process 
# ── b4 parallel execution starts and pass the result which in None
# ── parallel vs. sequential 
#    is about passing the function itself vs calling it rightnow

# ── args=("A",2) maps direct to the paramters of 'task'
# ── 'task' taks 'name' & 'seconds'
#    "A" becomes 'name' and '2' becomes 'seconds'

# ── 'join()' blocks main process and waits for that process to finish
# ── if call 'p1.start()' then immediately 'p1.join()'
# ── p2 cannot start until p1 finishes 
#    — back to serial execution

# ── 'if __name__ == "__main__":' is a guard:
#   'only run this block if file was run directly, 
#   not if it was imported by another process'
#   w/o every child process re-runs eaverything at top level

# ── 'mp.Process' — creates the child process
# ── 'if __name__ == "__main__":' 
#    protects main code from running inside every 
#    child process that gets spawned

# ── Serial - O(n): b/c ea. task runs sequentially - 
#    total time grows linearly
# ── Parallel - O(n/k): constant factor is k - notation O(n)
#    work split across k cores, plus overhead for spawn process

# ── PART 1 Excersice 1: multiprocess.Process ──────────────────────

import multiprocessing as mp
import random
import time

def bubble_sort(arr): 
    n = len(arr)
    for i in range (n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def generate_and_sort_numbers (n = 10000):
    numbers = [random.random() for _ in range (n)]
    bubble_sort(numbers)


def serial_runner(runs=3):
    start = time.perf_counter()
    process = []
    
    for i in range(runs):
        generate_and_sort_numbers()

    end = time.perf_counter()
    return end - start

def parallel_runner (runs=3):
    start = time.perf_counter()
    process = []

# loop 1 - create all processes
    for i in range(runs):
        p = mp.Process(target=generate_and_sort_numbers)
        process.append(p)

# loop 2 - start all processes
    for p in process:
        p.start()

# loop 3 - join all processes
    for p in process:
        p.join()

    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    serial_time = serial_runner (runs = 3)
    parallel_time = parallel_runner (runs = 3)
    print(f"Serial time: {serial_time: .2f}s")
    print(f"Parrallel time: {parallel_time: .2f}s")


# ── bubble_sort(arr)
#    repeatedly compares neighboring elements & swaps
#    modifies original list - no copy
# ── Time: O(n²)
#    potentially compares ea. against all others
# ── Space: O(1)
#    one var. in temp for swapping

# ── generate_and_sort_numbers(n=10000)
#    create list of 10k rando floats b/t 0-1
#    sorts via bubble sort - real computation

# ── serial_runner
#   simple loop calls generate_and_sort_numbers 3x
#   Sort 1 finishes, 2 starts, then 3
#   total time = sum of all 3

# ── parallel_runner - three loops
#    Loop 1: creates all 3 processes and appends to list
#    Loop 2: starts all 3 - run parallel
#    Loop 3: joins all 3 - main process waits for all to finish
#    Must be seperate b/c if start & join in same loop:
#    - wait for ea. process b4 start next

# ── Serial: O(n * n²) = O(n²) per task x num of runs
# ── Parallel: O(n²) - all runs at once; cost of one sort
# ── Space: O(1) - bubble.sort in place; no xtra memory


# ── PART 2: multiprocess.Pool ───────────────────
# ── Think: if do 'creat, start, join' for 100 process
#    need write 100 objects/loops; manually manage list

# ── Pool: automates processes
#    1: tell how many worker procesess
#    2: give func. & list of inputs
#    - automatically handles distribution, start, join 
# ── 'pool.map(func, list)': 
#    method applies func to ea. item on 'list' across processes
#    returns results in order

# ── Does parrellelism help when tasks waiting rather than computing?
#    Yes, when wait for network response not using CPU
#    idle waiting for data
# ── While process 1 waits for Image 1 to downlaod
#    Process 2 can wait for Image 2 to download
#    wait in parrallel
# ── Serial would wait for ea. sequentially
#    Total = sum of all wait times
# ── Parrallel all 10 wait at same time   
#    Total ≈ slowest single download
# ── Difference:
#    CPU-bound tasks compete for cores
#    I/O bound (like network downloads) compete for nothing

import multiprocessing as mp
import os
import time
import urllib.request
from PIL import Image

image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]

def download_and_rotate(item):
    # item is tuple (idx, url); first unpack
    idx, url = item
    # Step 1: download & save image to 'images/' folder
    urllib.request.urlretrieve(url, f"images/image_{idx}.jpg")
    # Step 2: open downloaded img w/ Pillow
    image = Image.open(f"images/image_{idx}.jpg")
    # Step 3: rotate 90 degrees & save to 'processed/' folder
    rotated = image.rotate(90, expand = True)
    rotated.save(f"processed/rotated_img_{idx}.jpg")

def serial_runner(urls):
    start = time.perf_counter()

    # build items & pair ea. URL w/ index start at 1
    items = list(enumerate(urls, start=1))
    # gives [(1, url1), (2, url2), (3, url3)...]

    for item in items:
        download_and_rotate(item)

    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")

def pool_runner(urls, workers=4):
    start = time.perf_counter()

    #    1: tell how many worker procesess
    #    2: give func. & list of inputs
    #    'with' pool auto closes and cleans after done
    items = list(enumerate(urls, start=1))
    # enumerate gives index and count begins at 1
    with mp.Pool(processes=workers) as pool:
            pool.map(download_and_rotate, items)

    end = time.perf_counter()
    print(f"Pool time: {end - start: .2f}s")

if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)
    serial_runner(image_urls)
    pool_runner(image_urls, workers=4)

# pool.map maps the func. to each item on list across process
# and returns results in order, this is automatic where as
# if did Process need to create object loops for ea. and 
# manually manage list

# ── Serial: O(n) - ea. image processes sequentially
# ── Pool: O(n/k) - n images split across k workers
# ── Space: O(n) - all image file handles exist atonce