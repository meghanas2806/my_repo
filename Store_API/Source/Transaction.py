# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:39:58 2022

@author: Meghana Suresh
"""

from Store import Store
import sys
import getopt
sys.path.append(".")


if __name__ == "__main__":

    argList = sys.argv[1:]
    options = "sb:"
    long_options = ["shopstatus", "buy"]

    try:
        arg, val = getopt.getopt(argList, options, long_options)
        for curr_arg, curr_val in arg:
            if  curr_arg in ("-s", "--shopstatus"):
                print("Status of the Shop\n")
                store_obj = Store(1) #To get status of the shop
                store_obj.get_products()
            elif curr_arg in ("-b", "--buy"):
                if (len(sys.argv[2]) > 0 and len(sys.argv[3]) > 0
                        and int(sys.argv[3]) > 0):
                    store_obj = Store(0) #To get status of the product
                    var1 = sys.argv[2]  # Product name
                    print("\nCurrent Product Status\n")
                    store_obj.get_data(var1)
                    #Display data
                    print("\nPurchase data\n")
                    var2 = int(sys.argv[3])  # buy amount
                    if (var2 <= store_obj.initial_amount):
                        store_obj.put_data(var2)
                        store_obj.get_purchase_data()
                    else:
                        print(f"Enter amount lesser than or equal to {store_obj.initial_amount}")
                else:
                    sys.argv[2] = 'Fruit'
                    sys.argv[3] = 0
                    print("Enter valid arguments!!")

    except Exception as err:
        print(str(err))
