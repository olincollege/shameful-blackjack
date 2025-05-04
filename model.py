"""
Contains the model class and card class.
"""

import random


class Model:
    """
    Contains all of the data needed to run the game
    """

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.player_bet = []
        self.player_bankroll = []

    def deal_player(self, deck, num):
        """
        deals one card to the player
        """
        self.player_hand.append(deck[num])

    def deal_dealer(self, deck, num):
        """
        deals one card to the dealer
        """
        self.dealer_hand.append(deck[num])

    def check_score(self, deck, hand):
        total = 0
        other_total = 0
        for card in hand:
            val = deck.deck[card]
            if val == (1, 11):
                total += val[0]
                other_total += val[1]
            else:
                total += val
                other_total += val
        return total, other_total

    def un_double_score(self, scores):
        if scores[0] == scores[1]:
            return scores[0]
        if scores[1] > 21:
            return scores[0]
        return scores

    def dealer_deal(self, deck_list, deck, num):
        while (
            self.check_score(deck, self.dealer_hand)[0] <= 16
            and self.check_score(deck, self.dealer_hand)[1] <= 16
        ):
            self.dealer_hand.append(deck_list[num])
            num += 1
        print(
            "The dealer's final score is",
            self.un_double_score(self.check_score(deck, self.dealer_hand)),
        )
        return self.un_double_score(self.check_score(deck, self.dealer_hand))

    # @property
    # def player_hand(self):
    #     """
    #     Returns the available deck
    #     """
    #     return self.player_hand

    # @property
    # def dealer_hand(self):
    #     """
    #     Returns the available deck
    #     """
    #     return self.dealer_hand


class Cards:
    """
    contains a dictionary with every card and its blackjack value.
    """

    # _SUITS = {"s": "spades", "c": "clubs", "h": "hearts", "d": "diamonds"}

    def __init__(self):
        """
        Sets up deck of cards
        """
        self._deck = {
            "As": (1, 11),
            "Ac": (1, 11),
            "Ad": (1, 11),
            "Ah": (1, 11),
            "2s": 2,
            "2c": 2,
            "2d": 2,
            "2h": 2,
            "3s": 3,
            "3c": 3,
            "3d": 3,
            "3h": 3,
            "4s": 4,
            "4c": 4,
            "4d": 4,
            "4h": 4,
            "5s": 5,
            "5c": 5,
            "5d": 5,
            "5h": 5,
            "6s": 6,
            "6c": 6,
            "6d": 6,
            "6h": 6,
            "7s": 7,
            "7c": 7,
            "7d": 7,
            "7h": 7,
            "8s": 8,
            "8c": 8,
            "8d": 8,
            "8h": 8,
            "9s": 9,
            "9c": 9,
            "9d": 9,
            "9h": 9,
            "10s": 10,
            "10c": 10,
            "10d": 10,
            "10h": 10,
            "Js": 10,
            "Jc": 10,
            "Jd": 10,
            "Jh": 10,
            "Qs": 10,
            "Qc": 10,
            "Qd": 10,
            "Qh": 10,
            "Ks": 10,
            "Kc": 10,
            "Kd": 10,
            "Kh": 10,
        }
        self._available_deck = self._deck

    def __repr__(self):
        string = ""
        for key, value in self._available_deck.items():
            string += key + ", "
        string = string[0 : len(string) - 2]
        return string

    # def print_card(self, card):
    #     """
    #     Represents a card
    #     card: a string matching one of the keys in the self._deck: Valuesuit format
    #     Returns: a string saying Value of Suit for the card
    #     """
    #     label = card[0]
    #     suit = self._SUITS[card[len(card) - 1]]
    #     val = self._deck[card]
    #     if label == "A":
    #         label = "Ace"
    #     if label == "K":
    #         label = "King"
    #     if label == "Q":
    #         label = "Queen"
    #     if label == "J":
    #         label = "Jack"
    #     if label == "1":
    #         label = "10"
    #     if val == (1, 11):
    #         val = "either 1 or 11"
    #     return label + " of " + suit + " with a value of " + str(val)

    def shuffle(self):
        """
        Shuffles the deck
        Returns: the newly shuffled deck- a dictionary
        """
        dictionary = self._deck
        keys = list(dictionary.keys())
        random.shuffle(keys)
        self._available_deck = {key: dictionary[key] for key in keys}
        return self._available_deck

    @property
    def available_deck(self):
        """
        Returns the available deck
        """
        return self._available_deck

    @property
    def deck(self):
        """
        Returns the available deck
        """
        return self._deck
