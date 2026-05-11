# ============================================================
# Session 3 | Notes
# Solving Hard-to-Solve Problems
# ============================================================

# ── KEY CONCEPTS ─────────────────────────────────────────────
# 1. iterables, iterators, generators
# 2. streaming vs loading
# 3. yield
# 4. HTS Problems (expo. & fatcorial)
# 5. RAG -Retrieved Augmented Generation

# ── PART 2: ITERABLE ─────────────────────────────────────────────────
# ── an object ppython can loop over
# ── ex.: str., list, file
# ── does NOT track position - just container
# ── Time: O(1) - Space: O(n)

it = iter(numbers)
print(next(it)) # pos 0 → 1
print(next(it)) # pos 1 → 2
print(next(it)) # pos 2 → 3

# iter() converts the iterable into an iterator
# iter() remembers its current postion
# next() moves it forward one step at a time


# ── PART 3: ITERATOR ─────────────────────────────────────────────────
# ── remembers its current position
# ── created wi/ '.iter'
# ── moves fwd w/ '.next()'
# ── once done, raises '.StopInteration'
# ── Time: O(1) Space: O(1)

it2 = iter(numbers)
print(next(it2)) # 1
print(next(it2)) # 2
print(next(it2)) # 3

# calling .'next()' after exhausted raises '.StopIteration'
    # crashes w/ '.next' when nothing left
# for loops catch these automaticaly - manual '.next()' doesn't

# ── PART 4: File streaming ───────────────────────
# a file object is already an iterator
# next(file) reads ONE line at a time
# The whole file is never loaded into memory
# Time: O(n) to read all lines — Space: O(1) per line

TEXT_FILE = "les_miserables.txt"

with open (TEXT_FILE, "r", encoding="utf-8") as file:
    first_line = next(file) # reads one line at a time
    second_line = next(file) # reads line 2 only

print(first_line)
print(second_line)

# Use streaming when:
# file too large to load
# only need one item at a time
# only need one iteration
# need immediate processing

# Use readlines() (load all) when:
# need to sort all lines
# need access index line [e.g. line 102]
# multiple iterations

# ── PART 5: yield & generators ───────────────────────
# a generator function uses yield instead of return
# yield gives single value, pauses & resumes on next()
# return gives one final value and stops function entirely
# Time: O(n) Space: O(1) - per item

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file: 
            line = line.strip() # removes space and \n from both ends
            if line != "":      # skip blank lines
                yield line      # give one line, pause, wait for next()

# for loop creates generator object and calls next() each iteration
# break stops after first line — rest of book never loaded

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

# ── O(n * m) — a new complexity
# n = number of lines in the file
# m = avg. line len (characters)
# "in" checks ea. character in the line → O(m)
# done for ea. line  → O(n*m) total
# Space:: O(m) - only one stripped line in memory at a times

# better than pre-loading lines
# readlines()  → Space: O(n*m) - entire file in memory
# generator  → Space: O(m) - one line at a time

# ── PART 7: stream vs. load ────────────────────────────
# STREAM stream:
# - file too large fore memory
# - need only one line at a time
# - only one pass needed
# - start processing immediately

# LOAD ALL when:
# - need sort lines
# - need index access [line 100]
# - multipass over same data
# - line comparison

# Session 3 | Part 3 | Exercise 03-03
# Tiny RAG — Retrieval Augmented Generation with Gemini

import os
from google import Generation

TEXT_FILE = "les_miserables.txt" # the file w/ one constant
QUESTION = "Who is Bishop Myriel?"
KEYWORDS = ["bishop", "myriel", "digne"]
MAX_LINES = 8 # send only 8 lines to gemini

# ── STEP 1: stream non-empty lines ───────────────────────────
# Time: O(n) — Space: O(1) per line

def useful_lines(path):
    # useful_lines() streams through the file one line at a time, 
    # strips whitespace, skips blank lines, and 
    # yields each useful line one at a time 
    # never holding more than one line in memory.
    """Yield non-empty lines from .txt file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

# yeilf give one val. pauses and waits for the next() call
# nothing stored line processed and handed off
# return would stop the function after the first lines
# then hand back that one val.

# ── STEP 2: retrieve relevant lines ──────────────────────────
# Time: O(n * m) — Space: O(k) where k is MAX_LINES

def retrieve_context (path, keyword, max_lines):
    """Find lines that match keywords, plus a few lines after ea. match."""
    matches =[]
    extra_lines = 0

    for line in useful_lines (path):
        line_lower = line.lower()

        if any (keyword in line_lower for keyword in keywords):
            matches.append(line)
            extra_lines = 2 # keeps 2 lines past
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines
            break

    return "\n".join(matches)


# ── STEP 3: build prompt and ask Gemini ──────────────────────
# retrieve only the relevant lines first
# send those lines as context — not the whole book
# Time: O(n * m) for retrieval — Space: O(k) for context

context = retrieve_context(TEXT_FILE, KEYWORDS, MAX_LINES)

prompt = f"""Use only this context to answer the question

