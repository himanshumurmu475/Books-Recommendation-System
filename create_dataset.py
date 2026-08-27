import os
import pandas as pd
import numpy as np

os.makedirs("data", exist_ok=True)

# Rich catalog including the exact books shown in the Stitch PageMatch design screenshots + iconic titles
books_data = [
    # Stitch PageMatch Featured & Trending Books
    ("0143132034", "The Night Ocean", "Paul La Farge", 2017, "Penguin Books", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1474296766i/30753553.jpg", 
     "Fiction / Literary", 416, 4.5, 320,
     "A captivating novel about a man's obsession with a literary mystery involving H.P. Lovecraft and a young fan, leading him on a journey that blurs the lines between reality, fiction, and madness. It's a story of love, deception, and the enduring power of myth.",
     "Slow Burn,Beautifully Written,Melancholic,Atmospheric", "Dark"),

    ("014028009X", "The Secret History", "Donna Tartt", 1992, "Vintage", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1449539316i/29044.jpg", 
     "Dark Academia / Mystery", 559, 4.8, 2450,
     "Under the influence of their charismatic classics professor, a group of clever, eccentric misfits at an elite New England college discover a way of thinking and living that is a world away from the humdrum existence of their contemporaries.",
     "Atmospheric,Dark Academia,Intellectual,Slow Burn", "Dark"),

    ("0143034901", "The Shadow of the Wind", "Carlos Ruiz Zafón", 2001, "Penguin Books", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1344922523i/1232.jpg", 
     "Gothic Mystery / Fiction", 487, 4.7, 3100,
     "Barcelona, 1945: A young boy named Daniel is taken by his antiquarian book-dealer father to the secret Cemetery of Forgotten Books, where he selects a title that drags him into a web of murder and madness.",
     "Gothic,Enchanting,Page-Turner,Atmospheric", "Dark"),

    ("015603297X", "Foucault's Pendulum", "Umberto Eco", 1988, "Harcourt", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388190055i/17841.jpg", 
     "Historical Mystery / Fiction", 641, 4.4, 1820,
     "Three book editors in Milan invent their own occult conspiracy theory for amusement, only to discover that sinister secret societies take their imaginary Plan with deadly seriousness.",
     "Complex,Intellectual,Conspiracy,Atmospheric", "Intellectual"),

    ("0316011770", "The Historian", "Elizabeth Kostova", 2005, "Little, Brown", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1554271871i/28872.jpg", 
     "Gothic Fiction / Horror", 704, 4.5, 2900,
     "A young woman uncovers letters that plunge her into a labyrinth of family secrets, academic intrigue, and a hunt across Europe for Vlad the Impaler.",
     "Gothic,Slow Burn,Atmospheric,Historical", "Dark"),

    ("125009528X", "If We Were Villains", "M.L. Rio", 2017, "Flatiron Books", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1484760312i/30319086.jpg", 
     "Dark Academia / Drama", 368, 4.6, 2100,
     "Oliver Marks has just served ten years in jail for a murder he may or may not have committed. On the day he's released, he tells the retired detective what really happened at Dellecher Conservatory.",
     "Dark Academia,Obsessive,Shakespearean,Tragic", "Dark"),

    ("1984880249", "Bunny", "Mona Awad", 2019, "Viking", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1558364730i/42815544.jpg", 
     "Satire / Horror", 304, 4.3, 1400,
     "Samantha Heather Mackey is an outsider in her small, highly selective MFA program at New England's Warren University. She is utterly repelled by the rest of her fiction writing cohort, a clique of unbearably twee rich girls who call each other 'Bunny'.",
     "Bizarre,Unsettling,Satirical,Dark", "Dark"),

    ("1250217288", "The House in the Cerulean Sea", "TJ Klune", 2020, "Tor Books", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1569514209i/45047384.jpg", 
     "Fantasy / Uplifting", 396, 4.9, 3400,
     "A delightful story about the profound experience of discovering an unlikely family in an unexpected place—and realizing that family is yours.",
     "Heartwarming,Whimsical,Cozy,Magical", "Whimsical"),

    ("0385534639", "The Night Circus", "Erin Morgenstern", 2011, "Doubleday", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1387124618i/9361589.jpg", 
     "Fantasy / Romance", 387, 4.7, 4200,
     "The circus arrives without warning. It is simply there, when yesterday it was not. Within the black-and-white striped canvas tents is an utterly unique experience full of breathtaking amazements.",
     "Enchanting,Whimsical,Romantic,Atmospheric", "Whimsical"),

    ("038554734X", "The Silent Architect", "E.R. Sterling", 2021, "HarperOne", 
     "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&q=80", 
     "Fiction", 352, 4.6, 950,
     "Winner of the Booker Prize. An architectural mystery tracing geometric secrets and lost cathedrals across 19th-century Europe.",
     "Beautifully Written,Mysterious,Architectural,Slow Burn", "Intellectual"),

    ("0062834835", "Whispers in the Pines", "Sarah Jenkins", 2022, "Scribner", 
     "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=500&q=80", 
     "Mystery", 320, 4.5, 780,
     "A thrilling mystery set deep in the ancient redwood forests of the Pacific Northwest, where old family secrets never stay buried.",
     "Spooky,Page-Turner,Atmospheric,Twisty", "Dark"),

    ("0374602603", "The Architecture of Silence", "Elena Rostova", 2020, "Penguin Press", 
     "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500&q=80", 
     "Architecture / Philosophy", 278, 4.7, 620,
     "A philosophical examination of stillness, sacred spaces, and the architecture that gives human consciousness room to breathe.",
     "Thought-Provoking,Meditative,Philosophical", "Hopeful"),

    ("0525559477", "Botanical History", "Arthur Pendelton", 2019, "Crown", 
     "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=500&q=80", 
     "Nature / History", 384, 4.8, 1100,
     "An observer's guide to the plant world, exploring the origins, diversity, and ecological significance of our planet's flora.",
     "Insightful,Beautifully Illustrated,Educational", "Hopeful"),

    ("0593135202", "Event Horizon", "Marcus Wei", 2023, "Ballantine Books", 
     "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&q=80", 
     "Science Fiction", 412, 4.8, 1650,
     "A hard sci-fi odyssey exploring relativistic physics, distant colony worlds, and humanity's confrontation with quantum anomalies.",
     "Mind-Bending,Epic,Futuristic,Suspenseful", "Intellectual"),

    # Classic & Popular Additions
    ("0061120084", "To Kill a Mockingbird", "Harper Lee", 1960, "Harper Perennial", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg", 
     "Classic", 336, 4.9, 5200, "The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it.",
     "Timeless,Emotional,Inspiring", "Hopeful"),

    ("0743273567", "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Scribner", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1490528560i/4671.jpg", 
     "Classic", 180, 4.6, 4800, "The tragic story of Jay Gatsby and his unrequited love for the beautiful Daisy Buchanan.",
     "Lyrical,Melancholic,Timeless", "Melancholy"),

    ("0141439513", "Pride and Prejudice", "Jane Austen", 1813, "Penguin Classics", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1320399351i/1885.jpg", 
     "Romance / Classic", 279, 4.8, 4900, "A timeless romance of witty banter, pride, and societal expectations.",
     "Witty,Romantic,Timeless", "Hopeful"),

    ("0451524934", "1984", "George Orwell", 1949, "Signet Classic", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1657781256i/5470.jpg", 
     "Dystopian", 328, 4.8, 4300, "The definitive dystopian classic portraying a totalitarian regime and the war against truth.",
     "Thought-Provoking,Dark,Chilling", "Dark"),

    ("0441172717", "Dune", "Frank Herbert", 1965, "Ace Books", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458.jpg", 
     "Sci-Fi", 688, 4.8, 3800, "Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides as he fulfills a destiny greater than he could ever imagine.",
     "Epic Worldbuilding,Intelligent,Futuristic", "Intellectual"),

    ("0345339681", "The Hobbit", "J.R.R. Tolkien", 1937, "Del Rey", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546071216i/5907.jpg", 
     "Fantasy", 310, 4.9, 4600, "Bilbo Baggins is a hobbit who enjoys a comfortable, unambitious life until the wizard Gandalf invites him on a great quest.",
     "Whimsical,Magical,Cozy", "Whimsical"),

    ("059035342X", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, "Scholastic", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1474154022i/3.jpg", 
     "Fantasy", 309, 4.9, 6100, "Harry Potter has no idea how famous he is until an owl delivers a letter summoning him to Hogwarts.",
     "Magical,Enchanting,Coming of Age", "Whimsical"),

    ("0735211299", "Atomic Habits", "James Clear", 2018, "Avery", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1655988385i/38657114.jpg", 
     "Self-Help", 320, 4.9, 5800, "A supremely practical guide on how small changes can produce remarkable life-changing results.",
     "Practical,Inspiring,Motivational", "Hopeful"),

    ("0857197681", "The Psychology of Money", "Morgan Housel", 2020, "Harriman House", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1581527774i/41881472.jpg", 
     "Finance / Self-Help", 256, 4.8, 3200, "Timeless lessons on wealth, greed, and happiness doing well with money.",
     "Eye-Opening,Practical,Engaging", "Intellectual"),

    ("0062316095", "Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2014, "Harper", 
     "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1703329310i/23692271.jpg", 
     "Non-Fiction", 443, 4.7, 3900, "A groundbreaking narrative of humanity's creation and evolution.",
     "Mind-Bending,Educational,Well-Researched", "Intellectual")
]

