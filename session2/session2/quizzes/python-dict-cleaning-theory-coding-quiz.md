# Python Dictionary Cleaning Theory and Coding Quiz

## Question 1

Why is `csv.DictReader` often easier to maintain than `csv.reader`?

- It skips rows with missing values automatically
- It allows access by column name instead of numeric index
- It always uses less memory than `csv.reader`
- It converts strings into numbers automatically

Answer: 2
Type: single
Time: 40
Explanation: Column-name access makes code clearer and reduces index mistakes.

## Question 2

Given `movie = {"music_by": ""}`, which check correctly treats the field as missing?

- `if movie["music_by"] is None:`
- `if movie["music_by"] == 0:`
- `if movie["music_by"].strip() == "":`
- `if len(movie["music_by"]) > 0:`

Answer: 3
Type: single
Time: 40
Explanation: In CSV-style data cleaning, missing values are often empty strings, so stripping and comparing to `""` is reliable.

## Question 3

Which pattern best describes a basic cleaning workflow?

- Read -> train model -> deploy
- Detect missing values -> update/fix -> validate -> save
- Sort -> reverse -> deduplicate only
- Compress -> encrypt -> upload

Answer: 2
Type: single
Time: 40
Explanation: Practical cleaning typically includes detection, correction, verification, and writing cleaned output.

## Question 4

What does this line do?

`movie["music_by"] = "Joe Hisaishi"`

- Deletes a key from the dictionary
- Creates or updates the `music_by` value
- Converts the whole dictionary to CSV
- Appends a new dictionary to a list

Answer: 2
Type: single
Time: 35
Explanation: Dictionary assignment updates an existing key or creates it if missing.

## Question 5

When writing cleaned rows to CSV with `DictWriter`, which steps are required?

- Create `DictWriter` with `fieldnames`
- Call `writeheader()`
- Call `writerows(rows)`
- Use `json.dump` in the same file handle

Answer: 1,2,3
Type: multiple
Time: 45
Explanation: `DictWriter` needs field names, then header writing, then row writing. `json.dump` is unrelated to CSV output.

## Question 6

If your script loops through all `n` rows once to detect missing values, what is the time complexity?

- O(1)
- O(log n)
- O(n)
- O(n^2)

Answer: 3
Type: single
Time: 35
Explanation: A single full pass over rows is linear time.

## Question 7

If your script stores all cleaned rows in a list before saving, what is the extra space complexity with respect to rows?

- O(1)
- O(log n)
- O(n)
- O(n^2)

Answer: 3
Type: single
Time: 35
Explanation: Keeping all rows in memory grows linearly with dataset size.

## Question 8

Why is saving cleaned data to a new file often better than overwriting the raw input immediately?

- It is always faster
- It preserves the original data for audit and rollback
- It removes the need for validation
- It guarantees perfect cleaning

Answer: 2
Type: single
Time: 40
Explanation: Keeping raw data intact makes debugging and verification safer.

## Question 9

Which statements about dictionary/list cleaning code are true?

- `for row in rows:` iterates one dictionary per row
- `row["year"] = "1989"` updates the current row
- `break` can stop at the first match
- `int(row["year"])` is always safe without checks

Answer: 1,2,3
Type: multiple
Time: 45
Explanation: The first three are core loop behaviors; converting to `int` is unsafe if values are missing or non-numeric.

## Question 10

Which strategy is best before computing an average from CSV text values?

- Convert every value with `int()` directly without checks
- Skip conversion and average strings
- Validate/clean values first, then convert numeric fields
- Sort rows alphabetically first

Answer: 3
Type: single
Time: 40
Explanation: Numeric statistics should be computed only after missing/invalid values are handled.
