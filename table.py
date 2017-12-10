class Table:

    #Attribs
    header = " _____________________________________________________\n|      Name      |  Current Amount  | Client Purchases|\n|----------------|------------------|-----------------|"
    cellsList = []


    #Function to set the table
    def setTable(self,pOrder,pStock):

        #Init the final list of table with the header
        self.cellsList = [self.header]

        #Loop to write all lines
        stockLength = len(pStock)
        cursor = 0

        while cursor < stockLength:

            if list(pStock.keys())[cursor] == pOrder[0]:

                cell ="                                                      \n|"+"{0}".format(list(pStock.keys())[cursor]).center(16," ")+"|"+"{0}".format(list(pStock.values())[cursor]).center(18," ")+"|"+"-{0}".format(pOrder[1]).center(17," ")+"|\n|----------------|------------------|-----------------|"
            else:
                cell ="                                                      \n|"+"{0}".format(list(pStock.keys())[cursor]).center(16," ")+"|"+"{0}".format(list(pStock.values())[cursor]).center(18," ")+"|"+"".center(17," ")+"|\n|----------------|------------------|-----------------|"

            self.cellsList.append(cell)
            cursor += 1



    def drawTable(self):

        for lines in self.cellsList:
            print(lines)