#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cpp1a.py
#

def main(args):
    
    a = int(input("Podaj a: "))
        
    b = int(input("Podaj b: "))
    
    while a + b <= 75:
            print(a + b)
            a = int(input("Podaj a: "))
            b = int(input("Podaj b: "))
    
            if a + b > 75:
                print(a + b, "Za duża suma")
                 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
