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
        if(self.status==0):
            fileObject = open("products.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            self.initial_amount = int(aList[self.product]["amount"])
            print('/'+self.product+'/'+str(aList[self.product]["amount"]))
            fileObject.close()
       
    
    def put_data(
            self, buy_amount):
        self.buy_amount = buy_amount
        with open("products.json",'r+') as fileObject:
                # First we load existing data into a dict.
                aList = json.load(fileObject)
                self.final_state = self.initial_amount - self.buy_amount
                if (self.final_state>9):
                    aList[self.product].update({"amount":str(self.final_state)})
                else:
                    aList[self.product].update({"amount":str(0)+str(self.final_state)})
                # Sets file's current position at offset.
                fileObject.seek(0)
                # convert back to json.
                json.dump(aList, fileObject,indent =4,sort_keys=True)
                
    def get_products(
            self):
        if(self.status==1):
            fileObject = open("products.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            for i in aList["Products"]:
                if (int(aList[i]["amount"])>0):
                    print('/'+i+'/'+str(aList[i]["amount"]))
            fileObject.close()
    
    def get_purchase_data(
            self):
        if(self.status==0):
            if (self.final_state >= 0):                    
                print('/'+self.product+'/'+str(self.initial_amount)+'/'
                      +str(self.buy_amount)+'/'+str(self.final_state))
            