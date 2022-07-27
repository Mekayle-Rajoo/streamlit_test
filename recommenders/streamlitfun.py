def collab(movie1,movie2, movie3, min_year):

    import pandas as pd
    from PIL import Image
    import requests
    from io import BytesIO
    import pickle

    train_data = pd.read_csv('resources/data/streamlit_ratings.csv')
    movies = pd.read_csv('resources/data/movies27000.csv')
    unpickled_model=pickle.load(open('resources/models/CW3_SVD.pkl', 'rb'))


    
    movies123 = train_data[(train_data["title"]==movie1)|(train_data["title"]==movie2)|(train_data["title"]==movie3)]
    
    if len(movies123)>150:
        movies123 = movies123.sort_values("rating").tail(150)
    
    watch_counts = pd.DataFrame(movies123["userId"].value_counts())
    max_watch_counts = watch_counts["userId"].max()
    
    users = list(watch_counts[watch_counts["userId"]==max_watch_counts].index)
    
    movieid = list(set(movies["movieId"][movies["year"]>min_year-1]))
    
    bestmatched = []

    for iid in movieid:
        movieaverage = []
        for uid in users:
            userprediction = unpickled_model.predict(uid, iid)[3]
            movieaverage.append(userprediction)
            
        if sum(movieaverage)/len(movieaverage)>4:
                bestmatched.append(iid)
                
                
             
    bestmatched = list(set(bestmatched))
    
    titles = movies[movies["movieId"].isin(bestmatched) & (movies["year"]>min_year-1)][["title","link", "image"]].reset_index()
    
    if len(titles)>10:
        titles =titles.sample(n=10).reset_index()


    return list(titles["title"])