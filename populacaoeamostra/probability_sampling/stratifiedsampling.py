from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd

dataset = pd.read_csv('census.csv')


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
# Desativado para comparação
# print(amostragem_estratificada(dataset, 100).head())
