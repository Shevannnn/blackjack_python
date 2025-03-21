class Card:
    def __init__(self, suit: str, face_value: str):
        self.suit = suit
        self.face_value = face_value
        self.value = self.get_card_value()

    def get_card_value(self):
        if self.face_value in ['J', 'Q', 'K']:
            return 10
        elif self.face_value == 'A':
            return 1  # Ace handled separately in game logic
        return int(self.face_value)

    def __str__(self):
        suit_names = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C': 'Clubs'}
        face_names = {'A': 'Ace', 'J': 'Jack', 'Q': 'Queen', 'K': 'King'}
        return f"{face_names.get(self.face_value, self.face_value)} of {suit_names.get(self.suit, 'Unknown')}"
