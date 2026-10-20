"""Task 4: Simple content-based movie recommender."""
MOVIES = [
    ("The Dark Knight", {"action","crime","drama"}),
    ("Mad Max: Fury Road", {"action","adventure","science fiction"}),
    ("Spider-Man: Into the Spider-Verse", {"animation","action","adventure"}),
    ("Inside Out", {"animation","comedy","family"}),
    ("The Grand Budapest Hotel", {"comedy","drama"}),
    ("The Proposal", {"romance","comedy"}),
    ("Pride & Prejudice", {"romance","drama"}),
    ("Gone Girl", {"thriller","mystery","drama"}),
    ("Shutter Island", {"thriller","mystery"}),
    ("Interstellar", {"science fiction","adventure","drama"}),
    ("The Martian", {"science fiction","adventure","comedy"}),
    ("Knives Out", {"mystery","comedy","crime"}),
]
def recommend(genre):
    return [(title, tags) for title,tags in MOVIES if genre.lower().strip() in tags]
def main():
    genres = sorted({g for _,tags in MOVIES for g in tags})
    print("CONTENT-BASED MOVIE RECOMMENDER")
    print("Available genres:", ", ".join(genres))
    genre = input("Which genre do you like? ").strip().lower()
    results = recommend(genre)
    if not results:
        print("No matches. Please choose a genre from the list.")
    else:
        print("\nRecommendations:")
        for i,(title,tags) in enumerate(results[:5],1):
            print(f"{i}. {title} — {', '.join(sorted(tags))}")
if __name__ == "__main__":
    main()
