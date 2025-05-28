import pandas as pd 
from data_preparation.pre_processing import normalization_process
from models import slp
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd


DIR_FILE_CREDIT_ANALISYS = "/home/eduardo-da-paz/Documents/university/ulbra/dsi/ap2/dataset/heart_disease_uci.csv"

def main():
    if DIR_FILE_CREDIT_ANALISYS:
        df_heart_disease = pd.read_csv(DIR_FILE_CREDIT_ANALISYS, index_col="id")
        normalization_process(df_heart_disease)


        # Aplicar processamento
        X_train, X_test, y_train, y_test, preprocessor = normalization_process(df_heart_disease)

        # Ajustar pré-processamento nos dados de treino
        preprocessor.fit(X_train)

        # Transformar dados
        X_train_processed = preprocessor.transform(X_train)
        X_test_processed = preprocessor.transform(X_test)

        clf = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000, random_state=42))
        ])

        clf.fit(X_train_processed, y_train)


        y_pred = clf.predict(X_test_processed)


        print("Acurácia:", accuracy_score(y_test, y_pred))
        print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

        cm = confusion_matrix(y_test, y_pred)
    else:
        print("file not informed")
                

def process_datasets():
    
    return

def train_models(credit_analysis: pd.DataFrame):
    X = credit_analysis[["renda", "divida"]]  # Variáveis independentes
    y = credit_analysis["classe"]  # Convertendo classe para 0 e 1 
    slp.slp_process(X, y)


if __name__ == '__main__':
    main()