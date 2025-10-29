%%writefile app.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from fuzzywuzzy import fuzz # NEW IMPORT: fuzzywuzzy
from fuzzywuzzy import process # NEW IMPORT: fuzzywuzzy


# --- CORE MODEL SETUP (Runs once when the app starts) ---

try:
    df = pd.read_csv('/content/Tamil_songs_90s_2Ks_latest.csv')
except FileNotFoundError:
    st.error("Error: 'Tamil_songs_90s_2Ks_latest.csv' not found. Please upload it to your Colab session.")
    st.stop()

# 1. Prepare Data and Features
features = [
    'danceability', 'acousticness', 'energy', 'liveness',
    'loudness', 'speechiness', 'tempo', 'mode',
    'key', 'Valence', 'popularity'
]
df_features = df[features]
df = df.drop_duplicates(subset='song_name').reset_index(drop=True)
df_features = df_features.loc[df.index]

# 2. Scale Features
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(df_features)

# 3. Calculate Similarity Matrix
cosine_sim = cosine_similarity(features_scaled)

# 4. Create Index Mapping: Use ORIGINAL song names as the index keys are used for fuzzy matching scores
# We will use df['song_name'] as the list of choices for fuzzy matching later.


# --- RECOMMENDATION FUNCTION (MODIFIED FOR FUZZY MATCHING) ---
def get_recommendations(song_title, num_recs=10):
    
    # 1. Try to find an EXACT (case-insensitive) match first
    song_title_lower = song_title.lower()
    
    # Create the index series dynamically here for the current df
    indices = pd.Series(df.index, index=df['song_name'].str.lower())
    
    if song_title_lower not in indices.index:
        
        # 2. If exact match fails, perform FUZZY MATCHING
        # Use the original song names for matching to handle mixed case/punctuation better
        all_song_titles = df['song_name'].tolist()
        
        # Find the best match using token_sort_ratio for robust comparison
        # Threshold: We require a score of 80% similarity or higher
        best_match_tuple = process.extractOne(song_title, all_song_titles, scorer=fuzz.token_sort_ratio, score_cutoff=80)
        
        if best_match_tuple:
            # Found a fuzzy match
            best_match_title = best_match_tuple[0]
            st.warning(f"Did not find '{song_title}'. Using closest match: **{best_match_title}**")
            # Overwrite the input title with the best match for the rest of the function
            song_title_lower = best_match_title.lower()
            
        else:
            # No acceptable fuzzy match found
            return f"Error: Song '{song_title}' not found in the dataset. Please check spelling."

    # Get the index (using the best match title's lowercase version)
    idx = indices[song_title_lower]

    # 3. Get the similarity scores for that song
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_songs_indices = [i[0] for i in sim_scores[1:num_recs + 1]]

    return df.iloc[top_songs_indices][['song_name', 'singer', 'Stream']]


# --- STREAMLIT WEB APP INTERFACE ---

st.title("🎶 Tamil Song Recommendation System")
st.markdown("Content-based recommendations using audio features.")

# User Input
song_input = st.text_input(
    'Enter a Song Title:',
    placeholder='E.g., En Iniya Pon Nilave'
)

num_recs = st.slider(
    'Number of Recommendations:',
    min_value=1, max_value=20, value=5
)

if st.button('Get Recommendations'):
    if song_input:
        with st.spinner('Searching for similar songs...'):
            recommendations = get_recommendations(song_input, num_recs)

            if isinstance(recommendations, str) and recommendations.startswith("Error"):
                st.error(recommendations)
            else:
                st.subheader(f"Top {len(recommendations)} Recommendations for '{song_input}'")
                st.dataframe(recommendations)
    else:
        st.warning('Please enter a song title to get recommendations.')

print("app.py saved successfully with fuzzy matching.")
