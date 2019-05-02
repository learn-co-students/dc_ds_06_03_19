import pandas as pd
import numpy as np
import time
from sklearn import tree, ensemble


def tr_te_split(df, traget_col, cond_col, cond):
    index_split = df[cond_col] > cond
    tr_x, tr_y, te_x, te_y = df.loc[index_split, df.columns != traget_col], \
    df.loc[index_split, traget_col], df.loc[~index_split, df.columns != traget_col], \
    df.loc[~index_split, traget_col] 
    
    return tr_x, tr_y, te_x, te_y

def calc_misclass_error(pred, target):
    error = np.where((pred == target) == False)[0].shape[0]/ target.shape[0]
    return error


def model(australian_rain_df):
    feat_importance = {}
    results = {'Model': ['-'], 'Training misclassification': ['-'], 'Test misclassification': ['-'], 'Runtime': ['-']}
    results_pd = pd.DataFrame(data = results)
    models = ['Tree', 'Random forest']
    # split to training data and test data
    tr_x, tr_y, te_x, te_y = tr_te_split(australian_rain_df, 'RainTomorrow', 'Year', 2014)
    for kind in models:
        start = time.time()
        if kind == 'Tree':
            model = tree.DecisionTreeClassifier()
        else : 
            model = ensemble.RandomForestClassifier()
        
        model = model.fit(tr_x, tr_y)
        predict_tr = model.predict(tr_x)
        predict_te = model.predict(te_x)
        tr_err, te_err = calc_misclass_error(predict_tr, tr_y), calc_misclass_error(predict_te, te_y)
        feat_importance[kind] = model.feature_importances_
        end = time.time()
        runtime = round((end - start) / 60, 2)
        
        
        
        results_pd = results_pd.append(pd.DataFrame({'Model': [kind], 'Training misclassification': [str(round(tr_err, 2))], 
                                            'Test misclassification': [str(round(te_err, 2))], 'Runtime': [runtime]}))
        
    return feat_importance, results_pd

