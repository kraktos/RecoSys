"""
implement a basic recommender system
"""
import pandas as pd
from sklearn.cross_validation import train_test_split


# define the inception of the code
def start():
    # load the users file
    users_df = pd.read_csv("data/users.dat", sep="::", names=['user_id', 'age', 'sex', 'occupation', 'zip_code'])
    print "Users dimension = {}".format(users_df.shape)

    # load the movie file
    movies_df = pd.read_csv("data/movies.dat", sep="::", names=["movie_id", "movie_name", "movie_genre"])

    unique_vals = movies_df['movie_genre']
    vals = "|".join(unique_vals)
    uniques = list(set(vals.split("|")))

    # prepopulate with all 0 s
    for val in uniques:
        movies_df[val] = 0

    # parse the genre to create boolean features
    for index, row in movies_df.iterrows():
        vals = row['movie_genre'].split("|")
        for val in vals:
            movies_df.loc[index, val] = 1

    # drop the redundant column
    del movies_df['movie_genre']

    print "Movies dimension = {}".format(movies_df.shape)

    # load the ratings file
    ratings_df = pd.read_csv("data/ratings.dat", sep="::", names=["user_id", "movie_id", "rating", "ts"])

    # split train/test on the ratings file
    train_ratings_df, test_ratings_df = train_test_split(ratings_df, test_size=0.25)

    print "Ratings Dimension (train){}, (test){}".format(train_ratings_df.shape, test_ratings_df.shape)

    #

if __name__ == '__main__':
    start()
