# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

This recommender is content-based, which means it compares each song's attributes to the user's taste profile instead of looking at what other people listen to. A song gets 2 points if its genre matches the user's favorite genre and 1 point if its mood matches the user's favorite mood. It also gets up to 1 more point for energy: the closer the song's energy is to the energy the user wants, the closer it gets to that full point. This means the highest score any song can get is 4. The recommender scores every song in the catalog, then sorts them from highest to lowest score. It returns the top few songs along with the reasons each one earned its points.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The catalog has only one rock song, so the "Deep Intense Rock" profile gets one great match and then mostly weak ones. Storm Runner scored 3.99, but the next result, Gym Hero, only matched the mood, and the last three only matched on energy and scored under 1.0. Because a genre match is worth the most points (+2.0), the system favors songs from the user's genre and has little to offer when that genre has few songs. Gym Hero (a pop song with an intense mood) showed up for both "High-Energy Pop" and "Deep Intense Rock" because its energy is high.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

**Weight shift experiment:** I halved the genre weight (from +2.0 to +1.0) and doubled the energy weight (energy points went from 1 minus the gap to 2 times that). For the "Sad but Energetic" profile (pop, sad, energy 0.9), the original top 3 were Gym Hero, Sunrise City, and Empty Porch Light, the only sad song. After the change, Empty Porch Light dropped out of the top 5, because energy mattered even more, and the mood match was worth relatively less next to it. For the Default profile, Rooftop Lights (happy) moved above Gym Hero (intense), which fits the user better. My conclusion is that the change made the rankings different, not more accurate, so I reverted the weights to the original values.

**Profile Comparisons:**

1. **High-Energy Pop vs Chill Lofi:** The top songs moved from high-energy pop songs (Sunrise City, Gym Hero) to low-energy lofi songs (Library Rain, Midnight Coding). This makes sense because both the genre and the energy target changed.
2. **High-Energy Pop vs Deep Intense Rock:** Gym Hero appears in both lists. It matches the pop genre for the first profile and the "intense" mood for the second, and its energy is high for both.
3. **Chill Lofi vs Deep Intense Rock:** These profiles want opposite energy levels. Lofi has several good matches, but rock has only one genre match (Storm Runner) because the dataset has only one rock song.
4. **High-Energy Pop vs Sad but Energetic:** The top 2 are the same two songs (Gym Hero and Sunrise City) because the genre match (+2.0) is worth more than the mood. Only the third result changes: Rooftop Lights (happy) is replaced by Empty Porch Light (sad).
5. **Unknown Genre vs Middle of Road:** Each profile has one genre match: Moonlit Sonata Sketch for classical and Coffee Shop Stories for jazz. After that, Middle of Road relies on energy closeness only, while Unknown Genre's next three songs also get a mood match because they are "chill".

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
