import csv
import json
from pathlib import Path


def find_missing(rows, fieldnames):
    missing_counts = {name: 0 for name in fieldnames}
    missing_examples = {name: [] for name in fieldnames}

    for line_number, row in enumerate(rows, start=2):  # header is line 1
        for column, value in row.items():
            if value is None or value.strip() == "":
                missing_counts[column] += 1
                missing_examples[column].append((line_number, row.get("title", "")))

    return missing_counts, missing_examples


def print_missing_report(missing_counts, missing_examples):
    print("\nMissing counts by column:")
    has_missing = False
    for column, count in missing_counts.items():
        if count > 0:
            has_missing = True
            print(f"- {column}: {count}")

    if not has_missing:
        print("- none")
        return

    print("\nWhere values are missing:")
    for column, examples in missing_examples.items():
        if examples:
            print(f"\n{column}")
            for line_number, title in examples:
                print(f"  line {line_number}: {title}")


def mini_dictionary_tutorial(script_dir):
    print("=== Mini tutorial: dictionary clean ===")
    movies = [
        {
            "title": "Howl's Moving Castle",
            "year": "2004",
            "director": "Hayao Miyazaki",
            "music_by": "",
        },
        {
            "title": "Kiki's Delivery Service",
            "year": "",
            "director": "Hayao Miyazaki",
            "music_by": "Joe Hisaishi",
        },
    ]

    for i, movie in enumerate(movies, start=1):
        for key, value in movie.items():
            if value.strip() == "":
                print(f"Record {i} missing field: {key}")

    original_movies = [movie.copy() for movie in movies]
    cleaned_movies = [movie.copy() for movie in movies]

    if cleaned_movies[0]["music_by"].strip() == "":
        cleaned_movies[0]["music_by"] = "Joe Hisaishi"

    if cleaned_movies[1]["year"].strip() == "":
        cleaned_movies[1]["year"] = "1989"

    print("Original:", original_movies)
    print("Cleaned:", cleaned_movies)

    mini_output = script_dir / "movies_clean.json"
    with mini_output.open("w", encoding="utf-8") as file:
        json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

    print(f"Saved: {mini_output}")
    return cleaned_movies


def find_dataset_path(script_dir):
    candidates = [
        Path("studio_ghibli_movies.csv"),
        script_dir.parent / "studio_ghibli_movies.csv",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def main():
    script_dir = Path(__file__).resolve().parent
    mini_dictionary_tutorial(script_dir)

    print("\n=== Exercise: studio_ghibli_movies.csv clean ===")
    dataset_path = find_dataset_path(script_dir)
    if dataset_path is None:
        print(
            "Could not find studio_ghibli_movies.csv. "
            "Download it first in the session2 folder."
        )
        return

    rows = []
    with dataset_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    if not fieldnames:
        print("No columns found in CSV header.")
        return

    print("Columns:", fieldnames)
    print("Total rows:", len(rows))

    missing_counts, missing_examples = find_missing(rows, fieldnames)
    print_missing_report(missing_counts, missing_examples)

    year_fixes = {
        "Kiki's Delivery Service": "1989",
        "Ponyo": "2008",
    }
    music_fixes = {
        "Howl's Moving Castle": "Joe Hisaishi",
    }

    filled_values = 0
    for row in rows:
        title = row.get("title", "")

        if row.get("year", "").strip() == "" and title in year_fixes:
            row["year"] = year_fixes[title]
            filled_values += 1

        if row.get("music_by", "").strip() == "" and title in music_fixes:
            row["music_by"] = music_fixes[title]
            filled_values += 1

    print("\nFilled values:", filled_values)

    years = []
    for row in rows:
        year_text = row.get("year", "").strip()
        if year_text.isdigit():
            years.append(int(year_text))

    if years:
        average_year = sum(years) / len(years)
        print(f"Average year: {average_year:.1f}")
    else:
        print("Average year: n/a")

    miyazaki_count = 0
    for row in rows:
        if "miyazaki" in row.get("director", "").lower():
            miyazaki_count += 1
    print("Miyazaki-directed movies:", miyazaki_count)

    output_path = dataset_path.with_name("studio_ghibli_movies_clean.csv")
    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved cleaned dataset to: {output_path}")

    missing_after_counts, _ = find_missing(rows, fieldnames)
    remaining_missing = sum(missing_after_counts.values())
    print("Remaining missing values after cleaning:", remaining_missing)

    print("\nComplexity:")
    print("Load rows into memory: time O(n * m), space O(n * m)")
    print("Find missing values: time O(n * m), space O(m + k)")
    print("Fill known missing values: time O(n), space O(1)")
    print("Average year and director count: time O(n), space O(n) for the years list")
    print("Write cleaned CSV: time O(n * m), space O(1) extra")


if __name__ == "__main__":
    main()
