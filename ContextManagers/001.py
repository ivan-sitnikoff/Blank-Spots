#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:09:32 2021

@author: peter
"""

class ContextManager:
    def __init__(self):
        print('Context Manager created')
    
    def __enter__(self):
        print('Begin Context Manager')
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('End Context Manager')
        
with ContextManager():
    print('Run operations')
