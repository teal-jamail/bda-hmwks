### Session 2 | Part 2

> In Session 2, we start working with CSV files using dictionary-style rows. This is quite different from arrays, because we can use column names as keys to access data (not indexes anymore).

#### 1. Goal

First, you will practice core CSV dictionary logic using:

- `csv.DictReader`
- key-based access (for example `row["title"]`)
- counters
- `for` loops
- `break` for first-match search

#### 2. Prerequisites

Before starting:

1. Open the `session2` folder in Visual Studio Code.
2. Create and activate your virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Create your exercise file inside `session2/solutions`, for example:

```txt
session2/solutions/exercise-02-01.py
```
#### 3. Basics you should know

The `csv.DictReader(file)` reads each CSV row as a `dict` (dictionary). Keys come from the header row (column names). Values are still strings, so numeric conversion is manual when needed.

*Let's start with the basics of dictionaries.*

A Python dictionary lets you store data as key → value pairs (like word → meaning). Instead of using numbers like lists, you use names (keys) to find values, which is easier to read and understand.

```python
person = {
    "name": "Stelios",
    "age": 20, # I wish
    "city": "London"
}
```

**Access values**

```python
print(person["name"])   # Stelios
```

**Add or change values**

```python
person["job"] = "Developer"   # add new
person["city"] = "Athens"     # update
```

**Remove values**

```python
del person["city"]
```

**Loop through dictionary using `items()`**

```python
for key, value in person.items():
    print(key, value)
```

#### 4. Read CSV rows as dictionaries

To run this tutorial, first download `movies.csv` from the Hugging Face repo: [Birkbeck/movies](https://huggingface.co/datasets/Birkbeck/movies)

```bash
hf download Birkbeck/movies movies.csv --repo-type dataset --local-dir .
```

Expected result: `movies.csv` appears in your current folder.

Run your scripts from the `session2` folder, so `open("movies.csv", "r")` works directly.
If you run from the `bda` root folder instead, use `open("session2/movies.csv", "r")`.

Let's create our first script. File: `session2/solutions/exercise-02-01.py`

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

Expected output shape:

```txt
{'movie_id': '1', 'title': 'Movie 1', 'year': '2020', ...}
{'movie_id': '2', 'title': 'Movie 2', 'year': '1994', ...}
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 5. Print one named column

File: `session2/solutions/exercise-02-01.py`

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["genres"])
```

Expected output shape:

```txt
Romance
Action, 
Animation, 
Thriller
...
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
>
> Time: O(n)
>
> Space: O(1)
>
> </details>

#### 6. Count rows using a counter

Count how many rows are from 2020. Complete the missing code. 

File: `session2/solutions/exercise-02-01.py`

```python
import csv

count = 0

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    ...

print(count)
```

> [!TIP]
>
> <details>
> <summary>Show solution</summary>
>
> ```python
> ...
> for row in reader:
>     if row["year"] == "2020":
>         count += 1
> ...
> ```
>
> </details>

#### 7. Find first match with `break`

Find the first row where `genres` contains `Action`. Fill up the missing code.

File: `session2/solutions/exercise-02-01.py`

```python
import csv

with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      ...

```

> [!TIP]
>
> What are the time and space complexities of this script? See solutions also
>
> <details>
> <summary>Show answer</summary>
>
>
> Time: O(n) worst case
>
> Space: O(1)
>
> ```python
> ...
> if "Action" in row["genres"]:
>    print(row)
>    break
> ...
> ```
>
> </details>

#### 8. Call Stelios for a quick challenge 🔥

Call Stelios for a quick challenge question before moving to the exercise.

#### 9. Exercise

Add your answers to:

```txt
session2/solutions/exercise-02-01.py
```

Use the `Birkbeck/movies` dataset from Hugging Face.

1. Examine the field names using `reader.fieldnames`. Print the names.
2. Print only the first 5 data rows.
3. Count how many movies are from the `USA`.
4. Find and print the first movie where `genres` is exactly `Action`.
5. Find and print the first movie where `Action` appears inside `genres`.
6. In one short comment, explain one benefit of `DictReader` over `csv.reader`.
7. What are the time and space complexities of your script(s)?

Use the `Birkbeck/movies_incomplete` dataset from Hugging Face.
Download it into a separate folder so it does not overwrite `movies.csv`:

```bash
mkdir -p data/movies_incomplete
hf download Birkbeck/movies_incomplete movies.csv --repo-type dataset --local-dir data/movies_incomplete
```

1. Find the missing data point and print row and column.
2. Find the average of `votes` from `data/movies_incomplete/movies.csv`. Why does the naive script fail? How can you fix it?

#### 10. Quiz

Complete the following quiz.

```shell
quizmd quizzes/python-csv-dictreader-quiz.md
```

If you want to choose a theme:

```bash
quizmd --theme light quizzes/python-csv-dictreader-quiz.md
quizmd --theme dark quizzes/python-csv-dictreader-quiz.md
```
