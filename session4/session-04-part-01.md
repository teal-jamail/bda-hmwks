### Session 4 | Part 1

> In Part 1, you will build multiprocessing programs from scratch and compare them to serial execution.

#### 1. Goal

You will:

- explain serial execution vs process-based parallel execution
- create, start, and join processes with `multiprocessing.Process`
- pass arguments into process target functions
- benchmark runtimes with `time.perf_counter()`

#### 2. Prerequisites

Before starting:

1. In Visual Studio Code terminal, update your local repository.

```bash
git pull origin main
```

If `git pull` fails because of local changes, use one of these paths:

Keep your work (recommended):

```bash
git stash push -m "session4-wip"
git pull origin main
git stash pop
```

Discard your local changes in `session4` only (use with care):

```bash
# Run this only from inside the session4 folder.
# Check first (it should end with `/bda/session4`):
pwd
git fetch origin
git restore --source origin/main --worktree --staged -- .
```

2. Open the `session4` folder in Visual Studio Code and in terminal.
3. Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

4. If `requirements.txt` is missing, create it in `session4/` with:

```txt
requests==2.32.3
Pillow
quizmd
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Basics you should know

- serial execution: tasks run one after another
- parallel execution: tasks can run at the same time
- process: an independent Python interpreter with separate memory
- `start()`: starts a child process
- `join()`: waits for a process to finish
- `time.perf_counter()`: high-resolution timer for benchmarking

#### 4. Create your first multiprocessing file

Before benchmarking, it helps to understand the basic time values we use:

- day/time (human-readable) helps us log when something ran
- Unix timestamp helps us store machine-friendly time values
- `time.perf_counter()` is best for measuring elapsed runtime

Quick warm-up:

Create `session4/solutions/exercise-04-00-time.py`, add this code, and run it.

```python
from datetime import datetime
import time

now = datetime.now()

print(f"Day: {now.strftime('%A')}")
print(f"Time: {now.strftime('%H:%M:%S')}")
print(f"Timestamp: {time.time():.2f}")
```

Run:

```bash
python3 solutions/exercise-04-00-time.py
```

Now create your first serial timing example.

Create `session4/solutions/exercise-04-01.py`, add this code, and run it.

```python
import time

def task(name, seconds):
    print(f"Task {name} started")
    time.sleep(seconds)
    print(f"Task {name} finished")


start = time.perf_counter()

task("A", 2)
task("B", 2)

end = time.perf_counter()
print(f"Total time: {end - start:.2f}s")
```

Run:

```bash
python3 solutions/exercise-04-01.py
```

Expected idea: serial execution should take about the sum of both sleeps (often around 4 seconds, but exact timing varies by machine/load).

Checkpoint question:

How long should this serial program take to run?

<details>
<summary>Show answer</summary>

About 4 seconds in most runs.

Why: the code runs two `time.sleep(2)` calls one after the other, so total serial time is close to `2 + 2 = 4` seconds (plus small overhead).

</details>

#### 5. Compare with multiprocessing execution

In the same file, replace the code with this multiprocessing version:

```python
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

    p1.join()
    p2.join()

    end = time.perf_counter()

    print(f"Parallel time: {end - start:.2f}s")


if __name__ == "__main__":
    serial_runner()
    parallel_runner()
```

Run again:

```bash
python3 solutions/exercise-04-01.py
```

Expected idea: parallel time should usually be significantly lower than serial time (often near 2 seconds here, but exact timing varies).

Checkpoint question:

How long should this multiprocessing version take, and why is it usually faster than the serial one?

<details>
<summary>Show answer</summary>

About 2 seconds in most runs.

Why: both tasks sleep for 2 seconds, but they run in separate processes at the same time, so total time is closer to the longest single task instead of the sum.

</details>

#### 6. Exercise

This exercise focuses on CPU-heavy workload with bubble sort. Create and complete this file: `session4/solutions/exercise-04-01-part01.py`.

* This script compares **serial** and **parallel** execution. It generates random numbers, sorts them using bubble sort, and measures how long the work takes.

You will need to complete the `serial_runner()` and `parallel_runner()` functions to see whether running the sorting tasks in parallel is faster.

> [!TIP]
>
> Due to the small size of the tasks, the serial version may sometimes be faster. 
>
> This is expected because parallel processing introduces extra overhead for creating and managing processes. 
>
> In general, the heavier the computation, the more beneficial parallel processing becomes.

```python
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

    end = time.perf_counter()
    return end - start

def parallel_runner(runs=3):
    start = time.perf_counter()

    processes = []

    # TODO: create runs processes
    # TODO: start each process
    # TODO: wait for each process to finish

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    serial_time = serial_runner(runs=3)
    parallel_time = parallel_runner(runs=3)

    print(f"Serial time: {serial_time:.2f}s")
    print(f"Parallel time: {parallel_time:.2f}s")
```

Complete this exercise in order:

1. Fill `serial_runner(runs=3)` to call `generate_and_sort_numbers()` exactly `runs` times.
2. Fill `parallel_runner(runs=3)` to create one process per run.
3. Start all processes, then `join()` all processes.
4. Run the file and compare serial vs parallel times.

#### 7. Quiz

```bash
quizmd quizzes/python-session-04-part-01-quiz.md
```
