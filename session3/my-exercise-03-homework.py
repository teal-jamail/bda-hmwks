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

            if len(chunk) == chunk_size:
                yield "\n".join(chunk)  # yield full chunk
                chunks_sent += 1
                chunk = []              # reset for next chunk

                if chunks_sent == max_chunks:
                    return              # stop - hit limit

    if chunk and chunks_sent < max_chunks:
        yield "\n".join(chunk)          # yields remain vals



# ── STEP 2: build the prompt for each chunk ──────────────────

def build_summary_prompt(chunk_text, chunk_number):
    """Build a Gemini prompt for one chunk."""
    return f"""You are summarizing one chunk from Les Misérables.

Return only valid JSON with these keys:
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
"""

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

# 429 error = free tier daily limit hit (20 requests/day)

# ── CHUNK SUMMARIZER ─────────────────────────
# book_chunks() - generator, yields 30 non-empty lines at a time
# build_summary_prompt() - build structured JSON prompt per chunk
# ask_gemini() - sends prompt, returns response text

# Space improvement over readlines():
# readlines() → O(n * m) — whole book in memory
# generator   → O(k * m) — only one chunk at a time

# ── HOMEWORK REFLECTION ───────────────────────────────────────
# 1. Which tasks were best solved with streaming?
#    Counting lines, finding first match, building chunks —
#    anything needing only one pass with no indexing
#
# 2. Which tasks required loading all data?
#    Sorting lines, accessing by index e.g. lines[100],
#    comparing lines against each other
#
# 3. Why is a generator with yield still an iterator?
#    Because it remembers its position and produces values
#    one at a time via next() — it just uses yield to do it
#
# 4. When does yield save memory compared with readlines()?
#    Always when you only need one item at a time —
#    readlines() is O(n*m) space, yield is O(m) per item
#
# 5. Why is sending the whole book to Gemini in one prompt bad?
#    Context window has a hard limit — the book won't fit
#    More tokens = more cost and more noise in the answer
#    RAG solves this by sending only relevant chunks
