#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:19:56 2021

@author: peter
"""

def friendly_decorator(func):
    def wrapper(self, lie):
        lie *= 2
        func(self, lie)
    return wrapper


class Lucy:
    def __init__(self, age):
        self.age = age
    
    @friendly_decorator
    def sayYourAge(self, lie):
        print(f'I am {self.age - lie}!')

lucy = Lucy(32)
lucy.sayYourAge(2)