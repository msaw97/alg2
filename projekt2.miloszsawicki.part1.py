#POLITECHNIKA GDANSKA WFTIMS
#MATEMATYKA SEMESTR IV
#ALGORYTMY I STRUKTURY DANYCH
#LABORATORIUM 2: ALGORYMY SORTUJACE
#MILOSZ SAWICKI
#21.03.2019
#part1:


import random
import time
import sys
sys.setrecursionlimit(5000)

licznik_q = 0

def generator(n):   #generator liczb losowych od 1-100000 z wstawieniem ich do listy
    lista=[]
    i=0
    while i < n:
        element = random.randint(1, 100000)
        lista.append(element)
        i=i+1
    return lista

def zapis(pliktxt, dane, zmienna):
    plik=open(pliktxt, zmienna)
    plik.writelines(str(dane))

def zapis_l(pliktxt, dane, zmienna):
    plik=open(pliktxt, zmienna)
    plik.writelines(str(dane))

def QuickSort(lista): #funkcja pomocnicza wprowadzajaca dalej liste wejsciowa i zwracajaca wynik
   quick_sort(lista, 0 , len(lista)-1)
   return lista

def quick_sort(lista, pierwszy, ostatni):
    if pierwszy<ostatni:    #
        pivot = partition(lista,pierwszy,ostatni)

        quick_sort(lista,pierwszy,pivot-1) #wywolania rekurencyje dla podzielonej listy wzgledem pivot
        quick_sort(lista,pivot+1,ostatni)

def partition(lista, pierwszy, ostatni): #wybiera element rozdzielajacy - pivot
    global licznik_q    #zmienna globalna liczy zlicza przestawienia
    pivot = lista[pierwszy]     #poczatkowo ustalam pivot na pierwszy element listy
    lewa = pierwszy + 1
    prawa = ostatni

    done = False
    while not done:

        while lewa <= prawa and lista[lewa] <= pivot: #sortuje na elementy wieksze badz rowne pivot
            lewa = lewa + 1

        while lewa <= prawa and lista[prawa] >= pivot: #sortuje na elementy mniejsze badz rowne pivot
            prawa = prawa - 1

        if prawa < lewa:
            done = True
            licznik_q = licznik_q +1
        else:
            pom = lista[lewa]
            lista[lewa] = lista[prawa]
            lista[prawa] = pom
            licznik_q = licznik_q +1

    pom = lista[pierwszy]
    lista[pierwszy] = lista[prawa]
    lista[prawa] = pom
    return prawa



rozmiar=[10000,25000,50000, 75000, 100000, 150000]
qoperacje= []
qczas = []
listy = []


for n in rozmiar:
    lista=generator(n)
    listy.append(lista)
    licznik_q=0
    start,end = 0,0
    zapis('in.%d.txt' %(n),lista,'w+')
    start=time.time()
    qlista=QuickSort(lista)
    end = time.time()
    qczas.append(end-start)
    zapis('out.%d.txt' %(n),qlista ,'w+')
    qoperacje.append(licznik_q)


zapis_l('czas.q.txt', qczas,'w+')
zapis_l('operacje.q.txt', qoperacje, 'w+')

print('\nCzas wykonania algorytmu quicksort: ', qczas)
print('\nIlosc wykonaych operacji dla quicksort: ',qoperacje)
print('\nZe wzgledu na limit ilosci rekursji w pythonie bylem zmuszony rozdzielic program na dwa skrypty.')
print('Listy wejsciowa, posortowana juz wyjsciowa oraz dane o zliczonym czasie i operacjach zapisane zostaly zapisane do plików i zostana odtworzone w drugim skrypcie wraz z pozostalymi algorytmami.')
print('Prosze o odtworzenie drugiego skryptu: projekt2.miloszsawicki.part2.py')
