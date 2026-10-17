# Movie Recommendation System

A content-based movie recommendation system built using Python, Machine Learning, and Streamlit. This application recommends five similar movies based on the movie selected by the user and displays their posters using the TMDB API.

## Project Overview

The Movie Recommendation System analyzes movie metadata such as genres, keywords, cast, director, and overview to recommend similar movies. It uses text preprocessing, CountVectorizer, and cosine similarity to identify movies with similar content.

The project also includes an interactive Streamlit web application that allows users to select a movie and view five recommendations.

## Features

- Select a movie from a dropdown menu.
- Get five similar movie recommendations.
- Display recommended movie posters.
- Process movie metadata using Python.
- Apply text preprocessing and stemming.
- Calculate similarity between movies using cosine similarity.
- Interactive web interface built with Streamlit.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Requests
- Jupyter Notebook

## Project Structure

```text
Movie-Recommendation-System/
│
├── movie_recommend.ipynb
├── movie_recommender_system.py
├── App.py
├── requirements.txt
├── README.md
├── new_df.pkl
└── similarity.pkl
```

**Note:** The `new_df.pkl` and `similarity.pkl` files are required by the Streamlit application. Ensure they are available or provide a process to generate them.

## Dataset

This project uses the TMDB 5000 Movie Metadata dataset available on Kaggle.

**Dataset Link:**  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

The dataset contains movie information and credits used for data preprocessing and building the recommendation model.

Dataset files:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## How It Works

1. **Data Collection:** Load the movie metadata and credits datasets.
2. **Data Preprocessing:** Handle missing values and select relevant features.
3. **Feature Extraction:** Extract genres, keywords, cast, director, and movie overview.
4. **Text Combination:** Combine selected features into a single text field called tags.
5. **Text Processing:** Convert text to lowercase and apply stemming using NLTK.
6. **Vectorization:** Convert text into numerical features using CountVectorizer.
7. **Similarity Calculation:** Calculate cosine similarity between movie vectors.
8. **Movie Recommendation:** Identify the five most similar movies.
9. **Poster Display:** Fetch and display movie posters using the TMDB API.

## Installation and Usage

### 1. Download the Repository

Download the repository from GitHub using the **Code → Download ZIP** option and extract the files.

### 2. Install Dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 3. Prepare Required Files

Ensure the following files are available:

- `new_df.pkl`
- `similarity.pkl`

These files are loaded by `App.py`. If they are missing, generate them using the model-building workflow before running the application.

### 4. Configure TMDB API

The application uses the TMDB API to fetch movie posters. Configure your TMDB API key securely using Streamlit secrets or environment variables.

Do not publish API keys or credentials in a public GitHub repository.

### 5. Run the Application

Execute the following command:

```bash
streamlit run App.py
```

The application will open in your browser.

## How to Use

1. Open the Streamlit application.
2. Select a movie from the dropdown menu.
3. Click the **Recommend** button.
4. View five recommended movies along with their posters.

## Applications

- Personalized movie discovery
- Content-based recommendation systems
- Machine Learning practice
- Natural Language Processing
- Data preprocessing and feature extraction

## Future Improvements

- Add movie genre and release-year filters.
- Improve recommendations using TF-IDF.
- Add movie ratings and additional information.
- Improve error handling and application performance.
- Deploy the application online using Streamlit Community Cloud.

## Author

**Abhinav Pradhan**

GitHub: [GitHub Profile](https://github.com/abhinavpradhan-dotcom)

## Acknowledgements

- Kaggle for the TMDB 5000 Movie Metadata dataset.
- The Movie Database (TMDB) for movie poster information.
- The Python open-source community.

