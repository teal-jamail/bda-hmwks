# Session 3 | Part 3 | Exercise 03-03
# Tiny RAG — Retrieval Augmented Generation with Gemini

import os
from google import genai

TEXT_FILE = "les_miserables.txt"
QUESTION = "Who is Fantine?"
KEYWORDS = ["fantine"]
MAX_LINES = 8

# ── STEP 1: stream non-empty lines ───────────────────────────
# Time: O(n) — Space: O(1) per line

def useful_lines(path):
    """Yield non-empty lines from .txt file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

# ── STEP 2: retrieve relevant lines ──────────────────────────
# Time: O(n * m) — Space: O(k) where k is MAX_LINES

def retrieve_context (path, keyword, max_lines):
    """Find lines that match keywords, plus a few lines after ea. match."""
    matches =[]
    extra_lines = 0

    for line in useful_lines (path):
        line_lower = line.lower()

        if any (keyword in line_lower for keyword in keyword):
            matches.append(line)
            extra_lines = 2 # keeps 2 lines past
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines:
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