import csv

# Example 1: Read CSV rows as dictionaries
with open ("movies.csv", "r") as file:
    reader =csv.DictReader(file)
    # instead of 'csv.reader' that gives list
    # 'DictReader' gives dictionary for ea. row
    # Col. names become the keys
    for row in reader:
        print(row)
        # Ea. row is now a dict.
        # instead of row[4] to get to genres 
        # Use row["genres"]

# Big o:
    # - Time: O(n) - Read ea. row 1x
    # - Space: O(1) - One row at a time


# Example 2: Print one named col
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        # loops through ea. row 1x [ea. row dict]
        print(row["genres"])
        # Use col. names instead of row index

# Big O
# Time: O(n) - loops through ea. row 1x
# Space: O(1) - one row at a time


# Example 3: Count rows using a counter
count = 0
# starts counter at zero

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Loop through ea. row
        if row ["year"] == "2020":
            # check if 'year' col. is 2020
            # string comparison 
            count += 1
            # if matches +1 to the counter
print(count)

# Big O
# Time: O(n)-loops through ea. row 1x
# Space: O(1)- only one extra var. 'count'


# Example 4: Find first match with break
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        # loops ea. line one at a time
        if "Action" in row["genres"]:
            # Checks if "Action" appears anywhere in genres col.
            # use 'in' not '==' b/c might be multi 'Action, Thriller'
            print(row)
            break
            # when found print row and stop

# Big O:
# Time: O(n) - worst case Action is the last row
# Space: O(1) - only stores one row at a time


# Exercise Task 1: Print field names using reader.fieldnames
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    # rcreats DictReaders
    # reads header automatic
    print (reader.fieldnames)
    # fieldnames is a property of DictReader 
    # stores col. names from header row
    # Access w/o looping

# Big O:
# Time O(1) - reads header not entire file
# Space: O(c) - stores col. names ( c = num. cols.)

# Excercise Task 2: Print first 5 rows
with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate (reader):
    # enumerate gives row (i) & data together
        if i == 5:
        # when counter hits 5 rows 0-4 printed
        # break stops loop
            break
        print("Task 2 - Fisrt 5 Rows", row)
        # prints ea. row as dict.

# Big O
# Time: O(1) - reads exact 5 rows, file size doesnt matter
# Space: O(1) - stores only 1 row at a time


# Excercise Task 3: Count movies from USA
count = 0
# counter begins 0

with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
    # loops ea. row 1 at a time
        if row ["country"] == "USA":
            # check is country col. has "USA" exactly
            # str comparison
            count += 1
            # adds one each time found

print("Task 3 - USA Movie Count", count)
# prints final count after loop through entire file

# Big O
# Time: O(n) - loops through ea. row to count countries w/ USA
# Space: O(1) - only one extra var. 'count'


# Task 4: Find/print first movie where genres is exactly Action
with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row ["genres"] == "Action":
            # will get the one with ONLY 'Action' (==)
            print("Task 4", row)
            break

# Big O
# Time: O(n) - worst case exact 'Action' is last row
# Space: O(1) - stores only one raw at a time


# Task 5: Find first movie where Action appears inside genres
with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Action" in row ["genres"]:
            print("Task 5", row)
            break

# Big O
# Time: O(n) - worst case 'Action is last row
# Space: O(1) - stores just one row at a time


# Task 6: Benefit of DictReader over csv.reader
# DictReader lets you access columns by name e.g. row["genres"] 
# instead of by index e.g. row[4] - much more readable and less 
# error prone, especially when columns change position

# Part 2 - Incomplete dataset 
# Task 1: Find missing data point
with open("data/movies_incomplete/movies.csv", "r") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    # stores col names to loop through and check ea. cell

    for line_number, row in enumerate(reader, start=2):
        # loops through every row - enumerate starts 2 b/c 1st is head
        for column in fieldnames:
            # for ea. row loops every col. name
            if row[column] == "":
                # checks if val. in col. empty str
                print(f"Missing cell at row {line_number}, column {column}")
                break
                # prints where missing val and stops checking that row


# Task 2: Avg. of votes
with open("data/movies_incomplete/movies.csv", "r") as file:
    reader = csv.DictReader(file)

    total = 0.0     # total stores running sum
    count = 0       # count tracks valid vals

    for row in reader: # loops every row one at a time
        try:
            votes = float(row["votes"]) # converts votes to float
            total += votes  # adds to toal
            count += 1      # incremental count x1
        except(ValueError, KeyError): 
            # ValueError = can't convert to float
            # KeyError = col doesn't exist
            continue
            # if conversion fails (null val)-skip row

