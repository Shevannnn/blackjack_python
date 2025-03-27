class Card:
    def __init__(self, suit: str, card_value: str):
        self.suit = suit
        self.card_value = card_value
        self.value = self.get_card_value()

    def get_card_value(self):
        if self.card_value in ['J', 'Q', 'K']:
            return 10
        elif self.card_value == 'A':
            return 1
        return int(self.card_value)

    def __str__(self):
        suit_names = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C': 'Clubs'}
        face_names = {'A': 'Ace', 'J': 'Jack', 'Q': 'Queen', 'K': 'King'}
        return f"{face_names.get(self.card_value, self.card_value)} of {suit_names.get(self.suit, 'idk')}"
