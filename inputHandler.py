class Input:

    def inputInteger(self,pString):

        intWritten = ''
        while type(intWritten) != int:
            try:
                intWritten = int(input(pString+"\n"))
            except:
                print("Character not allowed, enter a number")

        return intWritten

    def defineStock(self,pNumberOfRefences):

        stock = {}

        while pNumberOfRefences > 0:

            key = str(input("Enter the fruit's name : \n"))

            value = self.inputInteger("Enter the amount :")

            stock.update({key:value})

            pNumberOfRefences -= 1

        return stock