"""
Contains the View class
"""

from model import Cards

class View:
    """
    Contains every method used to display the cards in a deck or hand, as well
    as bet sizes, bankroll, and winnings after a game.

    Attributes:
    _SUITS (dict): defines what each suit stands for
    """

    _SUITS = {"s": "spades", "c": "clubs", "h": "hearts", "d": "diamonds"}

    def __init__(self):
        """
        Initializes an instance of the view class.
        """

    def print_card(self, deck, card):
        """
        Represents a card as a statement of suit, number and point value
        Args:
            deck: an instance of the Cards class, which contains a dict of all the cards and their point
            values
            card: a string matching one of the keys in the self._deck: Valuesuit format
        Returns: a string saying Value of Suit for the card
        """
        label = card[0]
        suit = self._SUITS[card[len(card) - 1]]
        val = deck[card]
        if label == "A":
            label = "Ace"
        if label == "K":
            label = "King"
        if label == "Q":
            label = "Queen"
        if label == "J":
            label = "Jack"
        if label == "1":
            label = "10"
        if val == (1, 11):
            val = "either 1 or 11"
        return label + " of " + suit + " with a value of " + str(val)

    def show_cards(self, deck, hand):
        """
        Args:
            deck: an instance of the Cards class, which contains a dict of all the cards and their point
            values
            hand: a list of strings representing the cards in the player's hand

        Returns a string representing every card in the hand
        """
        final_str = ""
        for card in hand:
            final_str += self.print_card(deck, card) + ", "
        return final_str[0 : len(final_str) - 2]

    def show_bet(self, bet):
        """
        Args:
            bet (int): * note that it can technically be anything, but before it will reach the input it will have
            to be an int; represents the bet the user has placed
            
        Returns a string saying how much the player has bet this time
        """
        return f"You have bet ${bet}."

    def show_bankroll(self, bankroll):
        """
        Args:
            bankroll (int): * note that it can technically be anything, but before it will reach the input it will have
            to be an int; represents the bankroll, or the amount of money a user has left
        Returns a string saying how much money the player has left
        """
        return f"You have ${bankroll} in the bank."

    def show_winnings(self, winnings):
        """
        Args:
            winnings (int): * note that it can technically be anything, but before it will reach the input it will have
            to be an int; represents the amount of money the player has won after a game
        Returns a string saying how much the player has won this time
        """
        return f"You just won ${winnings}."
