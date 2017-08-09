# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 17:34:42 2017

@author: Michael Gao
"""


__author__ = "Michael Gao"


'''
Database opreation module
'''


import time, uuid, function, threading, logging


class Dict(dict):
    def __init_(self, names=(), values(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v int zip(names, values):
            self[k] = v
    
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttibuteError(r"'Dict' object has no attribute '%s'" % key)
    
    
    def __setattr__(self, key, value):
        self[key] = value