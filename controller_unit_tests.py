from controller import Controller

def main():
    """
    Tests various methods in the Controller class

    Note that since the controller mostly deals with user input,
    we will be simulating user input in the terminal for our test.
    (i.e will try a valid response, then a non valid response)
    """

    # define a test instance of View
    test_controller = Controller()

    # TEST ASK_BEST
    print("TESTING ASK_BET")
    ask_bet_answer = test_controller.ask_bet()
    print(f"ask_bet answer: {ask_bet_answer}")
    # will ask to resubmit if number is negative or not an integer
    # once you input a correct value, it will return the value inputted
    # i would just like to say, there were a number of small, surprising long
    # issues to fix (i.e would return none if an incorrect answer was inputted first,
    # couldn't compare a str and int since the input was initially a str)
    # fixed the latter issue for all other functions
    print("------ END TEST ------")

    # since the structure of these functions is similar, I will only
    # test a subset of them
    # TEST ASK_HIT_OR_STAY
    print("TESTING ASK_HIT_OR_STAY")
    hit_stay_answer = test_controller.ask_hit_or_stay()
    print(f"ask_bet answer: {hit_stay_answer}")
    # only accepts h or s as inputs, otherwise asks for next input
    print("------ END TEST ------")

    # TEST ASK_INSURANCE
    print("TESTING ASK_INSURANCE")
    ask_insurance_answer = test_controller.ask_insurance()
    print(f"ask_bet answer: {ask_insurance_answer}")
    print("------ END TEST ------")

    # TEST ASK_AFTER_CHECKS
    print("TESTING ASK_AFTER_CHECKS")
    # checks if there's a case for splitting, insurance, or doubling down
    # asks, then adjusts bool depending on answer
    test_tuple = (False, True, False)
    ask_after_checks_answer = test_controller.ask_after_checks(test_tuple)
    print(f"ask_bet answer: {ask_after_checks_answer}")
    print("------ END TEST ------")


if __name__ == "__main__":
    main()
