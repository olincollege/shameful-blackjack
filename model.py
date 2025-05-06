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
        self.player_bet = 0
        self.player_bankroll = 500

    def set_bet(self, bet):
        self.player_bet = bet

    def subtract_from_bank(self, bet):
        self.player_bankroll -= bet

    def add_to_bank(self, bet):
        self.player_bankroll += bet

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
        """
        Evaluates the score of a given hand, returning two values in case one
        of the cards is an ace
        """
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
        """
        Chooses the better of two scores for the purposes of blackjack.

        Args:
            scores: the two scores to be chosen between, in a list

        returns:
            the better of the two scores as an integer
        """
        if isinstance(scores, int):
            return scores
        if scores[0] == scores[1]:
            return scores[0]
        if scores[1] > 21:
            return scores[0]
        return scores[1]

    def dealer_deal(self, deck_list, deck, num, dealer_hand):
        """
        Plays the game from the dealers side.

        Args:
        deck_list: The shuffled deck
        deck: The whole deck dictionary
        num: the number of cards deep into the deck the hand is
        dealer_hand: the first two cards in the dealers hand.

        Returns: an integer representing the dealers final score, equivalent to
        the sum of the values of the cards in the dealer's hand.
        """
        print(f"My Cards: {dealer_hand}")
        while (
            self.check_score(deck, dealer_hand)[0] <= 16
            and self.check_score(deck, dealer_hand)[1] <= 16
        ):
            dealer_hand.append(deck_list[num])
            num += 1
            print(dealer_hand)
            if self.check_score(deck, dealer_hand)[0] == 21:
                print("21!")
                return 21
            if self.check_score(deck, dealer_hand)[1] == 21:
                print("21!")
                return 21
            if self.check_score(deck, dealer_hand)[1] >= 17:
                return self.check_score(deck, dealer_hand)[1]
            if self.check_score(deck, dealer_hand)[0] >= 21:
                return self.check_score(deck, dealer_hand)[0]

    def checks(self, player_hand, dealer_hand, deck):
        """
        Checks to see if the player has the option to split, double down, or
        take insurance.

        When the two player cards are the same, the player can split.
        When the two player cards are between 9 and 11 inclusive, the player
        can double down.
        When the dealer's visible card is an Ace, the player can take insurance.

        args:
        player_hand: A dictionary containing two strings, each of which is
        a card as represented in the keys of the deck dictionary of the Cards
        class.
        Example: ['Kh', '8s']. This represents the player's hand.

        dealer_hand: A dictionary containing two strings, each of which is
        a card as represented in the keys of the deck dictionary of the Cards
        class.
        Example: ['Ad', '6h']. This represents the dealer's hand.

        deck: deck is the deck dictionary of the Cards class. The keys of the
        dictionary are strings with the first character being the card, and
        the second character being the suit. The values are the integer values
        of the cards as determined by the rules of blackjack.
        Example of one key value pair: "2c": 2
        In this dictionary, aces must have the value (1, 11) instead of a single
        integer.

        Returns:
        A tuple containing three booleans which represent the value of each of
        the three checks, with the indices of the tuple representing as such:
        (double down, split, insurance)

        Example:
        (True, False, True) - This return would indicate that the two cards
        used as input could be doubled down but not split, and the dealer has an
        ace.
        """
        double_down_vals = [9, 10, 11]
        aces = ["Ah", "As", "Ad", "Ac"]
        double_down = False
        split = False
        needs_insurance = False
        if player_hand[0] not in aces and player_hand[1] not in aces:
            if (
                sum(deck[player_hand[0]], deck[player_hand[1]])
                in double_down_vals
            ):
                double_down = True
        if player_hand[0][0] == player_hand[1][0]:
            split = True
        if dealer_hand[0][0] == "A":
            needs_insurance = True

        return (double_down, split, needs_insurance)

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
