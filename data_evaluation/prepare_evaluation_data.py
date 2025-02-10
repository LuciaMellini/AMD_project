import requests
from tqdm import tqdm
import pandas as pd
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = '134f6127b94264ff458f2b2b0ace38fd'
BASE_URL = 'https://api.themoviedb.org/3'
DATA_DIR = 'evaluation_data/'


def get_movies_in_dataset(filename, sample_size = None):
    df = pd.read_csv(filename, nrows=(sample_size if sample_size else None))
    return df

def search_movie_by_title(movie_title, release_year=None):
    search_url = f"{BASE_URL}/search/movie"
    params = {
        'api_key': API_KEY,
        'query': movie_title,  
    }
    
    if release_year:
        params['year'] = release_year 
    
    response = requests.get(search_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            movie = data['results'][0]  # only consider first movie found
            return movie['id']
        else:
            return "-1"
    else:
        response.raise_for_status()

def get_id_map(filename=None):
    if filename and os.path.exists(filename):
        with open(filename, "r") as infile:
            id_to_tmdb_id = json.load(infile)
        id_to_tmdb_id = {int(k):v for k,v in id_to_tmdb_id.items()}

    else:
        movies_df['tmdb_id'] = [search_movie_by_title(movie['name'], movie['date'])
                           for _, movie in tqdm(movies_df.iterrows(), total = n_movies, desc="Translating movie ids to TMDB ids")]
    
        id_to_tmdb_id = dict(zip(movies_df['id'], movies_df['tmdb_id']))
        
        if filename:
            with open(filename, "w") as outfile:
                json.dump(id_to_tmdb_id, outfile, indent=4)
            
    return id_to_tmdb_id
    
def fetch_page_similar_movies(movie_id, page):
    url = f"{BASE_URL}/movie/{movie_id}/similar"
    params = {
        'api_key': API_KEY,
        'page': page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()    

def search_similar_movie_ids(movie_id, n_pages=500):
    all_similar_movie_ids = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(fetch_page_similar_movies, movie_id, page) for page in range(1, n_pages + 1)]

        for future in as_completed(futures):
            data = future.result()  
            
            similar_movie_ids = [movie['id'] for movie in data['results']]
            all_similar_movie_ids.extend(similar_movie_ids)
    
    return all_similar_movie_ids

def get_similar_movie_ids(movie_df, n_pages, filename=None):
    if filename and os.path.exists(filename):
        with open(filename, "r") as infile:
            similar_movie_ids = json.load(infile)
    else:
        similar_movie_ids = {movie['tmdb_id']: list(set(search_similar_movie_ids(movie['tmdb_id'], n_pages))) 
                        for idx, movie in tqdm(movies_df.iterrows(), total=n_movies, desc="Extracting similar movies from TMDB")}
        
        valid_ids = set(movies_df['tmdb_id'])
        similar_movie_ids = {movie_id: [similar_id for similar_id in similar_list if similar_id in valid_ids] 
                        for movie_id, similar_list in similar_movie_ids.items()}
        if filename:                    
            with open(filename, "a") as outfile:
                json.dump(similar_movie_ids, outfile, indent=4)
                
    return similar_movie_ids    
        
if __name__ == "__main__":
    
    n_movies = 100
    movies_df = get_movies_in_dataset('letterboxd/movies.csv', sample_size=n_movies)
    movies_df = movies_df[['id', 'name', 'date']]
    
    id_to_tmdb_id = get_id_map(DATA_DIR + "movie_ids_map_test.json")     
    movies_df['tmdb_id'] = movies_df['id'].map(id_to_tmdb_id)
    
    similar_movies = get_similar_movie_ids(movies_df, 10, DATA_DIR + "similar_movies_test.json")
  