print("Average votes:", total /  count if count > 0 else "No valid values")
# Divides total by count for avg. 
# 'if count > 0' prevents divide by 0

# Big O
# Time: O(n) - loops every row
# Space: O(1) - stores only 2 extyra vars


# Part 3 - Data Cleaning

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
    # loops through ea movie dict
    # enumerate gives record num (i)
    # starting at 1 and the movie dict itself
    for key, value in movie.items():
        # for ea. movie, loops through every key-val pair
        # 'items ()' returns both key col name and val
        if value.strip() == "":
            # Checks if empty value
            # 'strip()' rremoves extra spaces first
            # "" just spaces counts as empty
            print (f"Record {i} missing field: {key}")
            # 'f' means f-str to put var direct inside {}

# Big O
# Time: O(n*m) - n records, m fields per record
# Space: O(1) - no extra storage

# Step 1b: Improved - check specific fields only
for i, movie in enumerate(movies, start = 1):
    if movie["music_by"].strip() == "":
        print(f"Record {i} missing field: music_by")
    if movie["year"].strip() == "":
        print(f"record {i} missing field: year")

# Instead of looping through every field as above;
# Check only necessary

# Big O
# Time: O(n) - loops through ea. record once w/ constant work
# Space: O(1)
    # Previous was O(n*m)

# Trade-offs:
# General version; works for any datasaet automatic
# Improved version: faster but need to know field names

# Step 2: Fix the missing values
if movies [0]["music_by"].strip() == "":
    # '.strip()' removes extra characters/whitespace
    movies [0]["music_by"] = "Joe Hisaishi"
    # checks if first movie's 'music_by' empty
    # if so fills in 
    # movies [0] first item on list

if movies[1]["year"].strip() == "":
    movies[1]["year"] = "1989"
    # checks if first movie's 'year' empty
    # if so fills in 
    # movies [0] first item on list

print(movies)

# Big O
# Time: O(1) - fixed number of checks regardless of size
# Space: O(1)


# Step 3: Save copy
original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy(for movie in movies)]
    # create 2 copies of list 
    # '.copy()' makes new dicts for ea. movie; 
    # so changes don't afftect another

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"
    # modifies only cleaned_movies

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"
    # modifies only cleaned movies

print("Original:", original_movies)
print("Cleaned:", cleaned_movies)

# Big O
# Time: O(n*m) - all fields copied from ea. record
# Space: O(n*m) - storing two full copies of data


# Step 4: Save cleaned data to disk
import json # for save json format

with open ("movies_clean.json", "w", encoding="utf-8") as file:
    # opens new 'movies_clea.json' in write "w" mode
    # Creates if non-existent
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)
        # 'json.dump' converts python object to json
        # writes direct to a file
        # 'cleaned_movies - list of dicts
        # 'ensure_ascii=False' - keeps characters or accents
        # 'indent=2'adds 2 spaces for readability (otherwise 1 line)
 print("Saved: movies_clean.json")

 # * Note: json.dump - write direct to file
        # json.dumps - returns s string; hence (s)


# Xersie 1
import csv

with open("studio_ghibli_movies.csv", "r", encoding="utf-8", newline="") as file:
     # 'newline' corrects line ends
     reader = csv.DictReader(file)
     fieldnames = reader.fieldnames
     # col names form header row

     rows = []
     for row in reader:
        rows.append(row)
        # loads all rows in memor (instead one row at a time)
        # can reuse data w/o open new file

print("Excersice 1: Columns:", fieldnames)
print("Excersice 1: Total rows:", len(rows))
# 'len(rows)' counts num. of rows

# Big O
# Time: O(n) - reads ea. row 1x
# Space: O(n) - stores everything in rows list


# Task 2: Find missing vals
print("/nMissing values:")
for line_number, row in enumerate(rows, start = 2):
    # starts looping ea. row at 2 (skips head)
    for column in fieldnames:
        # for ea. row loops ea. col name
        if row[column].strip()=="":
            # checks if val empty in col. after stripping spaces
            print(f"Row{line_number}, column {column}, title: {row['title']}")
          

