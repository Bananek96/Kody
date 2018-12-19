#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def wpisz(lista, n):
    for i in range(n):
        lista.append(random.randint(0, 50))
    print(lista)
    return lista
    
def zamien(lista, i):
    tmp = lista[i]
    lista[i] = lista[i + 1]
    lista[i + 1] = tmp
    
def sort(lista, n):
    print("Sortowanie przez wybór")
    i = 0
    while i < n:
        i += 1
        k = i
        j = i + 1
        while j < n:
            j += 1
            if lista[j] < lista[k]:
                zamien(lista, j)
    
def main(args):
    n = 20
    lista = []
    wpisz(lista, n)
    sort(lista, n)
    
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
