# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

My version is a content-based music recommender. It scores each song by genre match (+2.0), mood match (+1.0), and energy closeness (up to 1.0), then returns the top songs with the reasons for each score.

---

## How The System Works

Real-world music apps like Spotify use two main ideas to recommend songs. **Collaborative filtering** looks at what other users do: if people who like the same songs as you also love a new song, you will probably like it too. **Content-based filtering** looks at the songs themselves, using attributes like tempo, mood, and energy to find songs similar to the ones you already enjoy. Big apps mix both and learn from your likes, skips, saved songs, and playlists. My version is **content-based**: it gives each song a score based on how well its genre matches, how well its mood matches, and how close its energy is to what the user wants.

**Features used**

- `Song`
  - `genre`, `mood`, `energy`
  - Also available: `tempo_bpm`, `valence`, `danceability`, `acousticness`
- `UserProfile`
  - `favorite_genre`, `favorite_mood`, `target_energy`

**Algorithm Recipe**

Each song gets a score by adding up these points:

- **+2.0 points** if the song's genre matches the user's favorite genre
- **+1.0 point** if the song's mood matches the user's favorite mood
- **Energy points** = `1 - abs(user target energy - song energy)` (the closer the energy, the more points, up to 1.0)
- **Maximum score: 4.0**

**Expected Bias**

This system might over-prioritize genre, because a genre match is worth the most points. A song that matches the user's mood and energy perfectly but has a different genre can score at most 2.0, while a song that only matches the genre already gets 2.0 before its energy points are added. So the system may ignore good songs from other genres.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

This is the output of `python -m src.main` for the default profile: genre pop, mood happy, energy 0.8.

```text
Loading songs from data/songs.csv...

Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy closeness (+0.87)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy closeness (+0.96)

Crown the Block - Score: 0.98
Because: energy closeness (+0.98)

Night Drive Loop - Score: 0.95
Because: energy closeness (+0.95)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Evaluation: Profile Outputs

This is the full output of `python -m src.main` for all seven profiles.

```text
Loading songs from data/songs.csv...

=== Default ===

Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy closeness (+0.87)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy closeness (+0.96)

Crown the Block - Score: 0.98
Because: energy closeness (+0.98)

Night Drive Loop - Score: 0.95
Because: energy closeness (+0.95)


=== High-Energy Pop ===

Top recommendations:

Sunrise City - Score: 3.92
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.92)

Gym Hero - Score: 2.97
Because: genre match (+2.0), energy closeness (+0.97)

Rooftop Lights - Score: 1.86
Because: mood match (+1.0), energy closeness (+0.86)

Storm Runner - Score: 0.99
Because: energy closeness (+0.99)

Neon Skyline Drop - Score: 0.95
Because: energy closeness (+0.95)


=== Chill Lofi ===

Top recommendations:

Library Rain - Score: 4.00
Because: genre match (+2.0), mood match (+1.0), energy closeness (+1.00)

Midnight Coding - Score: 3.93
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.93)

Focus Flow - Score: 2.95
Because: genre match (+2.0), energy closeness (+0.95)

Spacewalk Thoughts - Score: 1.93
Because: mood match (+1.0), energy closeness (+0.93)

Coffee Shop Stories - Score: 0.98
Because: energy closeness (+0.98)


=== Deep Intense Rock ===

Top recommendations:

Storm Runner - Score: 3.99
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.99)

Gym Hero - Score: 1.97
Because: mood match (+1.0), energy closeness (+0.97)

Neon Skyline Drop - Score: 0.95
Because: energy closeness (+0.95)

Iron Furnace - Score: 0.93
Because: energy closeness (+0.93)

Sunrise City - Score: 0.92
Because: energy closeness (+0.92)


=== Sad but Energetic ===

Top recommendations:

Gym Hero - Score: 2.97
Because: genre match (+2.0), energy closeness (+0.97)

Sunrise City - Score: 2.92
Because: genre match (+2.0), energy closeness (+0.92)

Empty Porch Light - Score: 1.35
Because: mood match (+1.0), energy closeness (+0.35)

Storm Runner - Score: 0.99
Because: energy closeness (+0.99)

Neon Skyline Drop - Score: 0.95
Because: energy closeness (+0.95)


=== Unknown Genre ===

Top recommendations:

Moonlit Sonata Sketch - Score: 2.98
Because: genre match (+2.0), energy closeness (+0.98)

Spacewalk Thoughts - Score: 1.92
Because: mood match (+1.0), energy closeness (+0.92)

Library Rain - Score: 1.85
Because: mood match (+1.0), energy closeness (+0.85)

Midnight Coding - Score: 1.78
Because: mood match (+1.0), energy closeness (+0.78)

Empty Porch Light - Score: 0.95
Because: energy closeness (+0.95)


=== Middle of Road ===

Top recommendations:

Coffee Shop Stories - Score: 3.87
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.87)

Velvet Hours - Score: 0.98
Because: energy closeness (+0.98)

Dirt Road Summers - Score: 0.95
Because: energy closeness (+0.95)

Midnight Coding - Score: 0.92
Because: energy closeness (+0.92)

Focus Flow - Score: 0.90
Because: energy closeness (+0.90)
```

---

## Experiments You Tried

I halved the genre weight (+2.0 to +1.0) and doubled the energy weight. For the "Sad but Energetic" profile, the only sad song (Empty Porch Light) dropped out of the top 5. The rankings were different, not more accurate, so I reverted the weights.

---

## Limitations and Risks

The catalog is small and has only one rock song. The system favors genre over mood. It does not understand lyrics or language.

---

## Reflection

My reflection is in the Personal Reflection section of the [Model Card](model_card.md).



