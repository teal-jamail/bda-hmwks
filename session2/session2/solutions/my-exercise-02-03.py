# python3 solutions/my-exercise-02-03.py
# Session 2 Part 3 - Data Cleaning

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

# Step 1: Find missing values
for i, movie in enumerate(movies, start=1):
    for key, value in movie.items():
        if value.strip() == "":
            print (f"Record {i} missing field: {key}")

 
# Step 1b: Improved - check specific fields only
for i, movie in enumerate(movies, start = 1):
    if movie["music_by"].strip() == "":
        print(f"Record {i} missing field: music_by")
    if movie["year"].strip() == "":
        print(f"record {i} missing field: year")


# Step 2: Fix the missing values
if movies [0]["music_by"].strip() == "":
    movies [0]["music_by"] = "Joe Hisaishi"

if movies[1]["year"].strip() == "":
    movies[1]["year"] = "1989"

print(movies)


# Step 3: Save copy
original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy() for movie in movies]

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"

print("Original:", original_movies)
print("Cleaned:", cleaned_movies)

# Step 4: Save cleaned data to disk
import json

with open ("movies_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

print("Saved: movies_clean.json")


# Excersice Task 1:
import csv

with open("studio_ghibli_movies.csv", "r", encoding="utf-8", newline="") as file:
     reader = csv.DictReader(file)
     fieldnames = reader.fieldnames
     rows = []
     for row in reader:
        rows.append(row)

print("Excersice 1: Columns:", fieldnames)
print("Excersice 1: Total rows:", len(rows))

# Task 2: Find missing vals
print("\nMissing values:")
for line_number, row in enumerate(rows, start = 2):
    for column in fieldnames:
        if row[column].strip()=="":
            print(f"Row {line_number}, column {column}, title: {row['title']}")


# Task 3: Fix missing vals
year_fixes = {
    "Kiki's Delivery Service": "1989",
    "Ponyo": "2008",
}
music_fixes = {
    "Howl's Moving Castle": "Joe Hisaishi"
}

for row in rows:
    title = row["title"]

    if row["year"].strip()== "" and title in year_fixes:
        row["year"] = year_fixes[title]
    
    if row ["music_by"].strip () == "" and title in music_fixes:
        row["music_by"] = music_fixes[title]

print("Missing values fixed!")

# Task 4 - Calculate avg. year & count Miyazaki movies

# Task 4a: Avg. year
year = []
for row in rows:
    year_text = row["year"].strip()
    if year_text.isdigit():
        year.append(int(year_text))

if year:
    average_year = sum(year) / len(year)
    print(f"Avg. year: {average_year:.1f}")
else:
    print ("Avg. year: n/a")

# Task 4b: Count Miyazaki movies
miyazaki_count = 0
for row in rows:
    if "miyazaki" in row["director"].lower():
        miyazaki_count += 1

print("Miyazaki movies:", miyazaki_count)

# Task 5: Save clean rows to new .csv
with open("studio_ghibli_movies_clean.csv", "w", encoding= "utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print("Saved: studio_ghibli_movies_clean.csv")

# Task 6: re-check missing vals post-clean
print ("\nMissing vals post-clean:")
remaining = 0
for row in rows:
    for column in fieldnames:
        if row[column].strip() == "":
            remaining += 1
            print(f"Still missing: row {column}, title: {row['title']}")

print("remaining misisng vals:", remaining)

# Task 7: Complexity Summary
# Task 1 - Load rows: Time O(n), Space O(n) - stores all rows in memory
# Task 2 - Find missing: Time O(n * m), Space O(1)
# Task 3 - Fix missing: Time O(n), Space O(1)
# Task 4 - Average year & Miyazaki count: Time O(n), Space O(n) for years list
# Task 5 - Save cleaned CSV: Time O(n * m), Space O(1) extra
# Task 6 - Re-check missing: Time O(n * m), Space O(1)