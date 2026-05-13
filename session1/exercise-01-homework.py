# python3 session1/exercise-01-homework.py
# Task 1: Load dataset 
import csv

FILE_PATH = "session1/movies.csv"

# Task 2: Print row/col count
with open (FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader) #skip header

    num_cols = len(header)
    num_rows = 0
    for row in reader:
        num_rows += 1

print("Task 2: Number of data rows:", num_rows)
print("Task 2: Number of columns:", num_cols)

# Data rows: 1000
# Columns: 14

# Task 3: Print first 3 rows w/ header
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 3:
            break
        print("Task 3:", row)

# Complexity:
# Time: O(1) - reads exact 3 rows regardless of size
# Space: O(1) - stores only 1 row at a time

# Task 4: Find & print first 'Action' movie in 'genres'
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if "Action" in row[4]:
            print("Task 4:", row)
            break

# Complexity:
# Time: O(n) - worst case only one 'Action" at last index
# Space: O(1) - stores only 1 row at a time

# Task 5: Compute avg. 'rating_imbd'
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    total = 0.0
    count = 0

    for row in reader:    
        try:
            rating = float(row[5])
            total += rating
            count += 1
        except (ValueError, IndexError):
            continue # skip if row invalid/null

print("Task 5 - Average rating_imdb:", total/count if count > 0 else "No valid values")

# Complexity:
# Time: O(n) - worst case only one 'Action" at last index
# Space: O(1) - stores only 1 row at a time

# Task 6: Compute avg. of one or more cols
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    total = 0.0
    count= 0
    for row in reader:
        try: 
            metascore = float(row[13])
            total += metascore
            count += 1
        except (ValueError, IndexError):
            continue

print("Task 6 - Average metascore:", total/count if count > 0 else "No valid values")

# Task 7: Count how many movies have rating_imdb >= 8.0.
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    high_rating_count = 0
    for item in reader:
        try:
            rating = float(row[5])
            if rating >= 8.0:
                high_rating_count += 1
        except (ValueError, IndexError):
            continue

print("Task 7 - 8+ Rating", high_rating_count)

# Task 8: Report complexit for tasks 4 & 5
    # T4 - First-match search (find Action movie):
    # Time: O(n) - worst case only one 'Action" at last index
    # Space: O(1) - stores only 1 row at a time

    # T5 - Average computation (rating_imdb):
    # Time: O(n) - loops through every row to compute avg.
    # Space O(1) - store total/count cars - not entire

## Homework (Session 1)
- File: `session1/exercise-01-homework.py`
- Status: completed
- Notes:
  - computed averages for rating and one additional numeric column
  - handled missing or invalid values safely during computations