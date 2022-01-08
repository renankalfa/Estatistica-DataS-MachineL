from groupsampling import *
from simplerandom import *
from reservoirsampling import *
from stratifiedsampling import *
from systematicsampling import *

dataset = pd.read_csv('census.csv')

print(dataset['age'].mean())
print(amostragem_aleatoria_simples(dataset, 100)['age'].mean())
print(amostragem_sistematica(dataset, 100)['age'].mean())
print(amostragem_agrupamento(dataset, 100)['age'].mean())
print(amostragem_estratificada(dataset, 100)['age'].mean())
print(amostragem_reservatorio(dataset, 100)['age'].mean())
# Reservatório se aproximou melhor
