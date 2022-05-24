# API for buying and checking the status of products

## Implement an API for checking the status in the shop

1.The command to print the status of the shop can be given as below.

$python3 Transaction.py -s

or 

$python3 Transaction.py --shopstatus

#### Output

Status of the Shop

/Apple/50 <br/>
/Banana/40 <br/>
/Kiwi/30 <br/>
/Mango/55 <br/>
/Orange/65 <br/>




## Implement an API for buying a product

$python3 Transaction.py -b <product_name> <buy_amount>

or

$python3 Transaction.py --buy <product_name> <buy_amount>

Example:

$python3 Transaction.py -b Orange 40


#### Output
Current Product Status

/Orange/65

Purchase data

/Orange/65/40/25





