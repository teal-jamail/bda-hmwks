# Session 4 Part 2 Quiz (Pool and Parallel Image Processing)

## Question 1

What does `multiprocessing.Pool` mainly help with?

- Managing SQL connections
- Running the same function over many inputs in parallel
- Rotating images automatically
- Creating virtual environments

Answer: 2
Type: single
Time: 40
Explanation: `Pool` is designed for distributing similar tasks across worker processes.

## Question 2

What does `pool.map(func, data)` do?

- Calls `func` only once
- Applies `func` to each item in `data`
- Sorts `data` in place
- Creates output folders

Answer: 2
Type: single
Time: 35
Explanation: `map` runs the same function over each input item.

## Question 3

Why should each worker save to a unique output filename?

- To make files larger
- To avoid workers overwriting each other’s outputs
- To speed up imports
- To disable parallelism

Answer: 2
Type: single
Time: 40
Explanation: Unique filenames prevent collisions when multiple workers write files.

## Question 4

Which of the following is a good output naming pattern for this lab?

- `rotated.jpg` for every image
- `rotated_image_{idx}.jpg`
- `output.txt`
- `file`

Answer: 2
Type: single
Time: 35
Explanation: Indexed filenames are clear and collision-safe.

## Question 5

Why can this exercise benefit from parallel execution?

- It removes all image operations
- Images are independent tasks that can run concurrently
- It changes JPG to PNG automatically
- It avoids writing files

Answer: 2
Type: single
Time: 40
Explanation: Each image can be downloaded and processed independently.

## Question 6

What should you create before saving outputs?

- A database table
- Output folders (for example `images/` and `processed/`)
- A zip archive
- A YAML file

Answer: 2
Type: single
Time: 30
Explanation: Output directories must exist before files are written.

## Question 7

Which timer is best for elapsed-time benchmarking in this lab?

- `time.timezone`
- `time.sleep()`
- `time.perf_counter()`
- `os.getpid()`

Answer: 3
Type: single
Time: 30
Explanation: `perf_counter()` is high-resolution and suitable for timing.

## Question 8

A fair serial vs parallel comparison should use:

- Different URL sets
- The same URL list and same processing steps
- Fewer outputs in parallel
- No timing output

Answer: 2
Type: single
Time: 40
Explanation: Both modes must run equivalent work to compare meaningfully.

## Question 9

If parallel timing is not faster in one run, the best next step is:

- Assume multiprocessing is wrong
- Repeat runs and compare trends
- Delete timing code
- Remove image rotation

Answer: 2
Type: single
Time: 40
Explanation: Performance varies by network/system load; repeated runs are more reliable.

## Question 10

Which statement is most accurate?

- Pool-based parallelism is always faster for every workload
- Parallel speed depends on workload size and system overhead
- Serial always beats parallel
- Worker count never matters

Answer: 2
Type: single
Time: 40
Explanation: Real speedup depends on task characteristics and runtime overhead.
