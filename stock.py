class Stock:
    # Attribs
    stock = {}

    def __init__(self, pStock):

        if type(pStock) != dict:
            print("Error ! Type Dictionary not entered ! ")
        else:
            self.stock = pStock

    # Check an order received

    def checkOrder(self, pOrder):

        referenceCheck = False
        amountCheck = False

        # Check if the reference asked is in the stock
        for ref in self.stock.keys():
            if ref == pOrder[0]:
                referenceCheck = True

        # Check if the amount asked is correct and can be substracted from the stock
        if self.stock[pOrder[0]] >= pOrder[1]:
            amountCheck = True
        else:
            pass

        if referenceCheck == True and amountCheck == True:
            return True
        else:
            return False

    # Proceed an order checked
    def proceedOrder(self, pOrder):

        self.stock[pOrder[0]] -= pOrder[1]

    # Getter

    def getStock(self):
        return self.stock

    # Function to check the OutOfStock state

    def checkOutOfStock(self, pStock):

        noNull = 0

        for value in pStock.values():

            if value != 0:
                noNull += 1
                break

        if noNull == 0:
            return True
        else:
            return False
