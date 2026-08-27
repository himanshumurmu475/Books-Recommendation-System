import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load ML Model & Datasets
ARTIFACTS_DIR = "artifacts"

def load_artifacts():
    try:
        model = pickle.load(open(os.path.join(ARTIFACTS_DIR, "model.pkl"), "rb"))
        book_pivot = pickle.load(open(os.path.join(ARTIFACTS_DIR, "book_pivot.pkl"), "rb"))
        book_names = pickle.load(open(os.path.join(ARTIFACTS_DIR, "book_names.pkl"), "rb"))
        final_rating = pickle.load(open(os.path.join(ARTIFACTS_DIR, "final_rating.pkl"), "rb"))
        return model, book_pivot, book_names, final_rating
    except Exception as e:
        print(f"Error loading artifacts: {e}")
        return None, None, None, None

model, book_pivot, book_names, final_rating = load_artifacts()

def serialize_book_row(row):
    return {
        "isbn": str(row.get("ISBN", "")),
        "title": str(row.get("Book-Title", "")),
        "author": str(row.get("Book-Author", "Unknown Author")),
        "year": int(row.get("Year-Of-Publication", 2020)),
        "publisher": str(row.get("Publisher", "Independent")),
        "image_url": str(row.get("Image-URL-L", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&q=80")),
        "genre": str(row.get("Genre", "Fiction")),
        "pages": int(row.get("Pages", 350)),
        "rating": float(row.get("Rating", 4.5)),
        "num_ratings": int(row.get("Num-Ratings", 500)),
        "synopsis": str(row.get("Synopsis", "A compelling literary pursuit exploring the depths of human emotion and mystery.")),
        "vibe_tags": str(row.get("Vibe-Tags", "Atmospheric,Beautifully Written,Engaging")),
        "mood": str(row.get("Mood", "Whimsical"))
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/books")
def get_all_books():
    if final_rating is None:
        return jsonify([])
    books_list = [serialize_book_row(row) for _, row in final_rating.iterrows()]
    return jsonify(books_list)

@app.route("/api/book/<title>")
def get_book(title):
    if final_rating is None:
        return jsonify({"error": "Model not loaded"}), 500
    matched = final_rating[final_rating["Book-Title"].str.lower() == title.lower()]
    if not matched.empty:
        return jsonify(serialize_book_row(matched.iloc[0]))
    return jsonify({"error": "Book not found"}), 404

@app.route("/api/recommend")
def recommend():
    title = request.args.get("title", "The Secret History")
    n = int(request.args.get("n", 4))
    
    if model is None or book_pivot is None:
        return jsonify([])
        
    try:
        # Match book title in pivot index (case-insensitive fallback)
        matched_indices = [i for i, name in enumerate(book_pivot.index) if name.lower() == title.lower()]
        if matched_indices:
            book_id = matched_indices[0]
        else:
            book_id = 0
            
        distances, suggestions = model.kneighbors(
            book_pivot.iloc[book_id, :].values.reshape(1, -1), 
            n_neighbors=min(n + 1, len(book_pivot))
        )
        
        recommendations = []
        for idx in suggestions[0][1:]:
            recom_title = book_pivot.index[idx]
            info = final_rating[final_rating["Book-Title"] == recom_title]
            if not info.empty:
                recommendations.append(serialize_book_row(info.iloc[0]))
                
        return jsonify(recommendations)
    except Exception as e:
        print(f"Recommendation error: {e}")
        # Fallback to top books
        fallback = [serialize_book_row(row) for _, row in final_rating.head(n).iterrows()]
        return jsonify(fallback)

@app.route("/api/mood/<mood>")
def get_mood_books(mood):
    if final_rating is None:
        return jsonify([])
        
    mood_map = {
        "Whimsical": ["Fantasy / Uplifting", "Fantasy / Romance", "Fantasy", "YA"],
        "Dark": ["Dark Academia / Mystery", "Gothic Mystery / Fiction", "Satire / Horror", "Gothic Fiction / Horror", "Dystopian"],
        "Hopeful": ["Self-Help", "Architecture / Philosophy", "Nature / History", "Classic"],
        "Melancholy": ["Fiction / Literary", "Classic", "Romance / Classic"],
        "Intellectual": ["Science Fiction", "Sci-Fi", "Finance / Self-Help", "Non-Fiction", "Historical Mystery / Fiction"]
    }
    
    matching_genres = mood_map.get(mood, [])
    filtered = final_rating[final_rating["Genre"].isin(matching_genres)]
    if filtered.empty:
        filtered = final_rating[final_rating["Mood"] == mood]
    if filtered.empty:
        filtered = final_rating.head(4)
        
    return jsonify([serialize_book_row(row) for _, row in filtered.iterrows()])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting PageMatch on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
