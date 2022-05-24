# -*- coding: utf-8 -*-
"""
Created on Tue May 24 00:14:57 2022

@author: megha
"""

import json




"""
fileObject = open("products.json", "r+")
#jsonContent = fileObject.read()
aList = json.load(fileObject)
aList["Apple"].update({"amount":15})
fileObject.seek(0)
json.dump(aList,fileObject)
fileObject.close()

"""


filename = "products.json"

with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["Apple"].update({"amount":15})
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

