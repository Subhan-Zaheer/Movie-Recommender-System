import numpy as np
import pandas as pd
import streamlit as sl
import pickle


def get_top_similars(vectors, top_similar):
    if not top_similar:
        return f"Top Similar value is {top_similar}, but it should be greater than 0."
    return np.argsort(vectors)[::-1][1:top_similar+1]


def get_movies(df, index, top_similar, vector):
    vectors = df.iloc[index][f'{vector}_vectors']
    indexes = get_top_similars(vectors, top_similar)
    return df.iloc[indexes].title.values


def get_index_of_movie(df, name):
    return df[df['title'] == name].index[0]


def recommendation(df, name, top_similar, vector):
    if name not in df['title'].values:
        return "Enter a correct movie name. This name is not present in data."
    else:
        index = get_index_of_movie(df, name)
        return get_movies(df, index, top_similar, vector)

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))

movies = pd.DataFrame(movie_dict)


sl.title('Movie Recommender System')

options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

movie_titles = movies['title'].values

# Create the dropdown
selected_movie = sl.selectbox('Choose a movie:', movie_titles)
selection_vector = sl.selectbox('Select a vector:', ['bow', 'ngram'])

btn = sl.button('Get Recommendations')

if btn:
    recommendations = recommendation(movies, selected_movie, 5, selection_vector)

    for i in recommendations:
        sl.write(i)