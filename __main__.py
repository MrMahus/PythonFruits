

from stock import Stock
from client import Client
from table import Table


import sys
import time

# Variables

fruit_list = []
fruit_amount = []
stock_filled = False
months = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
    )
current_month = 0
years_passed = 0

# Function to handle int input

def inputInteger(p_string):
    int_written = ''
    while type(int_written) != int:
        try:
            int_written = int(input(p_string + '\n'))
        except ValueError:
            print('Character not allowed, enter a number')

    return int_written

# Function to put stock into dict

def defineStock(p_number_of_references):
    stock = {}

    while p_number_of_references > 0:
        key = str(input("Enter the fruit's name : \n"))

        value = inputInteger('Enter the amount :')

        stock.update({key: value})

        p_number_of_references -= 1

    return stock

# Generate the table

table = Table()

# Generate the Client

client = Client()

# Ask the user to set the stock

number_of_references = inputInteger("How many differents types of fruits would you stock ?")
stock_defined = defineStock(number_of_references)

# Save the stock in database

ourStock = Stock(stock_defined)
stock_filled = True

# Check if the stock is not empty

if ourStock.checkOutOfStock(ourStock.getStock()) == True:
    sys.exit('Out of Stock')

# 'Erase'
# print('\n'*80)

# Main loop

while stock_filled == True:

    # 'Erase'
    # print('\n' * 80)

    # Print the current month

    print ('-' + months[current_month] + '-')

    # Client get the stock and ask an order

    order = client.askStock(ourStock.getStock())

    # Send the order to the stock

    if ourStock.checkOrder(order) == True:

        # Order can be proceeded

        ourStock.proceedOrder(order)
    else:

        # Order can't be proceeded

        pass

    # Draw the table

    table.setTable(order, ourStock.getStock())
    table.drawTable()

    # Check if the stock is not empty

    if ourStock.checkOutOfStock(ourStock.getStock()) == True:
        stock_filled = False

    # Increments the month and check if it reach December

    current_month += 1

    if current_month == 12:
        current_month = 0
        years_passed += 1

    time.sleep(1)

# End of Loop

print ('You sell items during {0} years'.format(years_passed))
