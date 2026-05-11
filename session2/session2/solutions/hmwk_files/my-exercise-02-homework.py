import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def ask_gemini(prompt, model_name="gemini-2.5-flash"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_name}:generateContent"
    )

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as err:
        if err.code == 429:
            raise RuntimeError(
                "Gemini rate/limit reached. Please wait a minute and try again."
            ) from err
        raise

    return data["candidates"][0]["content"]["parts"][0]["text"].strip()

# Test ask_gemini
answer = ask_gemini("What is 2 + 2? Answer with just the number.")
print(answer)

# python3 solutions/hmwk_files/exercise-02-homework.py

import csv

# Task 1: Load studio_ghibli_movies.csv
rows = []
with open("studio_ghibli_movies.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames 
    for row in reader:
        rows.append(row)
print("Task 1: Loaded rows:", len(rows))

# Tasks 2 & 3: Find/fill missing year vals w/ Gemini
filled_count = 0

for row in rows:
    if row["year"].strip() == "":
        title = row["title"]
        prompt = (
            f'Return only the 4-digit release year for the Studio Ghibli movie "{title}".'
            f'Output format: only 4 digits, no extra text.'
        )
        answer = ask_gemini(prompt)
        row["year"] = answer
        filled_count += 1
        print(f"Tasks 2/3: Filled year for {title}: {answer}")

# Tasks 4/5 - Find/fill missing 'music_by' vals
filled_count = 0

for row in rows:
    if row["music_by"].strip() == "":
        title = row["title"]
        prompt = (
            f'Return only the name of the person credited for music in the Studio Ghibli movie "{title}".'
            f'Output format: name only, no extra text.'
        )
        answer = ask_gemini(prompt)
        row["music_by"] = answer
        filled_count += 1
        print(f"Task 3/4: Filled music_by for {title}: {answer}")

# Task 6 — Save the cleaned dataset 
with open("studio_ghibli_movies_ai_clean.csv.", "w", encoding= "utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print("Task 6: Saved studio_ghibli_movies_ai_clean.csv")

# Task 7: Print summary/ re-check vals
print("\nMissing vals post-clean:")
remaining = 0 # counter starts
for row in rows:
    for column in fieldnames:
        if row [column].strip() == "": # check still empty after stripwhite
            remaining += 1 # adds 1 to the counter
            print(f"Still missing row {column}, title: {row['title']}")
            # prints col/movie w/ missing vals
print("Remaining missing vals:", remaining)    
# final count
