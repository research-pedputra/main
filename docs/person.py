# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 20:58:12 2023

@author: pedputra
"""

class Person:
    def __init__ (self):
        self.A = 'Jokowi dodo'
        self.__B = 'Ganjar Pranowo'
    def PrintName (self):
        print(self.A)
        print(self.__B)

P = Person()
print(P.PrintName())