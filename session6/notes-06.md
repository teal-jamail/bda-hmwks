Session 6 - Threading, Mutex, Semaphore

--- CONCEPTS ---

* Thread: lightweight worker inside the same process, shares memory
* Process: seperate program w/ isolated memory (Sess 4)

* Race condition: two threads interleave read-update-write on shared memory
* Unpredictable result - depends on threading schedule

* Critical section: code touching shared state
* Mustn't be run by more that one thread at a time

* Mutex (lock): allows only one thread into the critical section at a time
* threading.Lock()

* Pattern: w/ lock
* critical section - only one thread access at a time

# --- EX. 1: Mutex---
* Module level:

from concurrent.futures import ThreadPoolExecutor
import threading

from faker import Faker

* Faker & Lock module level b/c all threads need share same lock object
- A new lock inside ea. function call then every thread would have own lock; 
    - nothing protected b/c ea. thread have own private lock and not block others
### Rule: one lock, defined once at top
### Rule: keep critical section as small as possible - too much locking kills parallelism

fake = faker = Faker()
write_lock = threading.Lock()

def generate_phrase(): # calls fake.sentence
    return fake.sentence(nb_words=6)

def save_phrase(index):
    phrase = generate_phrase()

    with write_lock: # Time O(1) # Space: O(1)
        with open("generated_phrases.txt", "a", encoding="utf-8") as file:
            file.write(f"Phrase {index}: {phrase}\n")

    print(f"Saved phrase {index}: {phrase}")

#### open file with "a" (append) mode
#### "w" would truncate file to empty ea. time thread opened it

# --- EX. 1 Main Block---  

if __name__ == "main":
    with open ("generated_phrases.txt", "w", encoding="utf-8"):
        pass

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(save_phrase, range (1, 11))
        # Time: O(n) # Space O(n)

    print("Done. Check generated_phrases.txt")

* 'executor.map' takes function 'save.phrase' & calls once for ea. val. in 'range(1,11)'
* calls 'save.phrase(1)' ... 'save.phrase(10)'; ea. in own thread all running concurrent up to 'max_workers' limit
* block until all 10 are done b4 moving past line

### Big O breakdown:
* 'range(1, 11)' = 10 vals - but if had 'n' phrases it would be 'n' calls

Therefore:'executor.map'
    Time: O(n) b/c submits and runs 'n' tasks
    Space: O(n) b/c executor holds 'n' futures in memory while they run

Ea. individual 'save_phrase' is O(1) Time & Space
    - b/c 1 line generated & 1 line written 
    - it = fixed coast regardelss input size

The lock itself is O(1)
    - aquire/release is constant-time 
    - wait depends on contention but operation itself is constant

### --- MUTEX PATTERN ---

- threading.Lock(): one thread at a time in critical section
- w/ lock: aquires on entry, releases on exit (even if error)
- keep critical section SMALL: wrap only shared resource access
- generate_Phrase() : NO lock, local memory only
- file write needs lock - shared resource

- 'executor.map(fn, iterable): calls fn once per iten concurrently
- block until all workers finished

- "a" = append to accumulate results
- "w" = truncate (use only b4 start of thread)

# --- Ex. 2: Semaphores---
* Semaphore is a generalisation of mutex
    - instead of 1 key, have N keys
    - up to N threads can be in critical section at once
    - while all N keys taken, next thread waits (ex: bathroom)
        - threading.Semaphores(4): 4 threads can access at once

### Decision rule: 
* Mutex: ehrn resource can be used by only 1 thread at a time
        - writing single file, updating counter
* Semaphore: resource has fixed capacity greater than 1
        - 4 concurrent API calls, 3 printers, 5 dwnld slots

### Formula:
- total time ≈ (n tasks / semaphore limit) x task duration
* 40 tasks/ 4 permits x 1s = ~10s (plus network overhead)

# Two coordination problems = two seperate objects
1. limiting concureent requests
2. protect shared results file
### Requires seperate locks
####    - Semaphore manages concurrency
####    - Lock manages exclusivity

with call_limit:          ← acquire semaphore
    make the request      ← protected by semaphore
    capture the result    ← still inside semaphore
                          ← semaphore released here
write result to file      ← outside semaphore, under write_lock

### Rule: hold semaphore for ONLY as long as using limited resource - immediately release when done so next thread can access (they gotta go number 2 real bad lol)

# --- SEMAPHORE PATTERN ---

* threading.Semaphores(n) - up to N threads into critical section at once
* mutex = semaphore w/ n=1
* use semaphore when resource has >1 capacity

#### two seperate objects for the two coordination problems
* 'call_limit' = Semaphore (4)     → controls concurrency
* 'write_lock' = Lock()            → controls file access
* hold semaphore for only the request, not file write
* release as soon as limited resource is done

* 02d in f-string = pad int. to 2 digit w/ leading zero
* range(1,41) give 40 starting with 1


# --- 06 Homework---
What are the four things each worker needs to do inside download_with_semaphore(url), in order?
1. Aquire dwnld seaphore - only 5 dwnlds run at once
2. Call download_video(url) - actual dwnld, return success or failure
3. Release semaphore - done w/ limited resource
4. write one result line to the result file - under file guard, so no overwrites