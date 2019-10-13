import random

NUM_OF_CARDS = 52


class cardMgr:
    def __init__(self, color, size):
        self.cards = [0] * NUM_OF_CARDS
        self.selectedCards = []
        self.color = color
        self.size = size

    def getCards(self, numOfCards):

        list = []
        for i in range(numOfCards):
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


cardmgr = cardMgr('Orange', 7)
print(cardmgr.getCards(5))
print(cardmgr.getCards(5))
print(cardmgr.getCards(5))
print(cardmgr.getCards(5))
