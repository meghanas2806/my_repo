# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:57:25 2022

@author: Meghana Suresh
"""

import json
import sys
sys.path.append("../Database")


class Store:
    def __init__(
            self, product):
        self.product = product
        #self.initial_amount = initial_amount
    
    def get_data(
            self):
        fileObject = open("products.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        print("Product chosen is: ",aList[self.product])
        print("Amount: ",aList[self.initial_amount])
    
    def put_data(
            self, final_state):
        self.initial_amount = final_state
        