# Task 3: Fix missing vals
year_fixes = {
    "Kiki's Delivery Service": "1989",
    "Ponyo": 2008,
}
music_fixes = {
    "Howl's Moving Castle": "Joe Hisaishi"
}
# two dicts storing known fixes
# movie title is the key & correct val is correct val

for row in rows: # loops entire dataset
    title = row["title"]
    # stores movie title for row to compare fixes dicts

    if row["year"].strip()== "" and title in year_fixes:
        row["year"] = year_fixes[title]
    # two conditionals: 
    # missing 'row["year"].strip()== ""'
    # have know fix 'year_fixes[title]'
    # if both true fills correct vals from 'year_fixes' dict
    
    if row ["music_by"].strip ( == "") and title in music_fixes:
        row["music_by"] = music_fixes[title]
    # same as above

print("Missing values fixed!")

# Big O
# Time: O(n) - loops ea. row 1x
# Space: O(1) extra - fixes dicts are fixed size

# Task 4a: Avg. year
year = []
for row in rows:
    year_text = row["year"].strip()
    if year_text.isdigit():
        # '.isdigit' checks if str contains nums only
        # returns t/f
        # check before convert to int
        years.append(int(year_text))

if years:
    average_year = sum(years) / len(years)
    print(f"Avg. year: {average_year:.1f}")
    # ':.1f' - format specifier, 
    # rnd '.1' decimal dispaly as float 'f'
else:
    print ("Avg. year: n/a")

# Task 4b: Count Miyazaki movies
miyazaki_count = 0
for row in rows:
    if "miyazaki" in row["director"].lower():
        # converts str to lowercase for casesensitive search
        miyazaki_count += 1

print("Miyazaki movies:", miyazaki_count)


# Task 5: Save clean rows to new .csv
with open("studio_ghibli_movies_clean.csv", "w", encoding= "utf-8", newline="") as file:
    # opens in "w" write mode and creates if non-existent

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # '.DictWriter' opposite '.DictReader'
    # write dicts to csvs
    # fieldnames tell which cols to write in what order

    writer.writerheader() # colnames 1st
    writer.writerows(rows) # writes all rows at once in one go

print("Saved: studio_ghibli_movies_clean.csv")

# Big O:
# Time: O(n*m) - write ea. row every col.
# Space: O(1)extra - data already in memory

# Task 6: re-check missing vals post-clean
print (/n"Missing vals post-clean:)
remaining = 0
# counter starts 0

for row in rows:
    # loops cleaned ds
    for column in fieldnames:
        if row[column].strip() == "":
            # check is still empty after strip whitespace
            remaining += 1
            # adds to the counter
            print(f"Still missing: row {column}, title: {row['title']}")
            # prints col & movie w/ missing val

print("remaining misisng vals:", remaining)
# prints final count

# Big O:
# Time: O(n*m) - checks ea. row every col
# Space: O(1) - just one counter var

# Session 2 HMWK (missing gemini scripts here)
# Task 1: Load studio_ghibli_movies.csv

rows = []
# empty list to store all rows
with open("studio_ghibli_movies.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames 
    # opens DS, creates Dictreader
    # Stores col. names in 'fieldnames' for later

    for row in reader:
        rows.append(row)
        # Loads ea. row into 'rows' list for multi-loop w/o re-open
print("Task 1: Loaded rows:", len(rows))

# Big O
# Time: O(n) - read ea. row 1x
# Space: O(n) - stores all rows in memory

# Tasks 2/3: Find/fill missing year vals w/ Gemini
filled_count = 0
# counter track gemini filled vals

for row in rows:
    if row["year"].strip() == "":
        # Loops ea. row to see if 'year' empty
        title = row["title"]
        # stores title to use in prompt

        prompt = (
            f'Return only the 4-digit release year for the Studio Ghibli movie "{title}".'
            f'Output format: only 4 digits, no extra text.'
        )
        # Build specific prompt asking Gemini for just the year
        # Strict format ez to store

        answer = ask_gemini(prompt)
        row["year"] = answer
        filled_count += 1
# Calls Gemini, gets answer, fills into row, adds to counter

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


# Task 7: Print summary/ re-check vals
print("\nMissing vals post-clean:")
remaining = 0 # counter starts
for row in rows:
    for column in fieldnames:
        if row [column].strip() == "": # check still empty after stripwhite
            remaining += 1 # adds 1 to the counter
            print(f"Still missing row {column}, title: {row['title']}")
            # prints col/movie w/ missing vals
print("Remaining missing vals:")    
# final count