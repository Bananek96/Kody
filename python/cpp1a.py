#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cpp1a.py
#

def main(args):
    
	a = 0
	b = 0
    
	while a < 75:
		a = int(input("Podaj  liczbę:"))
        b = b + a
	print("Za duza liczba", b)
      
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
