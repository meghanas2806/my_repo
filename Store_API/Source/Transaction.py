# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:39:58 2022

@author: megha
"""

import sys
sys.path.append(".")
from Store import Store


#if __name__ == "__main__":
print("Products Available\n")

store_obj = Store(1)
  
store_obj.get_products()


var1 = input("Enter the Product name: ")


#Display data 
store_obj.get_data(var1)

var2 = int(input("Enter the amount to purchase: "))

store_obj.put_data(var2)
 
#store_obj.get_data(var1)

store_obj.get_purchase_data()
