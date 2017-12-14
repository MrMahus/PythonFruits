


class Table:

    # Attribs

    first_col_length = 16
    second_col_length = 18
    third_col_length = 17

    header = " _____________________________________________________\n" \
             "|      Name      |  Current Amount  | Client Purchases|\n" \
             "|----------------|------------------|-----------------|"
    cells_list = []

    # Function to set the table

    def setTable(self, p_order, p_stock):

        # Init the final list of table with the header

        self.cells_list = [self.header]

        # Loop to write all lines

        stock_length = len(p_stock)
        cursor = 0

        while cursor < stock_length:

            if list(p_stock.keys())[cursor] == p_order[0]:

                cell = '|' \
                    + '{0}'.format(list(p_stock.keys())[cursor]).center(self.first_col_length,
                        ' ') + '|' \
                    + '{0}'.format(list(p_stock.values())[cursor]).center(self.second_col_length,
                        ' ') + '|' \
                    + '-{0}'.format(p_order[1]).center(self.third_col_length,
                        ' ') \
                    + '|\n|----------------|------------------|-----------------|'
            else:
                cell = '|' \
                    + '{0}'.format(list(p_stock.keys())[cursor]).center(self.first_col_length,
                        ' ') + '|' \
                    + '{0}'.format(list(p_stock.values())[cursor]).center(self.second_col_length,
                        ' ') + '|' + ''.center(self.third_col_length,
                        ' ') \
                    + '|\n|----------------|------------------|-----------------|'

            self.cells_list.append(cell)
            cursor += 1

    def drawTable(self):

        for lines in self.cells_list:
            print (lines)
