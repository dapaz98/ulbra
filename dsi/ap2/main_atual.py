from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('heart_disease_uci.csv')

df['target'] = df['num'].apply(lambda x: 1 if x > 0 else 0)


X = df.drop(columns=['id', 'dataset', 'num', 'target'])
y = df['target']

categorical_cols = ['sex', 'cp', 'restecg', 'slope', 'thal', 'exang', 'fbs']
numeric_cols = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca']


preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())]), numeric_cols),

        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first'))]), categorical_cols)
    ])

clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)


clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


print("Acurácia:", accuracy_score(y_test, y_pred))
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
# plt.title("Matriz de Confusão")
# plt.xlabel("Previsto")
# plt.ylabel("Real")
