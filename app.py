import streamlit as st
import pickle
import pandas as pd
from click import option

def hybrid_recommendation(user_id, movie_title, top_n=10):
    title_match = movies[movies['title'] == movie_title]

    if title_match.empty:
        print(f"Title '{movie_title}' not found in the dataset.")
        return []
    # User-based recommendations
    user_recs = set(get_user_recommendations(user_id, top_n))

    # Item-based recommendations
    item_recs = set(get_item_recommendations(movie_title, top_n))

    # Content-based recommendations
    content_recs = set(get_content_recommendations(movie_title))

    # Combine recommendations (intersection or union)
    final_recs = list(user_recs | item_recs | content_recs )[:top_n]

    return final_recs

# Example: Hybrid recommendations for a user and a movie
hybrid_recomendation=hybrid_recommendation(9, 'Action Jackson (1988)')
df1= pd.DataFrame(hybrid_recomendation, columns=['Movie Titles'])
print(df1)

movies_dict=pickle.load(open('movies1_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

options = st.selectbox(
    'How do you like to',
    movies['title'].values)

if st.button('Recommend'):
    st.write(options)