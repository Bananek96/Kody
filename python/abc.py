#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#  


def main(args):
    
    a = int(input("Podaj liczbe a: "))
    print(a)
    
    b = int(input("Podaj liczbe b: "))
    print(b)
    
    c = int(input("Podaj liczbe c: "))
    print(c)
    
    if a > b and a > c:
        print(a, "jest najwieksza")
    elif a < b and b > c:
        print(b, "jest najwieksza")
    elif a < c and b < c:
        print(c, "jest najwieksza")
    elif a == b == c:
        print(a, "jest najwieksza")
    else:
        if a == b and a < c:
            print(c, "jest najwieksze")
        if c == b and c < a:
            print(a, "jest najwieksze")
        if a == c and a < b:
            print(b, "jest najwieksze")
        if a == b and a > c:
            print(a, "jest najwieksze")
        if c == b and c > a:
            print(c, "jest najwieksze")
        if a == c and a > b:
            print(a, "jest najwieksze")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
