import pandas as pd

# Section 4 - load & inspect
movies = pd.read_json("datasets/Movies.json")

print(movies.head(10))
print(movies.tail(3))
print(movies.dtypes)
print(movies.shape)

# Section 5: find missing values
print(movies[["Distributor", "Major Genre", "IMDB Rating"]].isnull().sum())


# Section 6: counta all missing cells
missing_cells = movies.isnull().sum()
total_cells = movies.shape[0] * movies.shape[1]
missing_percentage = (missing_cells / total_cells) * 100

print(missing_cells)
print(missing_percentage)

# Section 7: filter rows w/ missing vals
missing_rating = movies[movies["IMDB Rating"].isnull()]
print(missing_rating[["Title", "IMDB Rating"]])

# Section 8: fill in missing txt vals w/ fillna()
clean_movies = movies.copy()
clean_movies["Major Genre"] = clean_movies["Major Genre"].fillna("missing")

print(clean_movies[["Title", "Major Genre"]].head())

# Section 9 - loc
movies.loc[100, ["Title", "Major Genre", "IMDB Rating"]]
print(movies.loc[100,["Title", "Major Genre", "IMDB Rating"]])

# Section 10 - .groupby()
avg_rating = movies.groupby("Distributor")["IMDB Rating"].mean()
print(avg_rating)

# Section 11 - fill missing num vals w/ mean
test_movies = movies.copy()
mean_rating = test_movies["IMDB Rating"].mean()
test_movies["IMDB rating"] = test_movies["IMDB Rating"].fillna(mean_rating)

print(mean_rating)
print(test_movies["IMDB Rating"].isnull().sum())

# median ignores magnitude of outliers
test_movies2 = movies.copy()
median_rotton = test_movies2["Rotten Tomatoes Rating"].median()
test_movies2["Rotten Tomatoes Rating"] = test_movies2["Rotten Tomatoes Rating"].fillna(median_rotton)

print(test_movies2["Rotten Tomatoes Rating"].isnull().sum())


# Section 12 - interpolation
# fills missing numeric vals by 
# estimating b/t the known vals on either side
# uses position of misisng vals relative to its neighborss

scores = pd.DataFrame({
    "week" :[1, 2, 3, 4, 5],
    "score": [50, None, 70, None, 90],
})
# wk 2 is missing sits b/t 50 & 70
# interpolation estimates it as 60, the midpoint [same for wk 4]

scores["score_interpolated"] = scores["score"].interpolate()

print(scores)

temps = pd.DataFrame({
    "day": [1, 2, 3, 4, 5, 6, 7],
    "temps": [20, None, 50, None, 70, None, 90],
})

temps["temps_interpolated"] = temps["temps"].interpolate()

print(temps)

# Section 13: interpolate Running Time min
test_movies3 = movies.copy()

before = test_movies3["Running Time min"].isnull().sum()
test_movies3["Running Time min"] = test_movies3["Running Time min"].interpolate()
after = test_movies3["Running Time min"].isnull().sum()

print(before)
print(after)
print(test_movies3[["Title", "Running Time min"]].head(10))

# if miss vals are at begin or end; 
# before or after any known val then left as NaN

# Section 14 - Cleaning col names
clean_movies = movies.copy()

clean_movies.columns = (
    clean_movies.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace(".", "", regex=False)
)

print(clean_movies.columns)
print(clean_movies["major_genre"].head())

# Section 15 - remove duplicates
print(movies.duplicated().sum())

clean_movies2 = movies.drop_duplicates()
print(clean_movies2.shape)

# print duplicate rows
duplicates = movies[movies.duplicated()]
print(duplicates)

# Section 16: cleaning text vals
# invisible proble - xtra space/ inconsisten capitalisation
# .value_count() would count seperately
# .groupby() would put in seperate groups
# .str.strip() removes leading and trailing spaces
# .str.lower() converts lowercase

clean_movies3 = movies.copy()

clean_movies3["Distributor"] = clean_movies3["Distributor"].str.strip()
clean_movies3["Major Genre"] = clean_movies3["Major Genre"].str.lower()

print(clean_movies3[["Distributor", "Major Genre"]].head())

# task - strip and lowercase Major Genre
clean_movies3["Major Genre"] = clean_movies3["Major Genre"].str.strip().str.lower()
print(clean_movies3["Major Genre"].head())

# Section 17 - drop rows where essential cols.
movies_with_rating = movies.dropna(subset=["IMDB Rating"])

print(movies.shape)
print(movies_with_rating.shape)

# task - drop rows where Title is null
movies_with_title = movies.dropna(subset=["Title"])

print(movies.shape)
print(movies_with_title.shape)

# ==========================================
# Section 18 - Exercise
# =========================================