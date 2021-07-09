import random
from breakingbaccarat.simngen.Card import Card

class CardHelper:

    def new_deck(self):

        deck = [
            # for spade cards
            Card("A", 1, "S"), Card("2", 2, "S"), Card("3", 3, "S"), Card("4", 4, "S"),
            Card("5", 5, "S"), Card("6", 6, "S"), Card("7", 7, "S"), Card("8", 8, "S"),
            Card("9", 9, "S"), Card("10", 0, "S"), Card("J", 0, "S"), Card("Q", 0, "S"),
            Card("K", 0, "S"),

            # for heart cards
            Card("A", 1, "H"), Card("2", 2, "H"), Card("3", 3, "H"), Card("4", 4, "H"),
            Card("5", 5, "H"), Card("6", 6, "H"), Card("7", 7, "H"), Card("8", 8, "H"),
            Card("9", 9, "H"), Card("10", 0, "H"), Card("J", 0, "H"), Card("Q", 0, "H"),
            Card("K", 0, "H"),

            # for diamond cards
            Card("A", 1, "D"), Card("2", 2, "D"), Card("3", 3, "D"), Card("4", 4, "D"),
            Card("5", 5, "D"), Card("6", 6, "D"), Card("7", 7, "D"), Card("8", 8, "D"),
            Card("9", 9, "D"), Card("10", 0, "D"), Card("J", 0, "D"), Card("Q", 0, "D"),
            Card("K", 0, "D"),

            # for club cards
            Card("A", 1, "C"), Card("2", 2, "C"), Card("3", 3, "C"), Card("4", 4, "C"),
            Card("5", 5, "C"), Card("6", 6, "C"), Card("7", 7, "C"), Card("8", 8, "C"),
            Card("9", 9, "C"), Card("10", 0, "C"), Card("J", 0, "C"), Card("Q", 0, "C"),
            Card("K", 0, "C"),
        ]

        return deck

    def get_playbox(self, deck_size=7, shuffles=10):

        deck = []

        '''generate cardbox for play'''
        for i in range(deck_size):
            deck += self.new_deck()

        '''shuffle cardbox before return'''
        for j in range(shuffles):
            random.shuffle(deck)

        return deck
