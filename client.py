from random import randint
class Client:

    bufferStock = {}
    referenceBought = ''
    amountBought = 0

    def __init__(self,pStock):
        self.bufferStock = pStock

    def bought(self,pStock):

        #Buffer the stock
        self.bufferStock = pStock

        #get list of the stock
        itemsList = []

        for key in self.bufferStock:
            itemsList.append(key)


        #Loop : Choose a random item to buy with an amount of it. It check if it's possible to buy it and remove things that can't be bought

        canBuy = True

        while canBuy == True:

            randomReference  = randint(0,len(itemsList)-1 )
            referenceToBuy = itemsList[randomReference]

            if self.bufferStock[referenceToBuy] > 0:

                randomAmount = randint(1, self.bufferStock[referenceToBuy])
                print("{1} : {0} ".format(randomAmount, referenceToBuy))
                self.bufferStock[referenceToBuy] -= randomAmount

                #Save what is bought and how many in attribs to send them later to another class
                self.amountBought = randomAmount
                self.referenceBought = referenceToBuy

                canBuy = False
            else:
                del itemsList[randomReference]

            if len(itemsList) == 0:
                canBuy = False


    def getBufferStock(self):
        return self.bufferStock


    def getReferecebought(self):
        return self.referenceBought

    def getAmountbought(self):
        return self.amountBought