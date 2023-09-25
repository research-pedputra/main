# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Item:
    pay_rate = 0.8
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
    def discount(self):
        self.price = self.price * Item.pay_rate
        

item1 = Item("Iphone", 100, 5)
item1.discount()
item2 = Item("Samsung", 200, 5)

print(f'Total price of {item1.name} is {item1.price}' )
