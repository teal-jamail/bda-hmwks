# Part 2 - Incomplete dataset 
# Task 1: Find missing data point
with open("data/movies_incomplete/movies.csv", "r") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    for line_number, row in enumerate(reader, start=2):
        for column in fieldnames:
            if row[column] == "":
                print(f"Missing cell at row {line_number}, column {column}")
                break

# Task 2: Avg. of votes
with open("data/movies_incomplete/movies.csv", "r") as file:
    reader = csv.DictReader(file)

    total = 0.0
    count = 0

    for row in reader:
        try:
            votes = float(row["votes"])
            total += votes
            count += 1
        except(ValueError, KeyError):
            continue

print("Average votes:", total /  count if count > 0 else "No valid values") 
