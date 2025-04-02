import pandas as pd 
from sklearn.preprocessing import MinMaxScaler 
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from scipy.stats import zscore
import numpy as np


CLASS_VARIABLE = "classe"
def remove_outliers(df_credit_analysis: pd.DataFrame):
    df_credit_analysis = df_credit_analysis[(np.abs(zscore(df_credit_analysis)) < 3).all(axis=1)]
    return

def categorization_variable(df_credit_analysis):
    df_credit_analysis[CLASS_VARIABLE] = df_credit_analysis[CLASS_VARIABLE].map({"mau": False, "bom": True})
    return df_credit_analysis

def generate_target_data(data):
    target_data = data[[CLASS_VARIABLE]].copy()
    return target_data

def min_max_scaler(df_credit_analysis: pd.DataFrame):
    remaining_vars = [col for col in df_credit_analysis.columns if col not in [CLASS_VARIABLE]]
    target_data = generate_target_data(df_credit_analysis)
    df_credit_analysis.drop(columns=[CLASS_VARIABLE], inplace=True)

    transf: MinMaxScaler = MinMaxScaler(feature_range=(-1, 3), copy=True).fit(df_credit_analysis)

    df_minmax = pd.DataFrame(transf.transform(df_credit_analysis), columns=(remaining_vars), index=df_credit_analysis.index)
    df_minmax[[CLASS_VARIABLE]] = target_data


    return df_minmax

def split_dataset(X, y, test_size=0.3, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    return X_train, X_test, y_train, y_test

def normalization_process(df_credit_analysis: pd.DataFrame):
    df_credit_analysis = categorization_variable(df_credit_analysis)
    df_credit_analysis = min_max_scaler(df_credit_analysis)
    return df_credit_analysis

