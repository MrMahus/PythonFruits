


class Table:

    # Attribs

    first_col_length = 16
    second_col_length = 18
    third_col_length = 17

    header = \
        ''' _____________________________________________________
|      Name      |  Current Amount  | Client Purchases|
|----------------|------------------|-----------------|'''
    cellsList = []

    # Function to set the table

    def setTable(self, pOrder, pStock):

        # Init the final list of table with the header

        self.cellsList = [self.header]

        # Loop to write all lines

        stockLength = len(pStock)
        cursor = 0

        while cursor < stockLength:

            if list(pStock.keys())[cursor] == pOrder[0]:

                cell = '|' \
                    + '{0}'.format(list(pStock.keys())[cursor]).center(self.first_col_length,
                        ' ') + '|' \
                    + '{0}'.format(list(pStock.values())[cursor]).center(self.second_col_length,
                        ' ') + '|' \
                    + '-{0}'.format(pOrder[1]).center(self.third_col_length,
                        ' ') \
                    + '|\n|----------------|------------------|-----------------|'
            else:
                cell = '|' \
                    + '{0}'.format(list(pStock.keys())[cursor]).center(self.first_col_length,
                        ' ') + '|' \
                    + '{0}'.format(list(pStock.values())[cursor]).center(self.second_col_length,
                        ' ') + '|' + ''.center(self.third_col_length,
                        ' ') \
                    + '|\n|----------------|------------------|-----------------|'

            self.cellsList.append(cell)
            cursor += 1

    def drawTable(self):

        for lines in self.cellsList:
            print lines



			
