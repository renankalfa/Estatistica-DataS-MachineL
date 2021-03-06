import pandas as pd
import numpy as np
import random

# dataset = pd.read_csv('census.csv')


def amostragem_agrupamento(dataset, numero_grupos):
    intervalo = len(dataset) // numero_grupos
    grupos = []
    id_grupo = contagem = 0
    for _ in dataset.iterrows():
        grupos.append(id_grupo)
        contagem += 1
        if contagem > intervalo:
            contagem = 0
            id_grupo += 1
    dataset['grupo'] = grupos
    random.seed(1)
    grupo_selecionado = random.randint(0, numero_grupos)
    return dataset[dataset['grupo'] == grupo_selecionado]


# Desativado para comparação
# print(amostragem_agrupamento(dataset, 325).head())
