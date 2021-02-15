#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:48:42 2021

@author: peter
"""

from contextlib import contextmanager

@contextmanager
def just_a_function():
    print('Context manager created')
    yield
    print('Context manager destroyed')
    
with just_a_function():
    print('Run operations')