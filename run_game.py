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


if __name__ == "__main__":
    main()
