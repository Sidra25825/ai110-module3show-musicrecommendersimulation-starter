"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        # Starter example profile
        "Default":           {"genre": "pop",  "mood": "happy",   "energy": 0.8},
        "High-Energy Pop":   {"genre": "pop",  "mood": "happy",   "energy": 0.9},
        "Chill Lofi":        {"genre": "lofi", "mood": "chill",   "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
        "Sad but Energetic": {"genre": "pop",       "mood": "sad",   "energy": 0.9},
        "Unknown Genre":     {"genre": "classical", "mood": "chill", "energy": 0.2},
        "Middle of Road":    {"genre": "jazz",      "mood": "relaxed", "energy": 0.5},
    }

    for name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {name} ===")
        print("\nTop recommendations:\n")
        for rec in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
