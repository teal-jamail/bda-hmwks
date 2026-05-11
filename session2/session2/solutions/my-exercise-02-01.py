# python3 solutions/my-exercise-02-01.py
import csv

# Example 1: Read CSV rows as dictionaries
with open ("movies.csv", "r") as file:
    reader =csv.DictReader(file)
    for row in reader:
        print(row)

# Example 2: Print one named col
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        print(row["genres"])


# Example 3: Count rows using a counter
count = 0

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row ["year"] == "2020":
            count += 1

print("Num. movies from 2020:", count)


# Example 4: Find first match with break
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Action" in row["genres"]:
            print("First Action Movie:",row)
            break

# Exercise Task 1: Print field names using reader.fieldnames
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    print ("Task 1 - Header w/ .fieldnames", reader.fieldnames)

# Excercise Task2: Print first 5 rows
with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for i, row in enumerate (reader):
        if i == 5:
            break
        print("Task 2 - First 5 Rows", row)

# Excercise Task 3: Count movies from USA
count = 0

with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row ["country"] == "USA":
            count += 1

print("Task 3 - USA Movie Count", count)

# Task 4: Find/print first movie where genres is exactly Action
with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row ["genres"] == "Action":
            print("Task 4", row)
            break

# Task 5: Find first movie where Action appears inside genres
with open ("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Action" in row ["genres"]:
            print("Task 5", row)
            break

# Task 6: Benefit of DictReader over csv.reader
# DictReader lets you access columns by name e.g. row["genres"] 
# instead of by index e.g. row[4] - much more readable and less 
# error prone, especially when columns change position


# Task 7: Complexity summary
# Task 1 - fieldnames: Time O(1), Space O(c)
# Task 2 - first 5 rows: Time O(1), Space O(1)
# Task 3 - USA count: Time O(n), Space O(1)
# Task 4 - exact Action: Time O(n), Space O(1)
# Task 5 - contains Action: Time O(n), Space O(1)
