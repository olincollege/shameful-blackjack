"""
Contains the model class and card class.
"""


class Model:
    """
    Contains all of the data needed to run the game
    """

    pass


class Cards:
    """
    contains a dictionary with every card and its blackjack value.
    """

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
