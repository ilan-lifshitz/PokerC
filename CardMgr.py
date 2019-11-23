import random

NUM_OF_CARDS = 52


class CardMgr:
    def __init__(self):
        self.cards = [0] * NUM_OF_CARDS
        self.selectedCards = []

    def get_cards(self, num_of_cards):

        list = []
        for i in range(num_of_cards):
            r = None
            while r in self.selectedCards or r is None:
                r = random.randint(0, NUM_OF_CARDS - 1)
            list.append(r)
            self.selectedCards.append(r)
        list = [x%13 + 2 for x in list]
        return list

    def print(self):
        print("number of cards is: ", NUM_OF_CARDS)
        for i in self.cards:
            print(i)


card_mgr = CardMgr()
print(card_mgr.get_cards(5))

