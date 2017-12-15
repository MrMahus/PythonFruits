from random import randint


class Client:
    def askStock(self, p_stock):

        # Ignore items with 0 amount

        for key in list(p_stock):
            if p_stock[key] == 0:
                del p_stock[key]

        stock_length = len(p_stock)

        # Choose a random reference

        random_number = randint(0, stock_length - 1)
        references_names = []

        for keys in p_stock.keys():
            references_names.append(keys)

        random_reference = references_names[random_number]

        # Choose random amount

        random_amount = randint(1, p_stock[random_reference])

        order = (random_reference, random_amount)

        return order