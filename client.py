from random import randint
class Client:


    def askStock(self,pStock):


        #Ignore items with 0 amount
        for key in list(pStock):
            if pStock[key] == 0:
                del pStock[key]

        stockLength = len(pStock)

        #Choose a random reference
        randomNumber = randint(0, stockLength -1)
        referencesNames = []

        for keys in pStock.keys():
            referencesNames.append(keys)

        randomReference = referencesNames[randomNumber]

        #Choose random amount
        randomAmount = randint(1,pStock[randomReference])

        order = (randomReference,randomAmount)

        return order