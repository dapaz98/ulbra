import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer


def normalize_target_variable(df: pd.DataFrame):
    df["target"] = df["num"].apply(lambda x: 1 if x > 0 else 0)
    return df

def data_balancing(y):
    target_count = y.value_counts()

    minority_class = target_count.idxmin()
    majority_class = target_count.idxmax()

    print("Minority class =", minority_class, ":", target_count[minority_class])
    print("Majority class =", majority_class, ":", target_count[majority_class])
    print(
        "Proportion:",
        round(target_count[minority_class] / target_count[majority_class], 2),
        ": 1",
    )


def create_preprocessor(X):
    numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())]), numeric_cols),

            ('cat', Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('encoder', OneHotEncoder(drop='first'))]), categorical_cols)
        ])

    return preprocessor


def split_dataset(X, y, test_size=0.3, random_state=42):
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )


def normalization_process(df: pd.DataFrame):
    df = normalize_target_variable(df)

    X = df.drop(columns=['dataset', 'num', 'target', 'thalch']) 
    y = df['target']

    data_balancing(y)

    X_train, X_test, y_train, y_test = split_dataset(X, y)

    preprocessor = create_preprocessor(X)

    return X_train, X_test, y_train, y_test, preprocessor
