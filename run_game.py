"""
runs da game
"""

from model import Cards


def main():
    """
    runs the blackjack game from start to finish.
    """
    print("Welcome to my table... Are you feeling lucky?")
    print("I'll show you the deck, so you can see there's been no tampering.")
    deck = Cards()
    print(deck)
    print("Now, I'll shuffle the cards, and show you those too.")
    deck.shuffle()
    print(deck)
    print("Ready to play?")
    deck.shuffle()
    list_deck = list(deck.available_deck.keys())
    card = list_deck[0]
    print(deck.print_card(card))


if __name__ == "__main__":
    main()
