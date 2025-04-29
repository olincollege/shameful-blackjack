"""
runs da game
"""

from model import Cards
from view import View


def main():
    """
    runs the blackjack game from start to finish.
    """
    view = View()
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
    print(view.print_card(deck, card))
    hand = [
        list_deck[0],
        list_deck[1],
        list_deck[2],
    ]  # should become the deal method  at some point
    print(view.show_cards(deck, hand))


if __name__ == "__main__":
    main()
