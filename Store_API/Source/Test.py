# -*- coding: utf-8 -*-
"""
Created on Tue May 24 00:14:57 2022

@author: megha
"""

import json




fileObject = open("products.json", "r")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)


