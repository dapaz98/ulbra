import pandas as pd
from data_preparation.pre_processing import split_dataset
from sklearn.linear_model import Perceptron
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score

def train(X_train, X_test, y_train):
    perceptron = Perceptron(max_iter=2000, eta0=1, random_state=42)
    perceptron.fit(X_train, y_train)
    y_pred = perceptron.predict(X_test)
    
    return y_pred

def cross_validate_model(X, y):
    perceptron = Perceptron(max_iter=2000, eta0=1, random_state=42)
    # Validação cruzada com 5 partições
    scores = cross_val_score(perceptron, X, y, cv=5)  # cv=5 faz 5-fold cross-validation
    print("Validação cruzada:", scores)
    print("Média da validação cruzada:", scores.mean())

def validate(y_pred, y_test):

    
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Confunsion Matrix:", confusion_matrix(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1-Score:", f1_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    

def slp_process(X, y):        
    cross_validate_model(X, y)
    X_train, X_test, y_train, y_test = split_dataset(X, y)
    y_pred= train(X_train, X_test, y_train, )
    validate(y_pred, y_test)
    