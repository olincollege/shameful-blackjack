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

    def ask_split(self):
        """
        Asks the user if they want to split.

        Returns True or false depending on the user input (true if they want to split, false
        if they don't).
        Raises a key error if the user doesn't input correctly.
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
            return self.ask_split()

    def ask_insurance(self):
        """
        Asks the user if they want insurance.

        Returns bool depending on the user input (true if they want insurance, false
        if they don't).
        Raises a key error if the user doesn't input correctly.
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
            return self.ask_insurance()

    def ask_after_checks(self, checks):
        """
        Asks the player if they'd like to split, double down, or take insurance,
        depending on the value of a tuple input into it.

        checks: A tuple in the format (bool, bool, bool). The value of bool is
        True or False. The values of the bools represent whether or not the
        player's and dealer's cards qualify to double down, split, or take
        insurance, respectively.

        returns: A tuple in the same format as the input boolean, with True
        representing a player electing to take the option provided to them for
        each case, and False representing the player not being able to or
        choosing to not use their option.

        Example: (True, False, True) - this represents the player choosing to
        double down and take insurance.
        """
        double_down = False
        split = False
        insurance = False
        if checks[0]:
            double_down = self.ask_double_down()
        if checks[1]:
            split = self.ask_split()
        if checks[2]:
            insurance = self.ask_insurance

        return (double_down, split, insurance)
