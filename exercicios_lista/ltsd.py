# Lista
estados_lista = ['SP', 'RJ', 'MG']
print(estados_lista[1])       # RJ
estados_lista[1] = 'SC'
print(estados_lista)          # SP, SC, MG
estados_lista.append('AC')
print(estados_lista)          # SP, SC, MG, AC
estados_lista.insert(2, 'ES')
print(estados_lista)          # SP, SC, ES, MG, AC
estados_lista.remove('SP')
print(estados_lista)          # SC, ES, MG, AC
estados_lista.pop(1)
print(estados_lista)          # SC, MG, AC




#Tupla

estados_tupla = ('SP', 'RJ', 'MG')

#Set

estados_set = {'SP', 'RJ', 'MG'}

#Dict

estados_dict = {'SP':"Sao Paulo", "RJ":'Rio de Janeiro', 'MG':'Minas Gerais'}

#1- Armazene 5 frutas nas 4 estruturas

#- Array
#- estrutura de repetição
#- armazenamento(lista, tupla, set, dict)
#- print

#2- Faça o mesmo exercicio anterior, mas com valores inteiros randomicos.
#- import random


################## Lista, Tupla, Set, Dicionário
#- Acesso por indice:
#- Alterável:
#- Permite duplicados:
#- Ordenado:

# -X
x = ['maçã', 'banana', 'uva']

# -Y
y = ('maçã', 'banana', 'uva')


# -W
w = {'maçã', 'banana', 'uva'}

# -Z
z = {'nome':'Joao', 'idade':'30', 'cidade':'SP'}


