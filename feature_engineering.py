def create_features(df):
    X = df.drop("failure", axis=1)
    y = df["failure"]
    return X, y