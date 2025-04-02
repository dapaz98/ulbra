
from imblearn.over_sampling import SMOTE
from numpy import ndarray
import pandas as pd
CLASS_VARIABLE = "classe"

def smote(data):
    target_count: pd.Series = data[CLASS_VARIABLE].value_counts()

    positive_class = target_count.idxmin()
    negative_class = target_count.idxmax()
    
    RANDOM_STATE = 42

    smote: SMOTE = SMOTE(sampling_strategy="minority", random_state=RANDOM_STATE)
    y = data.pop(CLASS_VARIABLE).values
    X: ndarray = data.values
    smote_X, smote_y = smote.fit_resample(X, y)
    df_smote: pd.DataFrame = pd.concat([pd.DataFrame(smote_X), pd.DataFrame(smote_y)], axis=1)
    df_smote.columns = list(data.columns) + [CLASS_VARIABLE]


    smote_target_count: pd.Series = pd.Series(smote_y).value_counts()
    print("Minority class=", positive_class, ":", smote_target_count[positive_class])
    print("Majority class=", negative_class, ":", smote_target_count[negative_class])
    print(
        "Proportion:",
        round(smote_target_count[positive_class] / smote_target_count[negative_class], 2),
        ": 1",
    )

    return df_smote


def balance_process(df_credit_analysis: pd.DataFrame):
    df_credit_analysis = smote(df_credit_analysis)
    return df_credit_analysis