import os
import pickle
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def train_model():
    print("Reading dataset files...", flush=True)
    books = pd.read_csv("data/books_dataset.csv")
    ratings = pd.read_csv("data/ratings_dataset.csv")

    print(f"Books shape: {books.shape}", flush=True)
    print(f"Ratings shape: {ratings.shape}", flush=True)

    # Merge ratings with books metadata
    merged_df = ratings.merge(books, on="ISBN")

    # Create User-Item Pivot Table
    # Rows: Book Titles | Columns: User IDs | Values: Ratings (0 if unrated)
    book_pivot = merged_df.pivot_table(
        index="Book-Title", 
        columns="User-ID", 
        values="Book-Rating"
    ).fillna(0)

    print(f"Pivot Matrix shape: {book_pivot.shape} (Books x Users)", flush=True)

    # Initialize and train KNN model
    # Using cosine similarity algorithm with brute force search
    model = NearestNeighbors(algorithm="brute", metric="cosine")
    model.fit(book_pivot.values)

    # Save artifacts to 'artifacts/' folder
    os.makedirs("artifacts", exist_ok=True)

    with open("artifacts/model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("artifacts/book_pivot.pkl", "wb") as f:
        pickle.dump(book_pivot, f)

    book_names = list(book_pivot.index)
    with open("artifacts/book_names.pkl", "wb") as f:
        pickle.dump(book_names, f)

    # Deduplicate books details for display lookup
    final_rating = books.drop_duplicates("Book-Title")
    with open("artifacts/final_rating.pkl", "wb") as f:
        pickle.dump(final_rating, f)

    print("\nModel training successful!", flush=True)
    print("Artifacts generated in 'artifacts/' directory:", flush=True)
    print("  - artifacts/model.pkl", flush=True)
    print("  - artifacts/book_pivot.pkl", flush=True)
    print("  - artifacts/book_names.pkl", flush=True)
    print("  - artifacts/final_rating.pkl", flush=True)

if __name__ == "__main__":
    train_model()
