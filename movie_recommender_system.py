#movie recommender system
import numpy as np
import pandas as pd

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

#print(movies.head())
#print(credits.head(1)['crew'].values)
#print(credits.head(1))

movies=movies.merge(credits, on='title')

#genres, id, keyword, title, overview, popularity, cast, crew
#print(movies['original_language'].value_counts())
#print(movies.info())
movies=movies[['movie_id','title','overview','genres','keywords','cast','crew']]

#for missing values
#print(movies.isnull().sum())
#overview    3
movies.dropna(inplace=True)
#print(movies.isnull().sum())

#ckeck duplicate values are there or not
#print(movies.duplicated().sum()) #no duplicate value

# print(movies.iloc[0].genres)
# to check there is any need to change or not

import ast
def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def convert3(obj):
    l = []
    count=0
    for i in ast.literal_eval(obj):
        if count!=0:
            l.append(i['name'])
            count+=1
        else:
            break
    return l
movies['cast'] = movies['cast'].apply(convert3)
#print(movies.head())

def fetch_director(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            l.append(i['name'])
            break
    return l
# print(movies['crew'].apply(fetch_director)) 
movies['crew'] = movies['crew'].apply(fetch_director)
#print(movies.head())

# print(movies['genres']) for removing places to better ML
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
# print(movies['genres'])

movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['tags'] = movies['overview'] + movies['genres'] + movies['cast'] + movies['keywords'] + movies['crew']
#print(movies.head())

new_df = movies[['movie_id','title','tags']]
#print(new_df)

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
# print(new_df.head())
# print(new_df['tags'][0])

# for converting in lower case
new_df['tags'] = new_df['tags'].astype(str).apply(lambda x:x.lower())
new_df['title'] = new_df['title'].astype(str).apply(lambda x:x.lower())
new_df['movie_id'] = new_df['movie_id'].astype(str).apply(lambda x:x.lower())
# print(new_df.head())
# print("-"*15 +"*"+"-"*15)

import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

# print(stem("loved")) to check stem function is working or not
new_df['tags']=new_df['tags'].apply(stem)
# print(new_df.head())

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()
# print(vectors[0])
# print(cv.get_feature_names_out())

from sklearn.metrics.pairwise import cosine_similarity
# print(cosine_similarity(vectors).shape)
similarity = cosine_similarity(vectors) #similaruty is a matrix

# l=sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x:x[1])[1:6]
# print(l)

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    for i in movies_list:
        print(new_df.iloc[i[0]].title)

recommend('avatar')
recommend('batman begins')