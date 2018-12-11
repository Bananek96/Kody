#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys


class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        self.szer, self.wys = szer, wys
        pygame.display.set_caption('Pong')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        self.pow.fill((0, 0, 0))
        for obGraf in args:
            self.pow.blit(obGraf.pow, obGraf.prost)
        pygame.display.update()

class PongGra(object):
    """ Kontroler gry """

    def __init__(self, szer, wys):
        pygame.init()
        self.plansza = Plansza(szer, wys)
        self.pal1 = Paletka(szer=100, wys=20, x=350, y=360)
        self.pal2 = Paletka(szer=100, wys=20, x=350, y=20, kolor =(0, 0, 255))
        self.pilka = Pilka(szer=20, wys=20, x=390, y = 190, kolor = (255, 255, 255))

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == MOUSEMOTION:
                    mX, mY = event.pos
                    self.pal1.przesun(mX, self.plansza.szer)

            self.pilka.ruszaj(self.plansza.szer, self.plansza.wys)
            self.plansza.rysuj(
                self.pal1, 
                self.pal2,
                self.pilka
            )

class ObiektGraf():
    def __init__(self, szer, wys, x, y, kolor = (0, 255, 0)):
        self.szer = szer
        self.wys = wys
        self.pow = pygame.Surface([szer, wys], pygame.SRCALPHA).convert_alpha()
        self.prost = self.pow.get_rect(x=x, y=y)

class Paletka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor = (255, 0, 0), maks_v=10):
        super().__init__(szer, wys, x, y, kolor)
        self.pow.fill(kolor)
        self.maks_v = maks_v
        
    def przesun(self, mX, o_szer):
        """
        :param:
        mX ~ składowa X pozycji paletki
        o_szer ~ szerokość okna gry
        """
        przesuniecie = mX - self.maks_v
        if przesuniecie > o_szer - self.szer:
            przesuniecie = o_szer - self.szer
        if przesuniecie< 0:
            przesuniecie = 0
        self.prost.x = przesuniecie

class Pilka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor = (0, 0, 0), px_v=3, py_v=3):
        super().__init__(szer, wys, x, y, kolor)
        pygame.draw.ellipse(self.pow, kolor, [0,0, self.szer, self.wys])
        self.px_v = px_v
        self.py_v = py_v
        self.px_v = px_v
        self.start_x = x 
        self.start_y = y 
        
        def ruszaj(self, o_szer, o_wys, *args):
            self.prost.move.ip(self.pX_v, py_v)
            if self.prost.right >= o_szer or self.prost.left <=0:
                self.px_v *= -1
            if self.prost.top <= 0 or self.prost.bottom >= o_wys:
                self.prost.x = o_szer / 2
                self.prost.y = o_wys / 2
                


if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
