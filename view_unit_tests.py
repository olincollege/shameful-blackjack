from view import View
from model import Cards, Model


def main():
    """
    Tests various methods in the View class
    """

    # define a test instance of View
    test_view = View()
    # define a test instance of a card deck Cards
    test_deck = Cards()
    # define a test instance of the deck as a list (no point values)
    test_list_deck = list(test_deck.available_deck.keys())
    # define a test model
    test_model = Model()

    # TEST PRINT_CARD
    # test the message for every card in the deck to see if the correct
    # value and type
    # this is for basic functionality, to make sure the function
    # behaves properly in-game
    print("TESTING PRINT_CARD")
    for value in test_list_deck:
        print(value)
        print(test_view.print_card(test_deck, value))
    print("------ END TEST ------")

    # TEST SHOW_CARDS
    # test basic functionality
    print("TESTING SHOW_CARDS")
    print(test_view.show_cards(test_deck, test_model.player_hand))
    # should return nothing because there's nothing in the player's
    # hand
    # then, add something to player's hand
    test_model.player_hand = ["5d"]
    print(test_view.show_cards(test_deck, test_model.player_hand))
    print("------ END TEST ------")

    # TEST SHOW_BET
    # test basic functionality
    # *THIS IS ONLY FOR DISPLAYING. CHECKING CORRECT VALUES IS IN
    # THE CONTROLLER
    print("TESTING SHOW_BET")
    print(test_view.show_bet("5"))
    print("------ END TEST ------")

    # TEST SHOW_BANKROLL
    # test basic functionality
    # *THIS IS ONLY FOR DISPLAYING. CHECKING CORRECT VALUES IS IN
    # THE CONTROLLER
    print("TESTING SHOW_BANKROLL")
    print(test_view.show_bankroll("2"))
    print("------ END TEST ------")

    # TEST SHOW_WINNINGS
    # test basic functionality
    # *THIS IS ONLY FOR DISPLAYING. CHECKING CORRECT VALUES IS IN
    # THE CONTROLLER
    print("TESTING SHOW_WINNINGS")
    print(test_view.show_winnings("3"))
    print("------ END TEST ------")


if __name__ == "__main__":
    main()
