class Table:

    #Attribs
    header = " _____________________________________________\n|      Name      |  Amount  | Client Purchases|\n|----------------|----------|-----------------|"
    cell =   "                                              \n|                |          |                 |\n|----------------|----------|-----------------|"

    cellsList = []


    def formatTable(self,pStock,pBought):

        #Reset Table
        self.cellsList = []

        #Get what was bought and how many
        referenceBought = pBought[0]
        amountBought = pBought[1]

        #Determine how many cells are required by counting number of differents items in stock
        cellsCounter = len(pStock)

        #Split stock into two list to print them separately
        fruitsList = []
        amountList = []

        for key, value in pStock.items():
            fruitsList.append(key)
            amountList.append(value)


        # Add the header of table
        self.cellsList.append(self.header)

        cursor = 0
        while cursor < cellsCounter:




            #Create a buffer cell which will be edited
            currentCell = list(self.cell)

            #Split fruits name and amount to insert them into a string
            currentFruit = list(fruitsList[cursor])
            currentValue = list(str(amountList[cursor]))

            #Insert name into the string
            i = 0
            for char in currentFruit:
                currentCell[51+i] = char
                i += 1

            #Insert amount into the string
            j = 0
            for val in currentValue:
                currentCell[68+j] = val
                j += 1


            #Add the edited cell with name and amount to a list to draw all of them later
            processedCell = "".join(currentCell)
            self.cellsList.append(processedCell)

            #Increments cursor
            cursor += 1


        #Insert the purchases
        k = 0
        index = 0
        while index == 0:
            if fruitsList[k] == referenceBought:
                index = k + 1
            k += 1

        editLine = list(self.cellsList[index])
        splitRef = list(str((amountBought)))

        l = 0
        for element in splitRef:
            editLine[81] = '-'
            editLine[82+l] = element
            l += 1

        processedLine = "".join(editLine)
        self.cellsList[index] = processedLine



    def drawTable(self):

        for lines in self.cellsList:
            print(lines)

