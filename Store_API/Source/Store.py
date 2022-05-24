# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:57:25 2022

@author: Meghana Suresh
"""

import json


class Store:
    def __init__(
            self, status):
        self.status = status
       
    
    def get_data(
            self,product):
        self.product = product
        if(self.status==1):
            fileObject = open("products.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            print("Product chosen is: ",self.product)
            self.initial_amount = aList[self.product]["amount"]
            print("Amount: ",self.initial_amount )
            fileObject.close()
       
    
    def put_data(
            self, final_state):
        self.final_state = final_state
        with open("products.json",'r+') as fileObject:
                  # First we load existing data into a dict.
                aList = json.load(fileObject)
                # Join new_data with file_data inside emp_details
                aList[self.product].update({"amount":self.final_state})
                # Sets file's current position at offset.
                fileObject.seek(0)
                # convert back to json.
                json.dump(aList, fileObject,indent = 4)
                
    def get_products(
            self):
        if(self.status==1):
            fileObject = open("products.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            for i in aList["Products"]:
                print(i)
            fileObject.close()
        
