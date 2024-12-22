import streamlit as st
import pickle
import pandas

def recommend(movie):
    movie_index = list(movies_list).index(movie)
    distances = similarity[movie_index]
    mlist = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in mlist:
        recommended_movies.append(movies_list[i[0]])
    return recommended_movies
movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be Recommended For',
(movies_list)
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)





