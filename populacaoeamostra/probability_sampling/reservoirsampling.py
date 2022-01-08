import pandas as pd
import random

dataset = pd.read_csv('census.csv')


def amostragem_reservatorio(dataset, amostras):
    stream = []
    # Cria uma lista de número do tamanho do dataset
    for c in range(len(dataset)):
        stream.append(c)
    i = 0
    tamanho = len(dataset)
    # Cria uma lista de 100 elementos 0
    reservatorio = [0] * amostras
    # Transforma em uma lista de 0 a 99
    for i in range(amostras):
        reservatorio[i] = stream[i]
    # Dá oportunidade para todos os elementos serem selecionados
    while i < tamanho:
        j = random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i += 1
    return dataset.iloc[reservatorio]


# Desativado para comparação
# print(amostragem_reservatorio(dataset, 100))
