"""
Contains the Controller class, which takes input from the user
"""


class Controller:
    """
    Contains all prompts needed for the game.
    """

    def __init__(self):
        """
        Intializes any attributes (none in this case) for the class.
        """

    def ask_bet(self):
        """
        Asks the user for how much they would like to bet. Prevents incorrect input (strings, negative numbers).
        Args:
            None
        Returns:
            action (int): the amount of money they want to bet
        """
        try:
            action = input(
                "How much would you like to bet? Enter a number between 1 and"
                " your current bankroll.\n"
            )
            if action.isnumeric():
                if int(action) <= 0:
                    raise ValueError
                return int(action)
            else:
                raise KeyError
        except KeyError:
            print("Please enter an integer greater than 0.")
            return self.ask_bet()

    def ask_hit_or_stay(self):
        """
        Asks the user if they want to hit or stay.

        Returns (bool) depending on the user input (true for hit, false for stay)
        Raises a key error if the user doesn't input correctly.
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
            return self.ask_hit_or_stay()

    def ask_double_down(self):
        """
        Asks the user if they want to double down.

        Returns bool depending on the user input (true for double down, false for no double
        down)
        Raises a key error if the user doesn't input correctly.
        """
        try:
            action = input("Would you like to double down?\n(y/n)")
            if action == "y" or action == "Y":
                return True
            if action == "N" or action == "n":
                return False
            raise KeyError
        except KeyError:
            print("Please enter y for yes or n for no.")
            return self.ask_double_down()

    def ask_want_to_continue(self):
        """
        Asks if the player would like to continue to another game.

        Returns:
        True if they want to continue, and False if they do not.
        """
        try:
            prompt = input("Would you like to continue? ")
            if prompt == "y" or prompt == "Y":
                return True
            if prompt == "N" or prompt == "n":
                return False
            raise KeyError
        except KeyError:
            print("Please enter y for yes or n for no.")
            return self.ask_want_to_continue()

    def ask_after_checks(self, checks):
        """
        Asks the player if they'd like to double down
        depending on the value of a boolean input into it.

        checks: boolean The value of bool is
        True or False. The values of the bools represent whether or not the
        player's and dealer's cards qualify to double down

        returns: boolean, with True
        representing a player electing to take the option provided to them for
        each case, and False representing the player not being able to or
        choosing to not use their option.

        Example: True - this represents the player choosing to
        double down
        """
        double_down = False
        if checks:
            double_down = self.ask_double_down()
        return double_down
