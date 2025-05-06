"""
Contains the model class and card class.
"""

import random

class Model:
    """
    Contains all of the data needed to run the game (content of deck, player and dealer's hands,
    bet, bankroll, etc.)
    """

    def __init__(self):
        """
        Defines the attributes necessary for gameplay.
        """
        self.player_hand = []
        self.split_1 = []
        self.split_2 = []
        self.split_3 = []
        self.dealer_hand = []
        self.player_bet = 0
        self.player_bankroll = 500

    def __repr__(self):
        """
        Prints relevant information, like contents of hands.
        """
        return (
            f"Player Hand: {self.player_hand}\nDealer Hand:"
            f" {self.dealer_hand}\nPlayer's Bet: {self.player_bet}\nPlayer's"
            f" Bankroll: {self.player_bankroll}"
        )

    def set_bet(self, bet):
        """
        Intializes the bet of the player.
        Args:
            bet (int): bet that player wants to use
        Returns:
            None
        """
        self.player_bet = bet

    def subtract_from_bank(self, bet):
        """
        Take money away from bankroll after bet has been set.
        Args:
            bet (int): bet that will be taken away from bankroll
        Returns:
            None
        """
        self.player_bankroll -= bet

    def add_to_bank(self, bet):
        """
        Adds money to bankroll after winnings are made.
        Args:
            bet (int): amount of money to add to bankroll
        Returns:
            None
        """
        self.player_bankroll += bet

    def deal_player(self, deck, num):
        """
        Deals one card to the player.
        Args:
            deck: list transformed from an instance of Cards class that contains
            card values (but not points)
            num: placement in deck that card will be pulled from (i.e deck[0] pulls
            first card in deck)
        Returns:
            None
        """
        self.player_hand.append(deck[num])

    def deal_dealer(self, deck, num):
        """
        Similar to deal_player; deals one card to the dealer.
        Args:
            deck: list transformed from an instance of Cards class that contains
            card values (but not points)
            num: placement in deck that card will be pulled from (i.e deck[0] pulls
            first card in deck)
        Returns:
            None
        """
        self.dealer_hand.append(deck[num])

    def check_score(self, deck, hand):
        """
        Evaluates the score of a given hand, returning two values in case one
        of the cards is an ace.
        Args:
            deck: instance of Cards class that contains a dict of card values and points
            hand: attribute in model class that is a list of card types only (no points) that the
            player has in hand
        Returns:
            total (int): total point value of cards in hand
            other_total (int): returns alternative total if the card is an ace
        """
        total = 0
        other_total = 0
        for card in hand:
            val = deck[card]
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

        Returns:
            the better of the two scores as an integer
        """
        if isinstance(scores, int):
            return scores
        if scores[0] == scores[1]:
            return scores[0]
        if scores[1] > 21:
            return scores[0]
        return scores[1]

    def checks(self, player_hand, dealer_hand, deck):
        """
        Checks to see if the player has the option to split, double down, or
        take insurance.

        When the two player cards are the same, the player can split.
        When the two player cards are between 9 and 11 inclusive, the player
        can double down.
        When the dealer's visible card is an Ace, the player can take insurance.

        Args:
        player_hand: A dictionary containing two strings, each of which is
        a card as represented in the keys of the deck dictionary of the Cards
        class.
        Example: ['Kh', '8s']. This represents the player's hand.

        Dealer_hand: A dictionary containing two strings, each of which is
        a card as represented in the keys of the deck dictionary of the Cards
        class.
        Example: ['Ad', '6h']. This represents the dealer's hand.

        Deck: deck is the deck dictionary of the Cards class. The keys of the
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
                deck[player_hand[0]] + deck[player_hand[1]]
            ) in double_down_vals:
                double_down = True
        if player_hand[0][0] == player_hand[1][0]:
            split = True
        if dealer_hand[0][0] == "A":
            needs_insurance = True

        return (double_down, split, needs_insurance)


class Cards:
    """
    Contains a dictionary with every card and its blackjack value.
    """

    def __init__(self):
        """
        Sets up deck of cards.
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
        """
        Sets up a string that displays all the card values.
        Args:
            None
        Returns:
            string (str): card name and point value
        """
        string = ""
        for key, value in self._available_deck.items():
            string += key + ", "
        string = string[0 : len(string) - 2]
        return string

    def shuffle(self):
        """
        Shuffles the deck.
        Returns: (dict) the newly shuffled deck
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
