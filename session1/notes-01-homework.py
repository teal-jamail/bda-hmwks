# Task 1: Load dataset 
import csv

FILE_PATH = "session1/movies.csv"

# Task 2: Print row/col count
with open (FILE_PATH, "r", newline="", encoding="utf-8") as file:
    # opens, 'r'-read only, 'newline'-line endings, 'encoding...'- special characters
    reader = csv.reader(file)
    header = next(reader) #skip header
        # takes first row and moves past to loop only data
    num_cols = len(header)
        # counts num of cols by checking num items in header row
    num_rows = 0
    for row in reader:
        num_rows += 1
            # counts each data row by adding 1 ea. time through loop

print("Number of data rows:", num_rows)
print("Number of columns:", num_cols)

# Task 3: Print first 3 rows w/ header
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        # enumerate tracks row num
        if i == 3:
            break
            # stops before 4th row
        print("Task 3:", row)

# Complexity:
# Time: O(1) - reads exact 3 rows regardless of size
# Space: O(1) - stores only 1 row at a time

# Task 4: Find & print first 'Action' movie in 'genres'
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
        # skips header
    for row in reader:
        # loops rows
        if "Action" in row[4]:
            # checks if genres (row 4) has 'Action'
            print("Task 4:", row)
            break

# Complexity:
# Time: O(n) - worst case only one 'Action" at last index
# Space: O(1) - stores only 1 row at a time

# Task 5: Compute avg. 'rating_imbd'
with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) # skips header

        total = 0.0 # b/c decimal
        count = 0
            # two vars track running total & counts valid ratings

    for row in reader:    
        try: 
            rating = float(row[5])
        # 'try' then converts rating col (row 5) to decimal
            total += rating
            count += 1
            # if works adds to total & increment count
        except (ValueError, IndexError):
            continue # skip if row invalid/null

print("Task 5 - Average rating_imdb:", total/count if count > 0 else "No valid values")
    # divides total count to get avg.
    # 'if count > 0' prevents div. by 0 if no valid rating

# Complexity:
# Time: O(n) - worst case only one 'Action" at last index
# Space: O(1) - stores only 1 row at a time

# Task 6: Compute avg. of one or more cols (same as above)
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

    high_rating_count = 0 # start count at 0
    for item in reader:
        try:
            rating = float(row[5]) # convert ratings to decimal
            if rating >= 8.0: # check if rating 8 or above
                high_rating_count += 1 3 if yes add 1 to count
        except (ValueError, IndexError): #skip null
            continue

print("Task 7 - 8+ Rating", high_rating_count)

# Complexity:
# Time: O(n) - must loop through every row to check every rating
# Space: O(1) - only stores one row at a time plus one counter variable