books_df = pd.DataFrame(books_data, columns=[
    "ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", 
    "Image-URL-L", "Genre", "Pages", "Rating", "Num-Ratings", "Synopsis", "Vibe-Tags", "Mood"
])
books_df["Image-URL-M"] = books_df["Image-URL-L"]
books_df["Image-URL-S"] = books_df["Image-URL-L"]

books_df.to_csv("data/books_dataset.csv", index=False)
print(f"Created data/books_dataset.csv with {len(books_df)} books.")

# Generate realistic collaborative ratings for 200 users
np.random.seed(42)
users = [f"User_{i}" for i in range(1, 201)]
ratings_list = []

# Map genre affinities to users so KNN clusters Stitch screenshot groups accurately
# Group 1: Dark Academia & Gothic Literary (The Secret History, If We Were Villains, Bunny, The Shadow of the Wind, Foucault's Pendulum, The Night Ocean, The Historian)
dark_academia_cluster = [
    "The Secret History", "If We Were Villains", "Bunny", "The Shadow of the Wind", 
    "Foucault's Pendulum", "The Night Ocean", "The Historian", "1984"
]

# Group 2: Whimsical & Cozy Fantasy (The House in the Cerulean Sea, The Night Circus, The Hobbit, Harry Potter and the Sorcerer's Stone)
whimsical_cluster = [
    "The House in the Cerulean Sea", "The Night Circus", "The Hobbit", 
    "Harry Potter and the Sorcerer's Stone", "The Architecture of Silence"
]

