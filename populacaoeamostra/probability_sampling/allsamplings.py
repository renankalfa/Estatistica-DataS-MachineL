import numpy as np
import random
from sklearn.model_selection import StratifiedShuffleSplit


def divider():
    print('=' * 72)


def amostragem_aleatoria_simples(dataset, amostras):
    return dataset.sample(n=amostras, random_state=1)


def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica


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


def amostragem_agrupamentoex1(dataset, numero_grupos):
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


def amostragem_estratificada(dataset, amostras):
    percentual = amostras / len(dataset)
    divido = StratifiedShuffleSplit(test_size=percentual, random_state=1)
    for _, y in divido.split(dataset, dataset['income']):
        df_y = dataset.iloc[y]
    return df_y


def amostragem_estratificadae_ex1(dataset, amostras):
    percentual = amostras / len(dataset)
    divido = StratifiedShuffleSplit(test_size=percentual, random_state=1)
    for _, y in divido.split(dataset, dataset['c#default']):
        df_y = dataset.iloc[y]
    return df_y


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
