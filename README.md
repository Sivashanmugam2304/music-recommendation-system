
# Tamil Song Recommendation System

## Project Overview

This project implements a content-based music recommendation system specifically for Tamil songs from the 90s, 2000s, and recent times. The system recommends songs based on their audio features like danceability, acousticness, energy, etc., using cosine similarity to find similar tracks. A Streamlit web application provides an interactive interface for users to get song recommendations.

Key features:
- **Content-Based Filtering:** Recommends songs based on audio characteristics.
- **Cosine Similarity:** Measures the similarity between songs using their scaled audio features.
- **Streamlit Web App:** Provides an easy-to-use graphical interface.
- **Fuzzy Matching:** Handles minor variations or typos in song titles entered by the user.

## Setup

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace with the actual repository URL
    cd <repository_name>
    ```

2.  **Install dependencies:**
    This project requires Python 3.6+ and the following libraries. You can install them using pip:
    ```bash
    pip install pandas scikit-learn streamlit fuzzywuzzy python-Levenshtein pyngrok
    ```

3.  **Obtain the dataset:**
    Place the `Tamil_songs_90s_2Ks_latest.csv` file in the project directory (or specify the correct path in `app.py`).

## How to Run the Streamlit App

Once the setup is complete, you can run the Streamlit application:

1.  Open your terminal or command prompt in the project directory.
2.  Execute the following command:
    ```bash
    streamlit run app.py
    ```

This will start the Streamlit web server. A local URL (usually `http://localhost:8501`) will be displayed in your terminal, and the app should open automatically in your web browser.

*Note: If you are running this in a Colab environment, you can use `pyngrok` as shown in the notebook to create a public URL.*

## How to Use the Recommendation System

Using the recommendation system through the Streamlit app is straightforward:

1.  **Enter a Song Title:** In the input box provided, type the name of a Tamil song you like. The system includes a fuzzy matching feature, so it might find a close match even if there are minor typos.
2.  **Select Number of Recommendations:** Use the slider to choose how many recommended songs you want to see (between 1 and 20).
3.  **Get Recommendations:** Click the "Get Recommendations" button.

The app will then display a table showing the recommended songs, including their names, singers, and stream counts (if available in the dataset).

## Data Source

The dataset used for this project (`Tamil_songs_90s_2Ks_latest.csv`) contains metadata and audio features for a collection of Tamil songs. (You might want to add more details about the data source if available).

## Future Improvements

-   Incorporate user feedback to refine recommendations.
-   Explore other recommendation techniques (e.g., collaborative filtering).
-   Expand the dataset to include more songs and potentially other languages.
-   Improve the fuzzy matching algorithm or provide suggestions to the user.

## Contact

(Optional: Add your contact information or links to your profiles here.)

Please copy the following markdown content and paste it into a file named `README.md` in your project's root directory.


# Tamil Song Recommendation System

## Project Overview

This project implements a content-based music recommendation system specifically for Tamil songs from the 90s, 2000s, and recent times. The system recommends songs based on their audio features like danceability, acousticness, energy, etc., using cosine similarity to find similar tracks. A Streamlit web application provides an interactive interface for users to get song recommendations.

Key features:
- **Content-Based Filtering:** Recommends songs based on audio characteristics.
- **Cosine Similarity:** Measures the similarity between songs using their scaled audio features.
- **Streamlit Web App:** Provides an easy-to-use graphical interface.
- **Fuzzy Matching:** Handles minor variations or typos in song titles entered by the user.

## Setup

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace with the actual repository URL
    cd <repository_name>
    ```

2.  **Install dependencies:**
    This project requires Python 3.6+ and the following libraries. You can install them using pip:
    ```bash
    pip install pandas scikit-learn streamlit fuzzywuzzy python-Levenshtein pyngrok
    ```

3.  **Obtain the dataset:**
    Place the `Tamil_songs_90s_2Ks_latest.csv` file in the project directory (or specify the correct path in `app.py`).

## How to Run the Streamlit App

Once the setup is complete, you can run the Streamlit application:

1.  Open your terminal or command prompt in the project directory.
2.  Execute the following command:
    ```bash
    streamlit run app.py
    ```

This will start the Streamlit web server. A local URL (usually `http://localhost:8501`) will be displayed in your terminal, and the app should open automatically in your web browser.

*Note: If you are running this in a Colab environment, you can use `pyngrok` as shown in the notebook to create a public URL.*

## How to Use the Recommendation System

Using the recommendation system through the Streamlit app is straightforward:

1.  **Enter a Song Title:** In the input box provided, type the name of a Tamil song you like. The system includes a fuzzy matching feature, so it might find a close match even if there are minor typos.
2.  **Select Number of Recommendations:** Use the slider to choose how many recommended songs you want to see (between 1 and 20).
3.  **Get Recommendations:** Click the "Get Recommendations" button.

The app will then display a table showing the recommended songs, including their names, singers, and stream counts (if available in the dataset).

## Data Source

The dataset used for this project (`Tamil_songs_90s_2Ks_latest.csv`) contains metadata and audio features for a collection of Tamil songs. (You might want to add more details about the data source if available).

## Future Improvements

-   Incorporate user feedback to refine recommendations.
-   Explore other recommendation techniques (e.g., collaborative filtering).
-   Expand the dataset to include more songs and potentially other languages.
-   Improve the fuzzy matching algorithm or provide suggestions to the user.

## Contact

(Optional: Add your contact information or links to your profiles here.)

Summary:
Data Analysis Key Findings
The project implements a content-based Tamil song recommendation system using audio features and cosine similarity.
A Streamlit web application provides a user interface for the recommendation system.
The setup instructions include cloning the repository, installing dependencies (pandas, scikit-learn, streamlit, fuzzywuzzy, python-Levenshtein, pyngrok), and obtaining the dataset (Tamil_songs_90s_2Ks_latest.csv).
The Streamlit app can be run using the command streamlit run app.py.
Users can get recommendations by entering a song title and selecting the number of recommendations in the Streamlit app.
Insights or Next Steps
The generated README content provides a comprehensive guide for users to understand, set up, and use the Tamil song recommendation system.
The inclusion of sections like "Future Improvements" suggests potential directions for enhancing the project.
