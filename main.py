import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        response = requests.get(url)

        # If API fails
        if response.status_code != 200:
            return None

        data = response.json()
        poster_path = data.get('poster_path')

        # If no poster available
        if poster_path is None:
            return None

        return "https://image.tmdb.org/t/p/w500/" + poster_path

    except:
        return None

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id   
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].original_title)

    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommender System')

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['original_title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)

    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])
        else:
            st.write("No Image")

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])
        else:
            st.write("No Image")

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])
        else:
            st.write("No Image")

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])
        else:
            st.write("No Image")

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])
        else:
            st.write("No Image")