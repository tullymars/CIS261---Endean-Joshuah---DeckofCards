import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "Jack", "Queen", "King"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, number_of_cards):
        dealt_cards = []
        for _ in range(number_of_cards):
            if not self.deck:
                break
            dealt_cards.append(self.deck.pop())
        return dealt_cards

    def count(self):
        return len(self.deck)

def main():
    print("Card Dealer")
    deck = Deck()
    deck.shuffle()
    print(f"I have shuffled a deck of {deck.count()} cards.")

    try:
        num_cards = int(input("How many cards would you like?: "))
    except ValueError:
        num_cards = 0

    dealt_cards = deck.deal(num_cards)
    
    if dealt_cards:
        print("\nGood luck! Here are your cards:")
        for card in dealt_cards:
            print(card)
    else:
        print("No cards were dealt.")

    print(f"\nThere are {deck.count()} cards left in the deck.")
    input("Press any key to continue . . .")

if __name__ == "__main__":
    main()
