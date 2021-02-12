#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:08:26 2021

@author: peter
"""

def decorator_passing_arguments(func):
    def wrapper(*args, **kwargs):
        print('See what I\'ve got:', *args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@decorator_passing_arguments
def full_name(first_name, last_name):
    print('My name is', first_name, last_name)
    

full_name('Ivan', 'Sitnikov')