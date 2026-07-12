import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dataset
movies = pd.read_csv("movies.csv")

# Fill missing values
movies['genres'] = movies['genres'].fillna('')

# Convert genres into vectors
cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(movies['genres'])

# Calculate cosine similarity
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# Reset index
movies = movies.reset_index()

# Create title-to-index mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


def get_recommendations(title):
    """
    Returns the top 10 movie recommendations based on genre similarity.
    """

    # Check whether the movie exists
    if title not in indices:
        return ["Movie not found! Please enter the exact movie title."]

    idx = indices[title]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Ignore the first movie (itself)
    sim_scores = sim_scores[1:11]

    # Get recommended movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return recommended movie titles
    return movies['title'].iloc[movie_indices].tolist()


# Test the recommendation system
if __name__ == "__main__":
    movie_name = input("Enter Movie Name: ")

    recommendations = get_recommendations(movie_name)

    print("\nRecommended Movies:\n")

    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")