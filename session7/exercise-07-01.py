import pandas as pd

# Task 1: Load Dataset
movies = pd.read_json("datasets/Movies.json")

# Task 2: First 5 Rows, Last 3 Rows, Shape
print(movies.head())
print(movies.tail(3))
print(movies.shape)

# Task 3: DataTypes & Summary Stats
print(movies.dtypes)
print(movies.describe())

# Task 4: Title, Release date, Rating
print(movies[["Title", "Release Date", "IMDB Rating"]])

# Task 5: Filter Movies w/ Rating >= 8
good_movies = movies[movies["IMDB Rating"] >= 8]
print(good_movies[["Title", "IMDB Rating"]])

# Task 6: Col. for "Long Movies"
movies ["Long Movies"] = movies["Running Time min"] >= 120
print(movies[["Title", "Long Movies"]])

# Task 7: Movie Count by Genre 
print(movies["Major Genre"].value_counts())

# Task 8: Sort by Rating
good_movies = movies.sort_values("IMDB Rating", ascending=False).head(10)
print(good_movies[["Title", "IMDB Rating"]])
# to see whether everything is stored right and if there are missing vals.

