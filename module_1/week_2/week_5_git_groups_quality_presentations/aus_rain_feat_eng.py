import pandas as pd

def transform_to_dummies(df, cols):
    dummies =  pd.get_dummies(df[cols])
    df = df.drop(cols, axis =1)
    df = pd.concat([df, dummies], axis=1)
    return df