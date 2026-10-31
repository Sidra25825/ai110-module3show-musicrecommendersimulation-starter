# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeFinder 1.0

---

## 2. Intended Use  

This recommender suggests songs from a small catalog based on a user's favorite genre, favorite mood, and target energy. It assumes the user can describe their taste with these three things. It is made for classroom learning, not for real users. It should not be used to make real product decisions or to represent a person's full musical taste.

---

## 3. How the Model Works  

This recommender is content-based, which means it compares each song's attributes to the user's taste profile instead of looking at what other people listen to. A song gets 2 points if its genre matches the user's favorite genre and 1 point if its mood matches the user's favorite mood. It also gets up to 1 more point for energy: the closer the song's energy is to the energy the user wants, the closer it gets to that full point. This means the highest score any song can get is 4. The recommender scores every song in the catalog, then sorts them from highest to lowest score. It returns the top few songs along with the reasons each one earned its points.

---

## 4. Data  

The catalog is data/songs.csv with 18 songs: 10 from the starter file and the rest added by me. Each song has a genre, mood, energy, tempo, valence, danceability, and acousticness. The recommender only uses genre, mood, and energy. The catalog is small, and some genres (like rock) have only one song. Many parts of musical taste are missing, such as language, lyrics, and era.

---

## 5. Strengths  

The system works best when the catalog has several songs that fit the user's genre and mood. For "Chill Lofi", the top results were three lofi songs, and Library Rain scored the maximum 4.00. The reasons shown with each score make it easy to see why a song was recommended.

---

## 6. Limitations and Bias 

The catalog has only one rock song, so the "Deep Intense Rock" profile gets one great match and then mostly weak ones. Storm Runner scored 3.99, but the next result, Gym Hero, only matched the mood, and the last three only matched on energy and scored under 1.0. Because a genre match is worth the most points (+2.0), the system favors songs from the user's genre and has little to offer when that genre has few songs. Gym Hero (a pop song with an intense mood) showed up for both "High-Energy Pop" and "Deep Intense Rock" because its energy is high.

---

## 7. Evaluation  

I tested 7 user profiles: Default (pop, happy), High-Energy Pop,
Chill Lofi, Deep Intense Rock, Sad but Energetic, Unknown Genre
(classical), and Middle of Road (jazz). I looked at whether the
top 5 songs matched each profile's genre, mood, and energy, and
whether the reasons made sense. What surprised me most was "Sad
but Energetic": the top two songs were pop songs that are not sad,
and the only sad song ranked third, because a genre match is worth
more than a mood match.

**Weight shift experiment:** I halved the genre weight (from +2.0 to +1.0) and doubled the energy weight (energy points went from 1 minus the gap to 2 times that). For the "Sad but Energetic" profile (pop, sad, energy 0.9), the original top 3 were Gym Hero, Sunrise City, and Empty Porch Light, the only sad song. After the change, Empty Porch Light dropped out of the top 5, because energy mattered even more, and the mood match was worth relatively less next to it. For the Default profile, Rooftop Lights (happy) moved above Gym Hero (intense), which fits the user better. My conclusion is that the change made the rankings different, not more accurate, so I reverted the weights to the original values.

**Profile Comparisons:**

1. **High-Energy Pop vs Chill Lofi:** The top songs moved from high-energy pop songs (Sunrise City, Gym Hero) to low-energy lofi songs (Library Rain, Midnight Coding). This makes sense because both the genre and the energy target changed.
2. **High-Energy Pop vs Deep Intense Rock:** Gym Hero appears in both lists. It matches the pop genre for the first profile and the "intense" mood for the second, and its energy is high for both.
3. **Chill Lofi vs Deep Intense Rock:** These profiles want opposite energy levels. Lofi has several good matches, but rock has only one genre match (Storm Runner) because the dataset has only one rock song.
4. **High-Energy Pop vs Sad but Energetic:** The top 2 are the same two songs (Gym Hero and Sunrise City) because the genre match (+2.0) is worth more than the mood. Only the third result changes: Rooftop Lights (happy) is replaced by Empty Porch Light (sad).
5. **Unknown Genre vs Middle of Road:** Each profile has one genre match: Moonlit Sonata Sketch for classical and Coffee Shop Stories for jazz. After that, Middle of Road relies on energy closeness only, while Unknown Genre's next three songs also get a mood match because they are "chill".

---

## 8. Future Work  

1. Add more songs, so every genre has several options.
2. Use more features, like valence and acousticness, and let users pick several favorite genres or moods.
3. Add a diversity rule, so the top results don't all come from the same genre, and lower the genre weight so mood can matter more.

---

## 9. Personal Reflection  

The most interesting thing I discovered was how apps like YouTube
and Spotify decide which songs I might like. I learned that there
are two main techniques: collaborative filtering, which looks at
what similar users do, and content-based filtering, which looks at
the song's own attributes. YouTube mostly relies on watch behavior,
while Spotify mixes both, and my project uses only the content-based
type. This was my biggest learning moment.

AI helped me mostly with writing and documentation. When I finished
a piece of work, I asked it to add the explanation to the README or
the model card. After that, I went back to the file and checked what
it wrote to see if it was correct, for example when we summarized my
scoring algorithm.

What surprised me was that my recommender only adds up points, yet
for the "Chill Lofi" profile it returned calm lofi songs that felt
like real recommendations.

Next, I would add more songs so every genre has several options,
and use more features like valence and acousticness.
