# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:39:58 2022

@author: megha
"""

import sys
sys.path.append(".")
from Store import Store

"""
class Transaction:
    def __init__(
            self,status,purchase):
        self.status = status
        self.purchase = purchase
"""   
    
        
        
        
    s = Store("Apple")
    
    s.get_data()
    
    s.put_data(15)
    
    s.get_data()