#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:58:57 2021

@author: peter
"""

def stand_alone_function():
    print('I\'m a sland alone function!')
    
    
def new_decorator(func):
    def wrapper():
        print('Code before function')
        func()
        print('Code after function')
        print()
    return wrapper
        
stand_alone_function()

stand_alone_function_decorated = new_decorator(stand_alone_function)

stand_alone_function_decorated()

stand_alone_function = new_decorator(stand_alone_function)

stand_alone_function()
