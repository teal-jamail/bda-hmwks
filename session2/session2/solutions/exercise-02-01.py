import csv
import shutil
import subprocess
import tempfile
from pathlib import Path

MOVIES_PATH = Path("movies.csv")
INCOMPLETE_PATH = Path("data/movies_incomplete/movies.csv")


def download_dataset(repo_id, filename, target_path):
    if target_path.exists():
        return True

    target_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            subprocess.run(
                [
                    "hf",
                    "download",
                    repo_id,
                    filename,
                    "--repo-type",
                    "dataset",
                    "--local-dir",
                    temp_dir,
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            source_path = Path(temp_dir) / filename
            if not source_path.exists():
                return False
            shutil.copyfile(source_path, target_path)
    except Exception:
        return False

    return target_path.exists()


def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def print_main_dataset_answers(path):
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        print("Field names:")
        print(reader.fieldnames)

        print("\nFirst 5 data rows:")
        usa_count = 0
        first_exact_action = None
        first_contains_action = None

        for row_number, row in enumerate(reader, start=1):
            if row_number <= 5:
                print(row)

            if row["country"] == "USA":
                usa_count += 1

            if first_exact_action is None and row["genres"] == "Action":
                first_exact_action = row

            if first_contains_action is None and "Action" in row["genres"]:
                first_contains_action = row

    print("\nMovies from USA:", usa_count)
    print("\nFirst movie where genres is exactly Action:")
    print(first_exact_action if first_exact_action else "No exact Action match found.")
    print("\nFirst movie where Action appears inside genres:")
    print(first_contains_action if first_contains_action else "No Action match found.")

    # DictReader lets us use column names, which is clearer than numeric indexes.
    print("\nComplexity:")
    print("Field names: time O(1), space O(c)")
    print("First 5 rows: time O(1), space O(1)")
    print("USA count: time O(n), space O(1)")
    print("First-match searches: time O(n), space O(1)")


def print_incomplete_dataset_answers(path):
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames or []
        total_votes = 0.0
        vote_count = 0

        print("\nMissing data in incomplete dataset:")
        found_missing = False

        for line_number, row in enumerate(reader, start=2):
            for column in fieldnames:
                value = row.get(column)
                if value is None or value.strip() == "":
                    print(f"Missing cell at row {line_number}, column {column}")
                    found_missing = True

            vote = safe_float(row.get("votes"))
            if vote is not None:
                total_votes += vote
                vote_count += 1

        if not found_missing:
            print("No missing cells found.")

    print("\nAverage votes from incomplete dataset:")
    print(total_votes / vote_count if vote_count else "No valid vote values found.")
    print(
        "A naive script fails because missing values cannot be converted directly "
        "with float(). The fix is to skip or handle invalid values before converting."
    )


def main():
    if not download_dataset("Birkbeck/movies", "movies.csv", MOVIES_PATH):
        raise FileNotFoundError(
            "movies.csv not found. Run from session2 after installing huggingface_hub."
        )

    if not download_dataset(
        "Birkbeck/movies_incomplete",
        "movies.csv",
        INCOMPLETE_PATH,
    ):
        raise FileNotFoundError(
            "data/movies_incomplete/movies.csv not found. "
            "Download the incomplete dataset first."
        )

    print_main_dataset_answers(MOVIES_PATH)
    print_incomplete_dataset_answers(INCOMPLETE_PATH)


if __name__ == "__main__":
    main()
