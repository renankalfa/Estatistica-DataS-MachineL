import pandas as pd
# import numpy as np
import random

dataset = pd.read_csv('census.csv')


def amostragem_aleatoria_simples(dataset, amostras):
    return dataset.sample(n=amostras, random_state=1)


# Desativado para comparação
# print(amostragem_aleatoria_simples(dataset, 100).head())
