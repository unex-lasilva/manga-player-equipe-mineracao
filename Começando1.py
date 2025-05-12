import pandas as pd

ratings  = pd.read_csv("ratings.csv", nrows=500)
movies   = pd.read_csv("movies_metadata.csv", nrows=100)
links    = pd.read_csv("links.csv", nrows=100)
credits  = pd.read_csv("credits.csv", nrows=100)
keywords = pd.read_csv("keywords.csv", nrows=100)

print("Ratings:")
print(ratings.head(500))  

print("\nMovies:")
print(movies.head(100))

print("\nLinks:")
print(links.head(100))

print("\nCredits:")
print(credits.head(100))

print("\nKeywords:")
print(keywords.head(100))