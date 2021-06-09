import pandas as pd # biblioteca responsavel para carregar a analise de dados
import numpy as np

base = pd.read_csv('iris.csv') # armazena na variavel base a leitura de um arquivo iris.csv na pasta
print(base) # mostra o que tem dentro da variavel base

np.random.seed(12345) # trava os valores 
amostra = np.random.choice(a = [0,1], size = 150, replace = True, p = [0.5,0.5]) # espalha valores de 0 e 1 com chance de 50% na amostra do arquivo

print(len(amostra)) # tamanho da amostra
print(len(amostra[amostra == 1])) # quantidade de 1 na amostra
print(len(amostra[amostra == 0])) # quantidade de 0 na amostra
