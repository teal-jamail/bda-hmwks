# Python CSV DictReader Quiz

## Question 1

What does `csv.DictReader(file)` return for each row?

- A list of strings
- A dictionary using column names as keys
- A single string
- A tuple of values

Answer: 2
Type: single
Time: 45
Explanation: `csv.DictReader` reads each CSV row as a dictionary, using the header row as keys.

## Question 2

Why is dictionary-style access often clearer than index-based access in CSV files?

- Because dictionaries are always faster
- Because column names are more meaningful than numeric indexes
- Because dictionaries remove missing values
- Because dictionaries convert values to numbers automatically

Answer: 2
Type: single
Time: 45
Explanation: Accessing columns by name, such as `row["title"]`, is usually clearer and easier to maintain than using indexes.

## Question 3

When using `csv.DictReader`, what type are CSV values read as?

- Integers
- Floats
- Strings
- Booleans

Answer: 3
Type: single
Time: 45
Explanation: CSV values are still read as strings, so numeric conversion must be done manually when needed.

## Question 4

Which of the following are used in this session?

- `csv.DictReader`
- key-based access like `row["title"]`
- `break` for first-match search
- `pandas.DataFrame`

Answer: 1,2,3
Type: multiple
Time: 45
Explanation: This session focuses on `csv.DictReader`, key-based access, counters, loops, and `break`, not pandas.

## Question 5

What does `reader.fieldnames` give you?

- The first 5 rows
- The list of column names
- The missing values
- The average of a column

Answer: 2
Type: single
Time: 45
Explanation: `reader.fieldnames` returns the column names taken from the CSV header row.

## Question 6

Why do we still use a counter with dictionary rows?

- Because dictionaries cannot be printed
- Because counting logic still uses loop + condition + counter
- Because dictionaries only work with counters
- Because counters convert strings to numbers

Answer: 2
Type: single
Time: 45
Explanation: Even though access is by key, counting still depends on looping through rows and increasing a counter when a condition is true.

## Question 7

What is the purpose of `break` when finding the first matching row?

- It skips the header row
- It stops the loop after the first match
- It converts a row into a dictionary
- It sorts the data

Answer: 2
Type: single
Time: 45
Explanation: `break` stops the loop immediately once the first matching row is found.

## Question 8

What is the difference between checking `genres == "Action"` and `"Action" in genres`?

- They are always exactly the same
- The first checks exact equality, while the second checks whether Action appears inside a longer string
- The first is for numbers and the second is for text
- The second only works with lists

Answer: 2
Type: single
Time: 45
Explanation: Exact equality matches only `Action`, while `in` also matches values like `Action, Adventure`.

## Question 9

Which of the following are valid tasks from this session?

- Count how many movies are from the USA
- Find the missing data point in an incomplete dataset
- Replace missing years with researched values
- Print only the first 5 data rows

Answer: 1,2,4
Type: multiple
Time: 45
Explanation: Part 1 includes counting, first rows, exact and partial matches, and finding missing data in `movies_incomplete`. Replacing missing years belongs to Part 2.

## Question 10

What is the time complexity of scanning the CSV row by row to find a match in the worst case?

- O(1)
- O(log n)
- O(n)
- O(n²)

Answer: 3
Type: single
Time: 45
Explanation: In the worst case, the script may inspect every row once, so the time complexity is O(n).
