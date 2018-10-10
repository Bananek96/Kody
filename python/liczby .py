#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby.py

def liczby2(a=10, b=99):
    
    """
    Drukuje wszystkie liczby 2-cyfrowe o niepowtarzających się
    cyfrach i ich ilość
    """
    for i in range(a, b):
        if (i % 11) != 0:
            print(i)
        print()
			          
        
    
def liczby3(a=100, b=999):
    
    """
    Drukuje wszystkie liczby 3-cyfrowe o niepowtarzających się
    cyfrach i ich ilość
    """
    for j in range(a, b):
        if (j % 11) != 0:
            print(j)
        print()

def main(args):
    
    print(liczby2())
    print(liczby3())
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
