import pandas as pd
from populacaoeamostra.probability_sampling.allsamplings import *

dataset = pd.read_csv('credit_data.csv')

# Testando a amostragem aleatória simples
print(amostragem_aleatoria_simples(dataset, 1000).head())
divider()

# Testando a amostragem sistemática
print(amostragem_sistematica(dataset, 1000).head())
divider()

# Testando a amostragem por grupos
print(amostragem_agrupamento(dataset, 1000).head())
divider()

# Testando a amostragem estratificada
print(amostragem_estratificadae_ex1(dataset, 1000).head())
divider()

# Testando a amostragem de reservatório
print(amostragem_reservatorio(dataset, 1000).head())
divider()
# teste git
# Comparando as médias do income
print(dataset['income'].mean())
print(amostragem_aleatoria_simples(dataset, 1000)['income'].mean())      # 232
print(amostragem_sistematica(dataset, 1000)['income'].mean())            # 360
print(amostragem_agrupamento(dataset, 2)['income'].mean())               # 485
print(amostragem_estratificadae_ex1(dataset, 1000)['income'].mean())     # 230
print(amostragem_reservatorio(dataset, 1000)['income'].mean())           # 220
# A que mais se aproximou foi a de reservatório
divider()
# Comparando as médias do age
print(dataset['age'].mean())
print(amostragem_aleatoria_simples(dataset, 1000)['age'].mean())         # 0,312
print(amostragem_sistematica(dataset, 1000)['age'].mean())               # 0,104
print(amostragem_agrupamento(dataset, 2)['age'].mean())                  # 0,236
print(amostragem_estratificadae_ex1(dataset, 1000)['age'].mean())        # 0,274
print(amostragem_reservatorio(dataset, 1000)['age'].mean())              # 0,235
# A que mais se aproximou foi a sistemática
divider()
# Comparando as médias de loan
print(dataset['loan'].mean())
print(amostragem_aleatoria_simples(dataset, 1000)['loan'].mean())        # 5
print(amostragem_sistematica(dataset, 1000)['loan'].mean())              # 62
print(amostragem_agrupamento(dataset, 2)['loan'].mean())                 # 54
print(amostragem_estratificadae_ex1(dataset, 1000)['loan'].mean())       # 21
print(amostragem_reservatorio(dataset, 1000)['loan'].mean())             # 15
# A que mais se aproximou foi a aleatórica simples
divider()
# Dá pra otimizar mais, criando uma lista com os itens que quero calcular a média.
