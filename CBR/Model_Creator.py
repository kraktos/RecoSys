"""
The core idea behind a CBR system is to train a model on each of the users personal
preferences. Given a set of features as predictors and a target variable which is the rating,
it is possible to learn a parameter vector theta. Once theta is learned, we can predict the
likely rating for any given rating.
"""


# grab the users ratings, and the movies file
def train_CBR(user_ratings_df, movies_df):
    print user_ratings_df.shape
    print movies_df.shape


# predict the ratings
def predict(test_ratings_df):
