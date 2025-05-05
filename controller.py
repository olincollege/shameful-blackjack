"""
Contains the Controller class and Dealer class
"""


class Controller:
    """
    Contains all prompts needed for the game.
    """

    def __init__(self):
        """
        docstring here - set up hand
        """

    def ask_bet(self):
        try:
            action = input(
                "How much would you like to bet? Enter a number between 1 and"
                " your current bankroll.\n"
            )
            if action.isnumeric():
                return int(action)
            else:
                raise KeyError
        except KeyError:
            print("Please enter an integer.")
            self.ask_bet()

    def ask_hit_or_stay(self):
        """
        Asks the user if they want to hit or stay.

        Returns True or false depending on the user input, and raises a key
        error if the user doesn't input correctly.
        """
        try:
            action = input("Would you like to hit or stay?\n(h/s) ")
            if action == "h" or action == "H":
                return True
            elif action == "s" or action == "S":
                return False
            raise KeyError
        except KeyError:
            print("Please enter h for hit or s for stay.")
            self.ask_hit_or_stay()

    def ask_double_down(self):
        """
        Asks the user if they want to double down.

        Returns True or false depending on the user input, and raises a key
        error if the user doesn't input correctly.
        """
        try:
            action = input("Would you like to double down?\n(y/n) ")
            if action == "y" or action == "Y":
                return True
            if action == "N" or action == "n":
                return False
            raise KeyError
        except KeyError:
            print("Please enter y for yes or n for no.")
            self.ask_double_down()

    def ask_split(self):
        """
        Asks the user if they want to split.

        Returns True or false depending on the user input, and raises a key
        error if the user doesn't input correctly.
        """
        try:
            action = input("Would you like to split?\n(y/n) ")
            if action == "y" or action == "Y":
                return True
            if action == "N" or action == "n":
                return False
            raise KeyError
        except KeyError:
            print("Please enter y for yes or n for no.")
            self.ask_split()

    def ask_insurance(self):
        """
        Asks the user if they want insurance.

        Returns True or false depending on the user input, and raises a key
        error if the user doesn't input correctly.
        """
        try:
            action = input("I have an ace! Would you like insurance?\n(y/n)")
            if action == "y" or action == "Y":
                return True
            if action == "N" or action == "n":
                return False
            raise KeyError
        except KeyError:
            print("Please enter y for yes or n for no.")
            self.ask_insurance()


class Dealer:
    """
    Does all the dealer stuff
    """
