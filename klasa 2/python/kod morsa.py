#!/usr/bin/env python
# -*- coding: utf-8 -*-

kod = {'A': '.-',  'B': '-...', 'C': '-.-.', 
     'D': '-..', 'E': '.',  'F': '..-.', 
     'G': '--.', 'H': '....', 'I': '..', 
     'J': '.---', 'K': '-.-', 'L': '.-..', 
     'M': '--',  'N': '-.',  'O': '---', 
     'P': '.--.', 'Q': '--.-', 'R': '.-.', 
     'S': '...', 'T': '-',  'U': '..-', 
     'V': '...-', 'W': '.--', 'X': '-..-', 
     'Y': '-.--', 'Z': '--..',

     'a': '.-',  'b': '-...', 'c': '-.-.', 
     'd': '-..', 'e': '.',  'f': '..-.', 
     'g': '--.', 'h': '....', 'i': '..', 
     'j': '.---', 'k': '-.-', 'l': '.-..', 
     'm': '--',  'n': '-.',  'o': '---', 
     'p': '.--.', 'q': '--.-', 'r': '.-.', 
     's': '...', 't': '-',  'u': '..-', 
     'v': '...-', 'w': '.--', 'x': '-..-', 
     'y': '-.--', 'z': '--..', 

     '0': '-----', '1': '.----', '2': '..---', 
     '3': '...--', '4': '....-', '5': '.....', 
     '6': '-....', '7': '--...', '8': '---..', 
     '9': '----.', ' ': ' ', '': ''
     } 

def koduj():
    tekst=input('Podaj tekst: ')
    # ~ print("".join({kod[i] for i in tekst]))
    for i in tekst:
        print(kod[i])
        
def dekoduj():
    tekst = []
    litera = ' '
    while litera > '':
        litera = input('Podaj kod Morsa; ')
        tekst.append(litera)
    print(kod[tekst.index()])

def main(args):
    # ~ koduj()
    dekoduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
