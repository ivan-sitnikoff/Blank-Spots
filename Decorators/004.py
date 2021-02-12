#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:54:54 2021

@author: peter
"""

import time
from functools import wraps

def decorator_maker(decorator_arg):
    def decorator(func):
        print(f'До старта {decorator_arg + 1} секунд')
        @wraps(func)
        def wrapper(*args, **kwargs):
            #print('I now about', decorator_arg, func_arg1, func_arg2)
            for i in range(decorator_arg, 0, -1):
                print(i)
                time.sleep(1)
            func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_maker(9)
def vostok(arg1, arg2):
    print(f'{arg1}: {arg2}')

vostok('Юрий Гагарин', 'Поехали!')
