### Session 2 | Part 3

> In Part 3, you first learn the cleaning pattern with one tiny dictionary, then apply the same logic to a real CSV dataset as an exercise.

#### 1. Goal

You will learn this exact sequence:

1. create data with a missing value
2. detect what is missing
3. update/fix the missing value
4. save cleaned data to disk

Then you will apply the same flow on `studio_ghibli_movies.csv`.

#### 2. Mini tutorial

Create:

```txt
session2/solutions/exercise-02-02.py
```

Start with two records:

- one missing `music_by`
- one missing `year`

```python
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
```

#### 3. Find the missing value

```python
for i, movie in enumerate(movies, start=1):
    for key, value in movie.items():
        if value.strip() == "":
            print(f"Record {i} missing field: {key}")
```

> [!TIP]
>
> `strip()` is a Python string method that removes extra characters from the beginning and end of a string. For example `text = "   hello   "` with `text.strip()` it becomes `hello`. Use the strip as a general rule of thumb when working with text.

Expected output:

```txt
Record 1 missing field: music_by
Record 2 missing field: year
```

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n * m), where `n` is number of records and `m` is number of fields per record.
>
> Space: O(1) extra space.
>
> </details>

Can you do it better for this specific dataset? Yes.

If you already know the fields you care about (`year`, `music_by`), you can avoid looping through every key:

```python
for i, movie in enumerate(movies, start=1):
    if movie["music_by"].strip() == "":
        print(f"Record {i} missing field: music_by")
    if movie["year"].strip() == "":
        print(f"Record {i} missing field: year")
```

> [!TIP]
>
> What are the time and space complexities of this improved script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n), because each record is checked once with constant work.
>
> Space: O(1) extra space.
>
> </details>

#### 4. Fix the missing value (update dictionary)

```python
if movies[0]["music_by"].strip() == "":
    movies[0]["music_by"] = "Joe Hisaishi"

if movies[1]["year"].strip() == "":
    movies[1]["year"] = "1989"

print(movies)
```

This is the core cleaning idea: detect then update.

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(1) for this exact two-record example.
>
> Space: O(1) extra space.
>
> In a generalized loop across `n` records, update time becomes O(n).
>
> </details>

#### 5. Keep a copy for safekeeping

Sometimes we want both versions:

- raw/original data (unchanged)
- cleaned data (updated)

Naming note:

- `original_movies`: backup copy for safekeeping (do not edit this)
- `cleaned_movies`: working copy that we edit during cleaning

```python
original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy() for movie in movies]

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"

print("Original:", original_movies)
print("Cleaned:", cleaned_movies)
```

From this point onward, "cleaned data" means the `cleaned_movies` list.

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n * m), because each copied record copies its fields.
>
> Space: O(n * m), because we store two copied lists.
>
> </details>

#### 6. Save cleaned dictionary to disk

Use JSON for this mini example:

```python
import json

with open("movies_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

print("Saved: movies_clean.json")
```

Now you have completed the full cleaning pipeline.

> [!TIP]
>
> What are the time and space complexities of this script?
>
> <details>
> <summary>Show answer</summary>
>
> Time: O(n * m), because writing depends on number of records and fields.
>
> Space: O(1) extra space (excluding data already in memory).
>
> </details>

#### 7. Exercise: apply same logic to CSV dataset

Use: [Birkbeck/studio_ghibli_movies](https://huggingface.co/datasets/Birkbeck/studio_ghibli_movies)

Download:

```bash
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv \
  --repo-type dataset \
  --local-dir .
```

Expected file in `session2/`:

```txt
studio_ghibli_movies.csv
```

#### 8. Exercise tasks

In `session2/solutions/exercise-02-02.py`, do the following:

1. Load the `studio_ghibli_movies.csv` dataset with `csv.DictReader`.
2. Find missing values by column and print where they are (line number + movie title).
3. Fix missing values (for this dataset, check `year` and `music_by`).
4. Calculate:

   - average of `year`
   - how many times Miyazaki appears as director

5. Save cleaned rows into a new file:

   - `studio_ghibli_movies_clean.csv`

6. Re-check missing values after cleaning and print remaining missing count.

7. What are the time and space complexities of your full script?

#### 9. Quiz

Complete the following quiz:

```bash
quizmd quizzes/python-dict-cleaning-theory-coding-quiz.md
```
