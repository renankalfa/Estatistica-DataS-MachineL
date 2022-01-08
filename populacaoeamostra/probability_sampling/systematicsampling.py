import pandas as pd
import numpy as np
import random

dataset = pd.read_csv('census.csv')


def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica


# Desativado para comparação
# print(amostragem_sistematica(dataset, 100).tail())
