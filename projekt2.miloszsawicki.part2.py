
#POLITECHNIKA GDANSKA WFTIMS
#MATEMATYKA SEMESTR IV
#ALGORYTMY I STRUKTURY DANYCH
#LABORATORIUM 2: ALGORYMY SORTUJACE
#MILOSZ SAWICKI
#21.03.2019
#part2:

import random
import time
import numpy as np
import matplotlib.pyplot as plt
import ast


licznik_s = 0
licznik_m = 0

def odczyt(pliktxt):
    f = open(pliktxt, 'r')
    return f.read()

def str_lista(dane):    #zamienia str na liste
    dane=ast.literal_eval(dane)
    return dane



def ShellSort(lista):
    shell_sort(lista)
    return lista

def insertion_sort(lista, start, step):
    global licznik_s
    for index in range(start+step, len(lista), step):

     obecna_wartosc = lista[index]
     pozycja = index

     while pozycja >= step and lista[pozycja - step] > obecna_wartosc:
         lista[pozycja] = lista[pozycja - step]
         pozycja = pozycja - step
         licznik_s = licznik_s + 1
     lista[pozycja] = obecna_wartosc


def shell_sort(lista):
    ilosc_podlist = len(lista) //2      #uzyskuje ilosc podlist
    while ilosc_podlist > 0:

        for startpoz in range(ilosc_podlist):
            insertion_sort(lista, startpoz, ilosc_podlist)

        ilosc_podlist = ilosc_podlist //2   #co iteracje zmiejszana ilosc podlist od posortowania ins sort


def MergeSort(lista):
    merge_sort(lista)
    return lista


def merge_sort(lista):
    global licznik_m
    if len(lista)>1:
        dlugosc_listy = len(lista)      #dzielenie listy na pol
        srodek = dlugosc_listy //2
        lewa = lista[:srodek]
        prawa = lista[srodek:]

        merge_sort(lewa)
        merge_sort(prawa)

        i=0 #pierwszy index listy lewej
        j=0 #pierwszy index listy prawej
        k=0

        while i < len(lewa) and j < len(prawa):
            if lewa[i] < prawa[j]:
                lista[k]=lewa[i]
                i=i+1
                licznik_m =licznik_m +1
            else:
                lista[k]=prawa[j]
                j=j+1
                licznik_m =licznik_m +1
            k=k+1


        while i < len(lewa):
                lista[k]=lewa[i]
                i=i+1
                k=k+1
                licznik_m =licznik_m +1

        while j < len(prawa):
            lista[k]=prawa[j]
            j=j+1
            k=k+1
            licznik_m =licznik_m +1




def wykres(typ, moperacje, qoperacje, soperacje, rozmiar):

    n_grup = 6

    fig, ax = plt.subplots()
    index = np.arange(n_grup)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, soperacje, bar_width,
    alpha=opacity,
    color='c',
    label='ShellSort')

    rects2 = plt.bar(index + bar_width, moperacje, bar_width,
    alpha=opacity,
    color='b',
    label='MergeSort')

    rects3 = plt.bar(index + bar_width, qoperacje, bar_width,
    alpha=opacity,
    color='k',
    label='QuickSort')

    plt.xlabel('Dlugosc listy wejsciowej')
    plt.ylabel(typ)
    plt.title(typ)
    plt.xticks(index + bar_width, rozmiar)
    plt.legend()

    plt.tight_layout()
    plt.show()




rozmiar=[10000,25000,50000, 75000, 100000, 150000]
soperacje, moperacje=[],[]
sczas, mczas= [],[]
listy = []
qczas = str_lista(odczyt('czas.q.txt')) #pobieram dane o quicksort z poprzedniego skryptu i zamieniam na liste
qoperacje = str_lista(odczyt('operacje.q.txt'))

for n in rozmiar:
    lista = odczyt('in.%d.txt' %(n)) #zczytuje poczatkowe listy z pierwszego skryptu
    lista=str_lista(lista)  #zamieniam str na listy
    listy.append(lista) #dodaje do zbioru nieposortowanych list


for i in listy:
    start,end = 0,0
    licznik_s=0
    start=time.time()
    slista=ShellSort(i)
    end=time.time()
    sczas.append(end-start)
    soperacje.append(licznik_s)

for i in listy:
    start,end = 0,0
    licznik_m=0
    start=time.time()
    mlista=MergeSort(i)
    end=time.time()
    mczas.append(end-start)
    moperacje.append(licznik_m)



print("Liczba operacji dla shellsort dla listy o dlugosci odpowienio 10000, 25000, 50000, 75000, 100000, 150000:")
print('operacje shellsort: ',soperacje)
print('operacje mergesort: ',moperacje)
print('operacje quicksort: ',qoperacje)
print('czas wykonania shellsort: ' ,sczas)
print('czas wykonania mergesort: ' ,mczas)
print('czas wykonania quicksort: ' ,qczas)

wykres('Ilosc operacji',moperacje, qoperacje, soperacje, rozmiar)
wykres('Czas wykonywania algorytmu',sczas, mczas, qczas, rozmiar)
