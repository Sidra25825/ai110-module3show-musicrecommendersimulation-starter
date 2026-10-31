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