Question:
{QUESTION}

Context:
{context}
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)

# ── RAG — RETRIEVAL AUGMENTED GENERATION ─────────────────────
# Find useful text first → send that text to Gemini → get answer
# LLMs don't know what's in your local files
# RAG gives them relevant context at the moment you ask

# Pipeline:
# 1. useful_lines()     → stream file, yield non-empty lines
# 2. retrieve_context() → keep lines w/ matching words + 2 after
# 3. build prompt       → inject retrieved lines as context
# 4. ask Gemini         → answer using only that context

# Why not send whole book?
# - context window has limit - cant fit entire novel
# - sending more text = more cost + more noise
# - RAG keeps the prompt small and targeted

# Time O(n * m) for retrieval
# Space: O(k) where k = MAX_LINES - nvr entire book

# ── PART 3 REFLECTION ────────────────────────────────────────
# 1. Which lines were retrieved?
#    Lines mentioning "fantine" + 2 lines after each match
#
# 2. Did Gemini have enough context?
#    Yes — enough to describe who Fantine is early in the book
#    but not her full story arc
#
# 3. What would improve this tiny RAG system?
#    - more keywords to catch more relevant lines
#    - increase MAX_LINES for wider context window
#    - use semantic search instead of keyword matching
#    - chunk by paragraph not by line


# Session 3 | Exercise 03-02
# Chunk summarizer — split Les Misérables into chunks
# send each chunk to Gemini, get a summary back

import os
from google import genai

MODEL_NAME = "gemini-2.5-flash"
TEXT_FILE = "les_miserables.txt"
CHUNK_SIZE = 30   # lines per chunk
MAX_CHUNKS = 3    # stop after 3 chunks to avoid API limits


# ── STEP 1: generator that yields chunks of lines ────────────
# Time: O(n * m) if all chunks processed
# Space: O(k * m) — only one chunk in memory at a time

def book_chunks(path, chunk_size=30, max_chunks=3):
    """Yield chunks of non-empty lines rom a txt file."""
    chunk = []
    chunks_sent = 0

    with open (path, "r", encoding = "utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue    # skip blank lines

            chunk.append(line)      # add line to current chunck

            if len(chunk == chunk_size):
                yield "\n".join(chunk)  # yield full chunk
                chunks_sent += 1
                chunk = []              # reset for next chunk

                if chunks_sent == max_chunks:
                    return              # stop - hit limit

    if chunk and chunks_sent < max_chunks:
        yield "\n".join(chunk)          # yields remain vals

# chunk = [] empties the list so the next 30 lines have clean contsiner to fill
# w/o it the next chunk would keep appending the same list
# it would grow by 30 each run instead of resetting to 0


# ── STEP 2: build the prompt for each chunk ──────────────────

def build_summary_prompt(chunk_text, chunk_number):
    """build a Gemini prompt for one chunk."
    return f"""You are summarizing one chunk from Les Misérables.

Return only valid JASON with these keys:
- chunk: the chunk number
- characters: important character names mentioned
- events: short event descriptions
- uncertainty: anything unclear

Rules: 
- Do not include Mardown fences
- Do not add commentary outside the JSON.
- if there are no clear events, use an empty list

Chunk number: {chunk_number}

Excerpt:
{chunk_text}


# ── STEP 3: ask Gemini ───────────────────────────────────────

def ask_gemini(prompt):
    """Send a prompt to Gemini and return the response text."""
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model = MODEL_NAME,
        contents = prompt,
    )
    return response.text

# ── STEP 4: loop through chunks and summarize ────────────────
# enumerate() gives us chunk_number starting at 1
# Time: O(n * m) local reading — Gemini calls are remote

for chunk_number, chunk_text in enumerate(
    book_chunks(TEXT_FILE, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS),
    start = 1
):
    prompt = build_summary_prompt(chunk_text, chunk_number)
    summary = ask_gemini(prompt)
    print(f"Chunk {chunk_number}")
    print(summary)
    print()

# ── EXERCISE 03-02: CHUNK SUMMARIZER ─────────────────────────
# book_chunks() - generator, yields 30 non-empty lines at a time
# build_summary_prompt() - build structured JSON prompt per chunk
# ask_gemini() - sends prompt, returns response text

# Space improvement over readlines():
# readlines() → O(n * m) — whole book in memory
# generator   → O(k * m) — only one chunk at a time

# 429 error = free tier daily limit hit (20 requests/day)