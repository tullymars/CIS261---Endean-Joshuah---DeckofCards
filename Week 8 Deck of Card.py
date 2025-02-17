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
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, number_of_cards):
        dealt_cards = []
        for _ in range(number_of_cards):
            if len(self.deck) == 0:
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
    print("\nHere are your cards:")
    print("Good luck!")
    for card in dealt_cards:
        print(card)

    print(f"\nThere are {deck.count()} cards left in the deck.")
    input("Press any key to continue . . .")

if __name__ == "__main__":
    main()
