from deck import Deck
import time

def ConsoleClear():
    print("\033c", end="")

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer_hand = [self.deck.draw_card(), self.deck.draw_card()]

    def calculate_hand_value(self, hand):
        value = sum(card.value for card in hand)
        ace_count = sum(1 for card in hand if card.face_value == 'A')

        while ace_count > 0 and value + 10 <= 21:
            value += 10
            ace_count -= 1

        return value

    def display_hands(self, reveal_dealer=False):
        ConsoleClear()
        print("Dealer's Hand:")
        if reveal_dealer:
            print(f"Value: {self.calculate_hand_value(self.dealer_hand)}")
            for card in self.dealer_hand:
                print(card)
        else:
            print(self.dealer_hand[0])
            print("[Face Down Card]")

        print("\nPlayer's Hand:")
        print(f"Value: {self.calculate_hand_value(self.player_hand)}")
        for card in self.player_hand:
            print(card)


    def player_turn(self):
        while self.calculate_hand_value(self.player_hand) < 21:
            move = input("\nEnter H - Hit or S - Stand: ").strip().upper()
            if move == "H":
                new_card = self.deck.draw_card()
                self.player_hand.append(new_card)
                # print(f"\nYou drew: {new_card}")
                self.display_hands()
            elif move == "S":
                break
            else:
                print("Invalid input, try again.")

    def dealer_turn(self):
        print("\nDealer is drawing a card. Please wait...")
        time.sleep(1)

        while self.calculate_hand_value(self.dealer_hand) < 17:
            new_card = self.deck.draw_card()
            self.dealer_hand.append(new_card)
            # print(f"\nDealer draws: {new_card}")
            # time.sleep(1)

    def check_winner(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        print("\nFinal Results:")
        self.display_hands(reveal_dealer=True)

        if player_value > 21:
            print("\nBust! You lose.")
        elif dealer_value > 21:
            print("\nDealer busts! You win!")
        elif player_value > dealer_value:
            print("\nYou win!")
        elif dealer_value > player_value:
            print("\nYou lose.")
        else:
            print("\nIt's a tie!")

    def play(self):
        self.display_hands()
        
        # Player's turn
        self.player_turn()
        
        # If player didn't bust, dealer plays
        if self.calculate_hand_value(self.player_hand) <= 21:
            self.dealer_turn()
        
        # Determine winner
        self.check_winner()

        # Replay
        if input("\nPlay again? (Y/N): ").strip().upper() == "Y":
            ConsoleClear()
            BlackjackGame().play()

if __name__ == "__main__":
    BlackjackGame().play()
