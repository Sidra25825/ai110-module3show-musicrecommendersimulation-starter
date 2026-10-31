# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->

**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->

---

## Session Log: Claude Code (2026-10-31)

### 1. Implementing `load_songs`

**Prompt used:**

> Open src/recommender.py and update only the load_songs function.
> It should use Python's csv module (DictReader) to read the CSV file
> at csv_path and return a list of dictionaries, one per song.
>
> Convert these columns to numbers so I can do math with them later:
> - id → int
> - energy, valence, danceability, acousticness → float
> - tempo_bpm → float
>
> Keep genre, mood, title and artist as text.
> Don't change any other function. Explain each line in simple words.

**What the AI did:**

The AI rewrote `load_songs` so it reads the file with `csv.DictReader`, converts `id` to `int` and `energy`, `tempo_bpm`, `valence`, `danceability` and `acousticness` to `float`, and returns a list of song dictionaries. It explained each line in simple words. It also moved the "Loading songs..." print to the start of the function and added `encoding="utf-8"` when opening the file.

**What was changed or double-checked:**

- The AI ran `load_songs("data/songs.csv")`, which loaded 10 songs with the number columns stored as numbers.
- The `import csv` line and an earlier DictReader version (without number conversion) were already in my uncommitted changes. The AI kept the import.
- No follow-up changes were requested.

### 2. Filling "How The System Works" in README.md

**Prompt used:**

> Open README.md and fill in the "How The System Works" section only.
> Don't change any other section.
>
> Write:
> 1. A short paragraph (4-5 sentences, simple words) explaining how
>    real-world recommenders work: collaborative filtering (other
>    users' behavior) vs content-based filtering (song attributes),
>    and what data they use (likes, skips, playlists, tempo, mood).
>    Then say what MY version prioritizes: it is content-based and
>    scores songs by genre match, mood match, and energy closeness.
>
> 2. A list of the features my Song and UserProfile will use:
>    - Song: genre, mood, energy (also available: tempo_bpm, valence,
>      danceability, acousticness)
>    - UserProfile: favorite_genre, favorite_mood, target_energy
>
> Keep it short and beginner-friendly.

**What the AI did:**

The AI replaced the placeholder prompts in that section with a 5-sentence paragraph explaining collaborative vs content-based filtering and the data real apps use, ending with how my content-based version scores songs. It then added a bullet list of the `Song` and `UserProfile` features I listed.

**What was changed or double-checked:**

- The AI pointed out that `UserProfile` in `recommender.py` also has a `likes_acoustic` field that is not in the README list. It left it out because it wasn't in my list.
- No follow-up changes were requested.

### 3. Adding 8 new songs to data/songs.csv

**Prompt used:**

> Open data/songs.csv. Add 8 new songs to the end of the file in valid
> CSV format, using exactly the same headers and column order.
>
> Rules:
> - Continue the id numbers (11, 12, ...)
> - Use genres and moods that are NOT already in the file
>   (for example: hip-hop, classical, r&b, country, metal, folk,
>   edm, reggae; moods like sad, romantic, angry, nostalgic, uplifting)
> - Keep energy, valence, danceability, acousticness between 0.0 and 1.0
> - Keep tempo_bpm realistic for each genre
> - Make the numbers match the genre and mood (for example, metal =
>   high energy, classical = low energy and high acousticness)
> - Don't change the existing 10 songs
>
> Don't change any other file.

**What the AI did:**

The AI added songs 11-18 with the genres hip-hop, classical, r&b, country, metal, folk, edm and reggae, and the moods confident, peaceful, romantic, nostalgic, angry, sad, euphoric and uplifting. It made up the titles and artists, and chose numbers that fit each genre (for example, metal has energy 0.97 and 172 bpm, classical has energy 0.18 and acousticness 0.97).

**What was changed or double-checked:**

- The AI checked the existing genres and moods first so the new ones would not repeat them. Three moods (confident, peaceful, euphoric) were the AI's own choices because my example list only had five.
- The AI loaded the file with `load_songs` and confirmed it read all 18 songs.
- No follow-up changes were requested.
