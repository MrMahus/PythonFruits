from stock import *
from client import *
from table import *
from inputHandler import *

import sys
import time

# Variables
fruitsList = []
fruitsAmount = []
stockFilled = False
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')
currentMonth = 0
yearsPassed = 0

# Generate Input Handler
input = Input()

# Generate the table
table = Table()

# Generate the Client
client = Client()

# Ask the user to set the stock
numbersOfReferences = input.inputInteger("How many differents types of fruits would you stock ?")
stockDefined = input.defineStock(numbersOfReferences)

# Save the stock in database
ourStock = Stock(stockDefined)
stockFilled = True

# Check if the stock is not empty
if ourStock.checkOutOfStock(ourStock.getStock()) == True:
    sys.exit("Out of Stock")

# 'Erase'
# print('\n'*80)


# Main loop
while (stockFilled == True):

    # 'Erase'
    # print('\n' * 80)

    # Print the current month
    print("-" + months[currentMonth] + "-")

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
        stockFilled = False

    # Increments the month and check if it reach December
    currentMonth += 1

    if currentMonth == 12:
        currentMonth = 0
        yearsPassed += 1

    time.sleep(1)

# End of Loop

print("\n \n You sell items during {0} years".format(yearsPassed))
