'''Echipa: 22-E7
Studenti: UNGUREANU G. CRISTIAN-IOAN, VLSANOVIĆ JOVAN
Tema proiect: D6-T1 | Procesarea unui set de date.
Resurse: https://medium.com/@antoniolui/a-practical-guide-to-pandas-data-etl-with-code-examples-bb2c27bdb572
https://stackoverflow.com/questions/12142174/run-a-python-script-with-arguments'''

import pandas as pd
import sys

# verificam sa existe un argument
if len(sys.argv) != 3:
  sys.exit("Not enough args")

# luam primul fisier dat ca parametru
inputFile = sys.argv[1]
# luam al doilea fisier dat ca parametru
outputFile = sys.argv[2]
# citim fisierul csv dat ca prim argument terminal avand ca delimitator ";" si sarind peste liniile rau formatate de asemenea prima linie pe care o consideram cap de tabel si denumim coloanele dupa cum se cere
data = pd.read_csv(inputFile, on_bad_lines='skip', delimiter=";", skiprows=[0], names=["An", "Luna", " Commodity code", "Commodity", "Value USD", "Quantity KG"])

# data = pd.read_csv("./comexstat_world_sample_22-E7.csv",on_bad_lines='skip',delimiter=";",skiprows=[0],names=["An", "Luna", " Commodity code","Commodity","Value USD","Quantity KG"])
print(data.head())

# concatenam coloana An cu coloana Luna pentru a forma coloana Data
data["Data"] = data["An"].astype(str)+'-'+data["Luna"].astype(str)
print(data.head())

# stergem coloanele An si Luna ca nu ne mai trebuie
data.drop(columns=["An", "Luna"], inplace=True)

# rearanjam coloanele in ordinea dorita
data = data[['Data', ' Commodity code', 'Commodity', 'Quantity KG', 'Value USD']]
print(data.head())

# creeam coloana Quantity T luand valoarea corespunzatoare din coloana Quantity KG pe care o impartim la 1000
data["Quantity T"] = data["Quantity KG"]/1000
print(data.head())

#creeam coloana Value EUR luand valoarea corespunzatoare din coloana Value USD pe care o inmultim cu 0,92
data["Value EUR"] = data["Value USD"]*0.92
print(data.head())

#rearanjam coloanele in ordinea dorita
data = data[['Data', ' Commodity code', 'Commodity', 'Quantity KG', 'Quantity T', 'Value USD', 'Value EUR']]
print(data.head())

#creem un fisier nou cu datele obtinute si numele fiind dat de al doilea parametru
data.to_csv(outputFile)

print(pd.__version__)

