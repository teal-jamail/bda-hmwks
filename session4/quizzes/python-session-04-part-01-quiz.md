# Session 4 Part 1 Quiz (Serial vs Multiprocessing Basics)

## Question 1

What is the key difference between serial and parallel execution?

- Serial uses more memory
- Serial runs tasks sequentially; parallel can run tasks concurrently
- Parallel always uses threads only
- Parallel cannot run Python code

Answer: 2
Type: single
Time: 45
Explanation: Serial executes one task after another; parallel overlaps independent tasks.

## Question 2

In `multiprocessing.Process(target=foo)`, what is `target`?

- The path to a data file
- The function to execute in the child process
- The CPU core number
- The timeout value

Answer: 2
Type: single
Time: 40
Explanation: The target is the callable executed by each process.

## Question 3

Why do we call `join()`?

- To start a process
- To force faster execution
- To wait until a process finishes
- To duplicate results

Answer: 3
Type: single
Time: 40
Explanation: `join()` ensures the parent waits for child completion.

## Question 4

If a 1-second task runs 3 times serially, expected runtime is near:

- 1 second
- 2 seconds
- 3 seconds
- 5 seconds

Answer: 3
Type: single
Time: 35
Explanation: Serial runtime is roughly the sum of individual durations.

## Question 5

Why is `if __name__ == '__main__':` important with multiprocessing?

- It enables sorting
- It avoids repeated child process spawning issues
- It sets worker count automatically
- It imports modules faster

Answer: 2
Type: single
Time: 45
Explanation: It protects startup behavior for spawned processes.

## Question 6

Which timer is preferred for elapsed-time benchmarks here?

- `time.sleep()`
- `datetime.date.today()`
- `time.perf_counter()`
- `os.getpid()`

Answer: 3
Type: single
Time: 35
Explanation: `perf_counter()` is high-resolution for timing measurements.

## Question 7

Why can multiprocessing help CPU-heavy independent tasks?

- It changes O(n²) to O(1)
- It distributes work across CPU cores
- It removes all overhead
- It eliminates loops

Answer: 2
Type: single
Time: 45
Explanation: Multiple processes can run on multiple cores.

## Question 8

When might parallel execution be slower than serial?

- Always for any task
- For very small tasks with high process overhead
- Only when using integers
- Never

Answer: 2
Type: single
Time: 45
Explanation: Process startup/synchronization cost can dominate tiny workloads.

## Question 9

`multiprocessing.Process` creates:

- a new thread in the same process
- a separate OS process
- a generator object
- a file descriptor only

Answer: 2
Type: single
Time: 40
Explanation: Each `Process` is an independent process managed by the OS.

## Question 10

What makes a fair serial-vs-parallel benchmark?

- Different tasks for each mode
- Same workload and same environment for both modes
- Fewer data points in serial
- Printing less in parallel

Answer: 2
Type: single
Time: 45
Explanation: Fair comparison requires equivalent work under similar conditions.
