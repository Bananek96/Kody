#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    
    a = int(input("Podaj Pierwszą Liczbę: "))
    b = int(input("Podaj Drugą Liczbę: "))
    c = int(input("Podaj Trzecią Liczbę: "))
    x = 0
    
    print(a, b, c)
    
    if a > b and a > c:
        x = a
    elif b > a and b > c:
        x = b
    elif c > a and c > b:
        x = c
    
    print("Największa Liczba to: ", x)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
