


class Stock:
    # Attribs

    stock = {}

    def __init__(self, p_stock):

        if type(p_stock) != dict:
            print ('Error ! Type Dictionary not entered ! ')
        else:
            self.stock = p_stock

    # Check an order received

    def checkOrder(self, p_order):

        reference_check = False
        amount_check = False

        # Check if the reference asked is in the stock

        for ref in self.stock.keys():
            if ref == p_order[0]:
                reference_check = True

        # Check if the amount asked is correct and can be substracted from the stock

        if self.stock[p_order[0]] >= p_order[1]:
            amount_check = True
        else:
            pass

        if reference_check == True and amount_check == True:
            return True
        else:
            return False

    # Proceed an order checked

    def proceedOrder(self, p_order):

        self.stock[p_order[0]] -= p_order[1]

    # Getter

    def getStock(self):
        return self.stock

    # Function to check the OutOfStock state

    def checkOutOfStock(self, p_stock):

        no_null = 0

        for value in p_stock.values():

            if value != 0:
                no_null += 1
                break

        if no_null == 0:
            return True
        else:
            return False