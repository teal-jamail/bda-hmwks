import csv
import json
import os
import re
from pathlib import Path
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
                "parts": [{"text": prompt}],
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


def extract_year(text):
    match = re.search(r"\b(18|19|20)\d{2}\b", text)
    if not match:
        return None
    return match.group(0)


def clean_name(text):
    # Keep first non-empty line and trim punctuation/spaces.
    for line in text.splitlines():
        candidate = line.strip().strip(".,;:!?\"'")
        if candidate:
            return candidate
    return None


def find_dataset_path():
    candidates = [
        Path("studio_ghibli_movies.csv"),
        Path(__file__).resolve().parent.parent / "studio_ghibli_movies.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def main():
    dataset_path = find_dataset_path()
    if dataset_path is None:
        raise FileNotFoundError(
            "studio_ghibli_movies.csv not found. Download it in session2 first."
        )

    rows = []
    with dataset_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    if not fieldnames:
        raise RuntimeError("CSV header not found.")

    filled_count = 0

    for row in rows:
        title = row.get("title", "").strip()
        year = row.get("year", "").strip()
        music_by = row.get("music_by", "").strip()

        if not year and title:
            prompt = (
                f'Return only the 4-digit release year for the Studio Ghibli movie "{title}". '
                "Output format: only 4 digits, no extra text."
            )
            ai_text = ask_gemini(prompt)
            parsed_year = extract_year(ai_text)
            if parsed_year:
                row["year"] = parsed_year
                filled_count += 1

        if not music_by and title:
            prompt = (
                f'Return only the composer full name for the Studio Ghibli movie "{title}". '
                "Output format: name only, no extra text."
            )
            ai_text = ask_gemini(prompt)
            parsed_name = clean_name(ai_text)
            if parsed_name:
                row["music_by"] = parsed_name
                filled_count += 1

    output_path = dataset_path.with_name("studio_ghibli_movies_ai_clean.csv")
    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    remaining_missing = []
    for i, row in enumerate(rows, start=2):
        for key, value in row.items():
            if value is None or value.strip() == "":
                remaining_missing.append((i, row.get("title", ""), key))

    print("Filled by AI:", filled_count)
    print("Saved:", output_path)

    if remaining_missing:
        print("Rows still missing values:")
        for line_no, title, key in remaining_missing:
            print(f"- line {line_no}: {title} -> {key}")
    else:
        print("No remaining missing values.")


if __name__ == "__main__":
    main()
