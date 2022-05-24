# -*- coding: utf-8 -*-
"""
Created on Tue May 24 00:14:57 2022

@author: Meghana Suresh

Unit test
"""
import json


class TestStore:
    def __init__(
            self, status):
        self.status = status
         
        
    def get_data(
            self,product):
        assert self.status == 0,"Wrong flag set to status"
        self.product = product
        if(self.status==0):
            fileObject = open("products_test.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            assert self.product in aList,"Product not available in store"
            self.initial_amount = int(aList[self.product]["amount"])
            assert self.initial_amount > 0,"Quantity should be greater than zero"
            fileObject.close()
            
    def put_data(
            self, buy_amount):
        assert self.status == 0,"Wrong flag set to status"
        self.buy_amount = buy_amount
        with open("products_test.json",'r+') as fileObject:
                # First we load existing data into a dict.
                aList = json.load(fileObject)
                assert self.buy_amount <= self.initial_amount,"Buy amount is greater than initial amount"
                self.final_state = self.initial_amount - self.buy_amount
                aList[self.product].update({"amount":str(self.final_state)})
                # Sets file's current position at offset.
                fileObject.seek(0)
                # convert back to json.
                json.dump(aList, fileObject,indent =4,sort_keys=True)
    
    def get_products(
            self):
        assert self.status == 1,"Wrong flag set to status"
        if(self.status==1):
            fileObject = open("products.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            for i in aList["Products"]:
                if (int(aList[i]["amount"])>0):
                    print('/'+i+'/'+str(aList[i]["amount"]))
            fileObject.close()
    
    
    
if __name__ == '__main__':
    
    store_obj = TestStore(0)#To get product status
    
    store_obj.get_data("Apple")
    
    store_obj.put_data(35)
    
    store_obj = TestStore(1)#To get shop status
    
    store_obj.get_products()
    
    print("Everything is correct!")
