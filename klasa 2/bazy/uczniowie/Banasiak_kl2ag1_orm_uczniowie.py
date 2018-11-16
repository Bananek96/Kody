#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) #instalacja bazy

#### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    
    klasa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
class Uczen(BazaModel):
    
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
        
class Przedmiot(BazaModel):
    
    przedmiot = CharField(null=False)
    imienaucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plecnaucz = BooleanField()
    
class Ocena(BazaModel):
    
    datad = DateTimeField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = DecimalField(null=False)

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Uczen, Klasa, Przedmiot, Ocena])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
