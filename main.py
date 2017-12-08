from stock import *
from client import *
from table import *

import sys
import time




#Variables
fruitsList = []
fruitsAmount = []
stockFilled = False
months = ('January','February','March','April','May','June','July','August','September','October','November','December')
currentMonth = 0
yearsPassed = 0



#Ask the user to set the stock
typesFruitsCount = ''

while type(typesFruitsCount) != int:
    try:
        typesFruitsCount = int(input("How many differents types of fruits would you stock ? \n \n"))
    except:
        print("Character not allowed, enter a number")



while typesFruitsCount > 0:

    key = str(input("Enter the fruit's name : \n"))

    value = ''
    while type(value) != int:

        try:
            value = int(input("Amount : \n"))
        except:
            print("Character not allowed, enter a number \n")

    fruitsList.append(key)
    fruitsAmount.append(value)
    typesFruitsCount -= 1



#Generate the stock in database
ourStock = Stock(fruitsList,fruitsAmount)
stockFilled = True


#Check if the stock is not empty
if ourStock.checkOutOfStock(ourStock.getStock()) == True:
    sys.exit("Out of Stock")


#Generate the Client
client = Client(ourStock)

#'Erase'
print('\n'*80)


#Main loop
while(stockFilled == True):

    #Client Buy in our stock
    print("\n{0} - Client bought : \n".format(months[currentMonth]))
    client.bought(ourStock.getStock())

    #Get what was bought and how many
    purchases = [client.getReferecebought(),client.getAmountbought()]

    #Actualize our stock
    ourStock.setStock(client.getBufferStock())

    #Draw the table
    table = Table()
    table.formatTable(ourStock.getStock(),purchases)
    table.drawTable()


    #Check if the stock is not empty
    if ourStock.checkOutOfStock(ourStock.getStock()) == True:
        stockFilled = False


    currentMonth +=1

    if currentMonth == 12:
        currentMonth = 0
        yearsPassed +=1

    #stockFilled = False  #Allows to have only one time loop
    #input("Press enter to continue..")
    time.sleep(2)
    # 'Erase'
    print('\n' * 80)


print("\n \n You sell items during {0} years".format(yearsPassed))