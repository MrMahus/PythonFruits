class Stock:
    #Attribs

    fruitsReferences = []
    stock = {}

    def __init__(self, fruitsList, fruitsAmount):

        if type(fruitsList) != list:
            print("Error ! Type List not entered ! ")
        else:
            self.fruitsReferences = fruitsList

        if type(fruitsAmount) != list:
            print("Error ! Type List not entered ! ")
        else:
            self.stock = dict(zip(self.fruitsReferences,fruitsAmount))


    def getStock(self):
        return self.stock

    def setStock(self,pNewStock):
        self.stock = pNewStock

    def checkOutOfStock(self,pStock):

        noNull = 0

        for key in pStock.values():

            if key != 0:
                noNull += 1

        if noNull == 0:
            return True
        else:
            return False

