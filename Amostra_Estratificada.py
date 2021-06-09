import pandas as pd  # biblioteca responsavel para carregar a analise de dados

from sklearn.model_selection import train_test_split # biblioteca usada bastante em machine learn e a função é utilizada para fazer a divição da base da dados

iris = pd.read_csv('iris.csv')  # pd.read_csv para ler arquivos do tipo .csv
iris['class'].value_counts()  # fazendo a contagem do atributo class

# Separa pela metade a class entre a variavel x e y
X, _, y, _ = train_test_split(
    iris.iloc[:, 0:4], iris.iloc[:, 4], test_size=0.5, stratify=iris.iloc[:, 4])

print(y.value_counts())  # mostra os valores de y

infert = pd.read_csv('infert.csv')  # pd.read_csv para ler arquivos do tipo csv

print('\n', '\n', infert['education'].value_counts()) # mostra os valores da colunoa education do arquivo infert
