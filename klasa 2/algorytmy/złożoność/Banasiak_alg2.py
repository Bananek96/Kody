#!/usr/bin/env python
# -*- coding: utf-8 -*-

def funkcja():
    a = 0
    while a < 1 or a > 99:
        a = int(input("Podaj a: "))
    
    return a

def funkcja2(a, i):
    if a == i:
        print("{} jest liczbą parzystą".format(a))
    elif a != i:
        i = i + 2
        if i > a:
            print("{} nie jest liczbą parzystą".format(a))
        else:
            funkcja2(a, i)
        

def main(args):
    a = funkcja()
    i = 2
    funkcja2(a, i)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
