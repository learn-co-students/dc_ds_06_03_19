from datetime import datetime
import scipy.stats
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def extract_year_mon_day_cols_from_date_col(df):
    df['Year'], df['Month'], df['Day'] = df['Date'].dt.year, df['Date'].dt.month, df['Date'].dt.day
    return df

def remove_miss_col_with_bigger_than_share(df, share):
    df = df.loc[:, (df.isnull().sum(axis=0) / df.shape[0]) <= share]
    
    return df

def get_mode_col_w_missing_vals(df, col_name, groupby_cols = None):
    mode = df[groupby_cols + [col_name]][~df[col_name].isna()].groupby(groupby_cols) \
    .agg(lambda x: scipy.stats.mode(x)[0])[col_name].reset_index()
    # merge with df
    df = pd.merge(df, mode, on=groupby_cols, suffixes=('', '_mode'))
    return df

def get_median_col_w_missing_vals(df, col_name, groupby_cols = None):
    median = df[groupby_cols + [col_name]][~df[col_name] \
                                                               .isna()].groupby(groupby_cols) \
                                                            .median()[col_name].reset_index()
    # merge with df
    df = pd.merge(df, median, on=groupby_cols, suffixes=('', '_median'))
    return df

def wrapper_median_mode_df(df): 
    for column in list(df.columns[df.isna().sum() > 0]):
        if df[column].dtype == 'O':
            df = get_mode_col_w_missing_vals(df, column, ['Location','Year','Month'])
            df = if_na_get_mode_or_median(df, column, func = 'mode')
        else:
            df = get_median_col_w_missing_vals(df, column, ['Location','Year','Month'])
            df = if_na_get_mode_or_median(df, column, func = 'median')
    return df

def if_na_get_mode_or_median(df, col_name, func = 'mode'):
    df.loc[df[col_name].isna(), col_name] = df[df[col_name].isna()][col_name + '_' + func]
    df = df.drop(col_name + '_' + func, axis=1)
    return df

def if_no_rainToday_zero_rainfall(df):
    df['Rainfall'] = df[['Rainfall', 'RainToday']].apply(lambda x: x['Rainfall'] \
                                                                          if x['RainToday'] == 'Yes' else 0 , axis =1)
    
    return df

def transform_string_to_date(pd_series):
    pd_series = pd_series.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    return pd_series


def transform_yes_no_col_to_binary(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: 1 if x == 'Yes' else 0)
    return df


def cleanup(df):
	df = df.drop('RISK_MM', axis=1)
	df['Date'] = transform_string_to_date(df['Date'])
	df = extract_year_mon_day_cols_from_date_col(df)
	print("There are " + str(sum(df.duplicated(subset=['Date','Location'], keep=False))) + " duplicated dates here!")
	df = df.drop('Date', axis=1)
	df = remove_miss_col_with_bigger_than_share(df, 0.35)
	df = wrapper_median_mode_df(df)
	df = if_no_rainToday_zero_rainfall(df)
	df = transform_yes_no_col_to_binary(df, 'RainToday')
	df = transform_yes_no_col_to_binary(df, 'RainTomorrow')
	num_cols = df.columns[df.dtypes == 'float64']
	cat_cols = df.columns[df.dtypes == 'object'][1:]
	return cat_cols, num_cols, df

def main():
	pass
