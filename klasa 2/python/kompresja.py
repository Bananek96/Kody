#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wspolczynnik(Vk, Vnk):
    Rc = float(Vk) / float(Vnk) * 100
    R2c = (1 - float(Vk) / float(Vnk)) * 100
    
    print('O ile zmniejszyły się dane: ', Rc)
    print('Ile miejsca zaoszczędziliśmy: ', R2c)

def main(args):
    for i in range(2):
        Vk = input('Podaj rozmiar danych skompresowanych (Bajty): ')
        Vnk = input('Podaj rozmiar danych nieskompresowanych (Bajty): ')
        wspolczynnik(Vk, Vnk)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
