#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rysunek.py
#  
# DANE WEJSCIOWE: boki a i b
# DANE WYJSCIOWE: rysunek prostokata rysowany gwiazdkami o wymiarach jakie podal uzytkownik

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak: ")
 
    for i in range(a):
        for j in range (b):
            print(znak)
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
