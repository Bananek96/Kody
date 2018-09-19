#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
#  


def main(args):
    
    a = int(input("Podaj a: "))
        
    b = int(input("Podaj b: "))
   
    while a >= b:
        b = int(input("Ty ancymonie, WIĘKSZA!!!!! Podaj b:"))
               
        for i in range(a, b+1):
        #    if i % 2 == 0:
                if not i % 2:
                    print(i)
                                
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