# Group 3: Intellectual & Non-Fiction (The Silent Architect, Botanical History, Event Horizon, Dune, Atomic Habits, Sapiens: A Brief History of Humankind, The Psychology of Money)
intellectual_cluster = [
    "The Silent Architect", "Botanical History", "Event Horizon", "Dune", 
    "Atomic Habits", "Sapiens: A Brief History of Humankind", "The Psychology of Money", "The Architecture of Silence"
]

for user_id in users:
    cluster_type = np.random.choice(["dark", "whimsical", "intellectual"], p=[0.4, 0.35, 0.25])
    if cluster_type == "dark":
        favored_titles = dark_academia_cluster
    elif cluster_type == "whimsical":
        favored_titles = whimsical_cluster
    else:
        favored_titles = intellectual_cluster
        
    n_ratings = np.random.randint(8, 18)
    sampled = books_df.sample(n=n_ratings)
    
    for _, b in sampled.iterrows():
        isbn = b["ISBN"]
        title = b["Book-Title"]
        if title in favored_titles:
            rating = np.random.choice([9, 10], p=[0.3, 0.7])
        else:
            rating = np.random.choice([1, 2, 3, 4, 5, 6], p=[0.2, 0.2, 0.2, 0.2, 0.1, 0.1])
        ratings_list.append((user_id, isbn, rating))

ratings_df = pd.DataFrame(ratings_list, columns=["User-ID", "ISBN", "Book-Rating"])
ratings_df.to_csv("data/ratings_dataset.csv", index=False)
print(f"Created data/ratings_dataset.csv with {len(ratings_df)} ratings.")
