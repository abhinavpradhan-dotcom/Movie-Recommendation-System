import pickle
import time
import streamlit as st
import requests

# DO NOT ABLE TO GENERATING PROPER OUTPUT
# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=0ddcd4065bd968b7a92d52bff21930c4&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# DO NOT ABLE TO GENERATING PROPER OUTPUT
# def fetch_poster(movie_id):
#     try:
#         url = "https://api.themoviedb.org/3/movie/{}?api_key=0ddcd4065bd968b7a92d52bff21930c4&language=en-US".format(movie_id)
#         response = requests.get(url, timeout=5) # Added a timeout
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#         return "https://via.placeholder.com/500x750?text=No+Poster" # Placeholder image
#     except Exception:
#         return "https://via.placeholder.com/500x750?text=Error"


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0ddcd4065bd968b7a92d52bff21930c4&language=en-US"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    # Try up to 3 times in case of temporary network latency or rate limit
    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                poster_path = data.get('poster_path')
                if poster_path:
                    return "https://image.tmdb.org/t/p/w500/" + poster_path
                return "https://via.placeholder.com/500x750?text=No+Poster"
            elif response.status_code == 429:
                time.sleep(1)  # Brief pause if rate-limited
                continue
            else:
                break
        except requests.exceptions.RequestException as e:
            time.sleep(0.5)
            
    return "https://via.placeholder.com/500x750?text=Poster+Unavailable"


def recommend(movie):

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate (similarity[index])), reverse=True, key = lambda x: x[1])
    recommended_movies = []
    recommended_posters = []
    time.sleep(0.2)
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters


movies = pickle.load(open('new_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = movies['title'].values
selected_movie_name = st.selectbox (
    "TYPE OR SELECT A MOVIE", movies_list
)

# DO NOT ABLE TO GENERATING PROPER OUTPUT
# if st.button("show Recommendation"):
#     st.write("Recommend Movies based on your intrests are")
#     recommended_movies_name, recommended_movies_poster = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movies_name[0])
#         st.image(recommended_movies_poster[0])
    
#     with col2:
#         st.text(recommended_movies_name[1])
#         st.image(recommended_movies_poster[1])
        
#     with col3:
#         st.text(recommended_movies_name[2])
#         st.image(recommended_movies_poster[2])
    
#     with col4:
#         st.text(recommended_movies_name[3])
#         st.image(recommended_movies_poster[3])
    
#     with col5:
#         st.text(recommended_movies_name[4])
#         st.image(recommended_movies_poster[4])

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])