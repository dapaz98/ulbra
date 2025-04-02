import pandas as pd 
from models import slp
import os

DIR_FILE_CREDIT_ANALISYS = "/home/eduardo-da-paz/Documents/university/ulbra/dsi/exercise_II/dataset"

def main():
        for file in os.scandir(DIR_FILE_CREDIT_ANALISYS):
            if file.is_file():
                credit_analysis = pd.read_csv(file.path, index_col="n")
                train_models(credit_analysis)
                print(f"file: {file.path}")

def train_models(credit_analysis: pd.DataFrame):
    X = credit_analysis[["x1", "x2"]]  # Variáveis independentes
    y = credit_analysis["d"]  # Convertendo classe para 0 e 1 
    slp.slp_process(X, y)


if __name__ == '__main__':
    main()