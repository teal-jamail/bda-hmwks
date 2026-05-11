# Session 3 | Part 1 | Exercise 03-01
# Iterables, iterators, generators, streaming vs loading

# ── PART 1: Iterables and iterators ──────────────────────────────────────────

numbers = [1, 2, 3]

# A list is an iterable — Python can loop over it
for number in numbers:
    print(number)


# Session 3 | Part 1 | Exercise 03-01
# Iterables, iterators, generators, streaming vs loading

# ── PART 1: interable ─────────────────────────────────
# ── lists NOT iterable - pythons loops over
# ── position NOT tracked, container
# ── Time: O(n) - Space: O(n)

numbers = [1,2,3]

for number in numbers:
    print(number)

# ── PART 2: interator ───────────────────────────────
# iter() converts the iterable into an iterator
# iter() remembers its current postion
# next() moves it forward one step at a time
# Time: O(1) per next() - Space: O(1)

it = iter(numbers)
print(next(it)) # pos 0 → 1
print(next(it)) # pos 1 → 2
print(next(it)) # pos 2 → 3

# ── PART 3: StopIteration ───────────────────────────────
# calling .'next()' after exhausted raises '.StopIteration'
# for loops catch these automaticaly - manual '.next()' doesn't
# Time: O(1) Space: O(1)

it2 = iter(numbers)
print(next(it2)) # 1
print(next(it2)) # 2
print(next(it2)) # 3
# print(next(it2)) # StopIteration - nothing left
# crashes w/ '.next' when nothing left

# ── PART 4: File streaming ───────────────────────
# a file object is already an iterator
# python reads one line at a time - nvr loads entire file
# Time: O(n) Space: O(1)

TEXT_FILE = "les_miserables.txt"

with open (TEXT_FILE, "r", encoding="utf-8") as file:
    first_line = next(file) # reads one line at a time
    second_line = next(file) # reads line 2 only

print(first_line)
print(second_line)


# ── PART 5: yield & generators ───────────────────────
# a generator function uses yield instead of return
# yield gives single value, pauses 7 continue later
# return gives one final value and stops function entirely
# Time: O(n) Space: O(1) - per item

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip() # removes space and \n from both ends
            if line != "":      # skip blank lines
                yield line      # give one line, pause, wait for next()

# print only first non-empty line then stop 
for line in non_empty_lines(TEXT_FILE):
    print(line)
    break

# ── PART 6: Exercise — count lines containing a word ─────────
# Time: O(n*m) - n lines, m avg. line len for 'in' check
# Space: O(m) - only one stripped line in memory at a time

target = "Jean"
count = 0

for line in non_empty_lines(TEXT_FILE):
    if target in line:
        count += 1

print(count)

# ── PART 7: When to load all data ────────────────────────────
# stream not always enough
# load all when: sort, index, multi. pass
# Time: O(n) - Space: O(n*m) - entire file in memory

with open(TEXT_FILE, "r", encoding = "utf-8") as file:
    lines = file.readlines()

print(lines[100]) # diect index access - needs all line pre-load