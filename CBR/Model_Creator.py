"""
The core idea behind a CBR system is to train a model on each of the users personal
preferences. Given a set of features as predictors and a target variable which is the rating,
it is possible to learn a parameter vector theta. Once theta is learned, we can predict the
likely rating for any given rating.
"""
import pandas as pd


# grab the users ratings, and the movies file
def train_cbr(user_ratings_df, movies_df):
    # generate features and target
    df = pd.merge(left=user_ratings_df, right=movies_df, left_on='movie_id', right_on='movie_id')
    feature_list = list(user_ratings_df.columns.values) + list(movies_df.columns.values)
    feature_list.remove('rating')
    X_train = df.loc[:, set(feature_list)]
    y_train = df.loc[:, ['rating']]
    del X_train['movie_name']
    del X_train['ts']
    del X_train['movie_id']

    # group by user ids

    # fit a regression model for each user id


# predict the ratings
def predict(test_ratings_df):
    print test_ratings_df.shape