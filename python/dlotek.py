#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileLiczb = int(input("Podaj ilość typowanych liczb: "))
    maksLiczba = int(input("Podaj maksymalna losowaną liczbe: "))
    print("wytypuj {} z {} liczb".format(ileLiczb, maksLiczba))

    # komentarz
    liczby = []
    for i in range(ileLiczb):
        liczba = random.randint(1, maksLiczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
        print(liczba)

    #     odp = input("Podaj liczbę od 1 do 10: ")
    #     print(" Podałeś liczbę:", odp)

    #     if liczba == int(odp):
    #         print("Zgadłeś!")
    #         break
    #     else:
    #         print("Jeszcze raz!!!")

    # return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
