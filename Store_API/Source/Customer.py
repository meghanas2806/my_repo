# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:39:58 2022

@author: megha
"""
import sys

sys.path.append(".")

from Store import Store

s = Store("Apple",20)

s.get_data()

s.put_data(15)

s.get_data()