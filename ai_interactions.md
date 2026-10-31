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

### 4. Adding the Algorithm Recipe and Expected Bias to README.md

**Prompt used:**

> Open README.md. In the "How The System Works" section, add
> to what is already there (don't delete anything):
>
> 1. An "Algorithm Recipe" with these exact rules:
>    - +2.0 points for a genre match
>    - +1.0 point for a mood match
>    - Energy points = 1 - abs(user target energy - song energy)
>    - Maximum score: 4.0
>
> 2. A short "Expected Bias" note (2-3 sentences) saying this system
>    might over-prioritize genre, because a genre match is worth the
>    most points, so it may ignore songs that match the user's mood
>    and energy but have a different genre.
>
> Keep it short and simple. Don't change any other section.

**What the AI did:**

The AI added an "Algorithm Recipe" list with the four rules and a 3-sentence "Expected Bias" note under the features list. The bias note includes an example: a song in a different genre with a mood match and perfect energy can only reach 2.0, while a genre-only match starts at 2.0.

**What was changed or double-checked:**

- The AI checked that the points add up to the 4.0 maximum (2.0 + 1.0 + 1.0).
- No follow-up changes were requested.

### 5. Adding sample output to README.md

**Prompt used:**

> Open README.md. Add a new section called "Sample Recommendation
> Output" at the end. Run `python -m src.main` and paste the exact
> terminal output into a fenced code block (text, not a screenshot).
> Add one sentence above it saying it's the output for the default
> profile: genre pop, mood happy, energy 0.8.
> Don't change any other section.

**What the AI did:**

The AI ran `python -m src.main` and pasted the output (top 5 songs for the default profile) into a text code block with the sentence above it. It did not add a new section at the end, because the README already had a "Sample Recommendation Output" section from the template. It filled in that section instead.

**What was changed or double-checked:**

- The AI's placement differs from my prompt (the existing section instead of a new one at the end). The AI explained why and offered to move it.
- The AI pointed out that two lines at the end of `recommend_songs` come after a `return`, so they never run.

### 6. Shortening docstrings in recommender.py

**Prompt used:**

> Open src/recommender.py. Add a 1-line docstring to load_songs,
> score_song, and recommend_songs. Replace the existing docstrings
> only in these three functions. Don't change any code or other functions.

**What the AI did:**

The AI replaced the multi-line docstrings of the three functions with one-line docstrings that describe what each function does and returns. No code was changed.

**What was changed or double-checked:**

- The AI ran `python -m src.main` again to confirm the program still works.
- The old "Required by src/main.py" notes were removed so each docstring fits on one line.

### 7. Filling "How the Model Works" in model_card.md

**Prompt used:**

> Open model_card.md. Find the "Algorithm Summary" section (or the
> section about how the algorithm works) and fill it in. Don't change
> any other section.
>
> Write 5-6 short sentences in plain language, no code, for a
> non-programmer. Explain:
> - The recommender is content-based: it compares each song's
>   attributes to a user's taste profile.
> - Each song gets points: +2.0 for a genre match, +1.0 for a mood
>   match, and up to +1.0 for energy (1 minus the gap between the
>   user's target energy and the song's energy).
> - The maximum score is 4.0.
> - Every song is scored, then the list is sorted from highest to
>   lowest, and the top k are returned with the reasons for each score.

**What the AI did:**

There was no "Algorithm Summary" section, so the AI filled in "3. How the Model Works" with 6 plain sentences covering the points in my prompt. It described the energy rule in words instead of as a formula and wrote "the top few songs" instead of "top k".

**What was changed or double-checked:**

- The AI pointed out the wording choices above and offered to use the exact formula or the word "k" instead.

### 8. Adding test profiles to main.py

**Prompt used:**

> Open src/main.py. Keep the existing default profile. Add these 3
> profiles and run recommend_songs for each one in a loop, printing
> the profile name as a header, then the top 5 results in the same
> format as now (title, score, reasons). Don't change recommender.py.
>
> profiles = {
>     "High-Energy Pop":   {"genre": "pop",  "mood": "happy",   "energy": 0.9},
>     "Chill Lofi":        {"genre": "lofi", "mood": "chill",   "energy": 0.35},
>     "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
> }

**What the AI did:**

The AI put the default profile and the 3 new profiles into one `profiles` dictionary and looped over it, printing each profile name as a header and then the top 5 results in the same format as before.

**What was changed or double-checked:**

- The AI ran `python -m src.main` and confirmed the default results did not change.
- The AI pointed out that "Deep Intense Rock" has only one rock song to match, so the rest of its top 5 is filled mostly by energy.

### 9. Adding all profile outputs to README.md

**Prompt used:**

> Open README.md. Add a section called "Evaluation: Profile Outputs".
> Run `python -m src.main` and paste the full terminal output,
> for all profiles, into one fenced code block (text, not a screenshot).
> Don't change any other section.

**What the AI did:**

The AI ran `python -m src.main` and added an "Evaluation: Profile Outputs" section with the full output for all 4 profiles in one text code block. It placed the section after "Sample Recommendation Output" and before "Experiments You Tried".

**What was changed or double-checked:**

- The AI saved the output to a file and inserted it with a script, so the pasted text matches the program output exactly (only the trailing blank lines were removed).

### 10. Writing "Limitations and Bias" in model_card.md

**Prompt used:**

> Open model_card.md. In the "Limitations and Bias" section, write
> 3-5 sentences in simple words about one weakness I found.
> Don't change any other section.
>
> What I found:
> - songs.csv has only one rock song. For the "Deep Intense Rock"
>   profile, Storm Runner scored 3.99, but the other four results had
>   no genre or mood match, only energy closeness (all under 1.0).
> - Genre is worth the most points (+2.0), so the system favors
>   songs from the user's genre and has little to offer when the
>   genre has few songs.
> - Gym Hero (pop, intense) appeared for both "High-Energy Pop" and
>   "Deep Intense Rock", because its energy is high.
>
> Only write what is listed here. Don't invent anything.

**What the AI did:**

The AI wrote 4 sentences in the "Limitations and Bias" section about the single rock song, the large genre weight, and Gym Hero appearing in two profiles.

**What was changed or double-checked:**

- The AI compared my notes to the program output and found one mistake: Gym Hero did get a mood match (+1.0, score 1.97) for "Deep Intense Rock". Only the last three results matched on energy alone. The AI corrected that sentence to match the output.

### 11. Adding edge-case profiles to main.py

**Prompt used:**

> Open src/main.py. Add these 3 profiles to the existing profiles
> dictionary, without removing the current ones. Don't change
> recommender.py.
>
> "Sad but Energetic": {"genre": "pop",       "mood": "sad",   "energy": 0.9},
> "Unknown Genre":     {"genre": "classical", "mood": "chill", "energy": 0.2},
> "Middle of Road":    {"genre": "jazz",      "mood": "relaxed", "energy": 0.5},

**What the AI did:**

The AI added the 3 profiles after the existing 4 and ran `python -m src.main` to show the results. It summarized the top result for each profile: Gym Hero for "Sad but Energetic", Moonlit Sonata Sketch for "Unknown Genre", and Coffee Shop Stories for "Middle of Road".

**What was changed or double-checked:**

- The AI pointed out that "Unknown Genre" does not really test an unknown genre, because `songs.csv` already has a classical song (Moonlit Sonata Sketch). It suggested a genre not in the file, like "blues" or "k-pop".
- The AI noted that for "Sad but Energetic", happy and intense pop songs ranked above the only sad song, which shows the genre bias.

### 12. Weight shift experiment in score_song

**Prompt used:**

> Open src/recommender.py. In score_song only, change the weights:
> genre match from +2.0 to +1.0, and energy points from (1 - gap)
> to 2 * (1 - gap). Keep the mood weight at +1.0. Update the
> reasons text so the points shown match the new values. Verify
> that the maximum score is now 4.0. Don't change any other file.

**What the AI did:**

The AI changed the genre weight to +1.0 and the energy points to 2 * (1 - gap), updated the genre reason text, and updated the `score_song` docstring to list the new weights. For the Default profile, Rooftop Lights moved above Gym Hero.

**What was changed or double-checked:**

- The AI tested a perfect match (score 4.0) and a song that matches nothing with the biggest energy gap (score 0.0), and ran the tests (2 passed).
- The AI pointed out that the README and model card still described the old weights.
- The weights were later reverted to the original values (+2.0 genre, 1 - gap energy). The AI did not make this change.

### 13. Writing the weight shift experiment in model_card.md

**Prompt used:**

> Open model_card.md. In the Evaluation section, add a short
> paragraph (4-5 sentences, simple words) about one experiment.
> Don't change any other section or any code.
>
> What I did:
> - Weight shift experiment: I halved the genre weight (+2.0 to +1.0)
>   and doubled the energy weight (1 - gap became 2 * (1 - gap)).
> - For "Sad but Energetic" (pop, sad, 0.9), the original top 3 were
>   Gym Hero, Sunrise City, and Empty Porch Light (the only sad song).
>   After the change, Empty Porch Light dropped out of the top 5,
>   because energy mattered even more and mood was ignored more.
> - For the Default profile, Rooftop Lights (happy) moved above
>   Gym Hero (intense), which fits the user better.
> - My conclusion: the change made rankings different, not more
>   accurate. I reverted the weights to the original values.
>
> Only write what is listed here. Don't invent anything.

**What the AI did:**

The AI added a 5-sentence paragraph about the experiment under the template prompts in the Evaluation section. It kept the template prompts because the request said to add, not replace.

**What was changed or double-checked:**

- The AI checked my notes. For the Default profile, it had seen Rooftop Lights move above Gym Hero when it ran the program with the new weights. For "Sad but Energetic", it worked out the new scores by hand (not by running the program) and confirmed that Empty Porch Light (1.70) drops below Storm Runner, Neon Skyline Drop, and Iron Furnace, out of the top 5.
- The AI changed "mood was ignored more" to "the mood match counted for less", because the mood weight stayed at +1.0 and only became smaller compared to the doubled energy points.

### 14. Writing Profile Comparisons in model_card.md

**Prompt used:**

> Open model_card.md. In the Evaluation section, add a short
> "Profile Comparisons" part. For each pair below, write 1-2 simple
> sentences saying what changed and why it makes sense. Don't change
> any other section or any code. Only use the facts listed here.
>
> 1. High-Energy Pop vs Chill Lofi: top songs moved from pop songs
>    with high energy (Sunrise City, Gym Hero) to lofi songs with low
>    energy (Library Rain, Midnight Coding), because both genre and
>    energy target changed.
> 2. High-Energy Pop vs Deep Intense Rock: Gym Hero appears in both.
>    It matches pop for the first profile and the "intense" mood for
>    the second, and its energy is high for both.
> 3. Chill Lofi vs Deep Intense Rock: opposite energy levels. Lofi
>    has several good matches, but rock has only one genre match
>    (Storm Runner) because the dataset has one rock song.
> 4. High-Energy Pop vs Sad but Energetic: the top 2 are the same
>    (Gym Hero, Sunrise City) because the genre match (+2.0) beats
>    mood. Only the third result changes: Rooftop Lights (happy)
>    becomes Empty Porch Light (sad).
> 5. Unknown Genre vs Middle of Road: classical has a genre match
>    (Moonlit Sonata Sketch), and jazz has only one (Coffee Shop
>    Stories). After that, both profiles rely on energy closeness only.

**What the AI did:**

The AI added a "Profile Comparisons" part after the weight shift paragraph in the Evaluation section, with one numbered item of 1-2 sentences for each of the 5 pairs.

**What was changed or double-checked:**

- The AI checked each fact against the program output from the original weights. Pairs 1-3 matched.
- Pair 5 had a mistake: for "Unknown Genre", results 2-4 also got a mood match (+1.0) because they are "chill", so it does not rely on energy closeness only. The AI corrected the sentence. "Middle of Road" does rely on energy only after Coffee Shop Stories.
- Pair 4: the top 2 are the same songs but in a different order (Sunrise City is first for High-Energy Pop, Gym Hero is first for Sad but Energetic). The AI wrote "the same two songs" so the sentence stays true, and offered to add the order swap.
