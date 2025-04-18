"""
Contains the View class
"""


class View:
    """
    Has all of the view thingys
    """

    def __init__(self):
        """
        you say blah blah blah blah!
        """

    def ask_hit_or_stay(self):
        """
        I do not say blah blah blah blah!
        """
        try:
            action = input("Would you like to hit or stay?\n(h/s)")
            if action == "h" or action == "H":
                return True
            elif action == "s" or action == "S":
                return False
            raise KeyError
        except KeyError:
            print("what the shit my guy")
            self.ask_hit_or_stay()

    def show_cards(self):
        """
        I'm on an airplane! I love you! It is me, adam sandler!
        """
        # for card in hand:
        #     print(card)
