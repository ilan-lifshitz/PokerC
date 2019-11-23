
class User:
    global_var = 777
    def __init__(self, name):
        self.name = name
        self.num_of_cards = 5

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_num_of_cards(self):
        return self.num_of_cards

    def set_num_of_cards(self, num_of_cards):
        self.name = num_of_cards

    def print(self):
        print("name: ", self.name)
        print("num of cards: ", self.num_of_cards)


#user = User("ilan")
#user.print()