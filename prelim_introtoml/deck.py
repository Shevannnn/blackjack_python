import random
from card import Card

class Deck:
    def __init__(self):
        suits = ['D', 'H', 'S', 'C']
        faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, face) for suit in suits for face in faces]
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None
