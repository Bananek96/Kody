#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main(args):
    
    lista =[]
    for i in range(1):
        lista.append(random.sample(range(0, 31), 5))
    print("Lista 5 losowych i unikalnych liczb: ", lista)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
