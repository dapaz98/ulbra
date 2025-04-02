import pandas as pd 
from data_preparation.pre_processing import normalization_process
from data_balancing.data_balancer import balance_process
from models import slp
import os

DIR_FILE_CREDIT_ANALISYS_0 = "/home/eduardo-da-paz/Documents/university/ulbra/dsi/task_1/dataset/analise_credito.csv"
DIR_FILE_CREDIT_ANALISYS_1 = "/home/eduardo-da-paz/Documents/university/ulbra/dsi/task_1/dataset"

def main():
    if DIR_FILE_CREDIT_ANALISYS_1:
        credit_analysis = pd.read_csv(DIR_FILE_CREDIT_ANALISYS_0, index_col="cliente")
        credit_analysis = balance_process(credit_analysis)
        credit_analysis = normalization_process(credit_analysis)
        train_models(credit_analysis)
    else:
        for file in os.scandir(DIR_FILE_CREDIT_ANALISYS_1):
            if file.is_file():
                credit_analysis = pd.read_csv(DIR_FILE_CREDIT_ANALISYS_0, index_col="n")
                train_models(credit_analysis)

                

def process_datasets():
    
    return

def train_models(credit_analysis: pd.DataFrame):
    X = credit_analysis[["renda", "divida"]]  # Variáveis independentes
    y = credit_analysis["classe"]  # Convertendo classe para 0 e 1 
    slp.slp_process(X, y)


if __name__ == '__main__':
    main()