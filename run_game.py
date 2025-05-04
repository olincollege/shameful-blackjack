"""
runs da game
"""

from model import Cards, Model
from controller import Controller, Dealer
from view import View


def main():
    """
    runs the blackjack game from start to finish.
    """
    model = Model()
    view = View()
    controller = Controller()
    print("Welcome to my table... Are you feeling lucky?")
    print("I'll show you the deck, so you can see there's been no tampering.")
    deck = Cards()
    print(deck)
    print("Now, I'll shuffle the cards, and show you those too.")
    deck.shuffle()
    print(deck)
    print("Ready to play? I'll shuffle the cards one final time.")
    deck.shuffle()
    list_deck = list(deck.available_deck.keys())
    # card = list_deck[0]
    # print(view.print_card(deck, card))
    num_cards = 0
    model.deal_player(list_deck, num_cards)
    # print(model.player_hand)
    num_cards += 1
    model.deal_player(list_deck, num_cards)
    num_cards += 1
    # print(model.player_hand)
    print("Your cards are: ", view.show_cards(deck, model.player_hand))
    print(
        "Your current score is",
        model.un_double_score(model.check_score(deck, model.player_hand)),
    )
    while (
        controller.ask_hit_or_stay()
        and model.check_score(deck, model.player_hand)[0] < 21
        and model.check_score(deck, model.player_hand)[1] < 21
    ):
        print("You hit, so you will be dealt another card")
        model.deal_player(list_deck, num_cards)
        num_cards += 1
        # print(model.player_hand)
        print("Your cards are:", view.show_cards(deck, model.player_hand))
        print(
            "Your current score is",
            model.un_double_score(model.check_score(deck, model.player_hand)),
        )
    print(
        "Your current score is",
        model.un_double_score(model.check_score(deck, model.player_hand)),
    )
    print("Now, it's my turn.")


if __name__ == "__main__":
    main()


class OneHand:
    """
    Runs an individual hand of blackjack from start to finish
    """

    def deal_setup(self):
        """
        Deals two cards to the dealer and two cards to the player
        """
        #       model.deal
        #       view.display_cards
        #       model.check_for_ace
        #       self.checks(card1, card2)
        #       if control.ask_hit_or_stay:
        #                  model.add_a_card()
        #
        pass

    def checks(self, cards_in_hand, dealer_cards):
        """
        runs every checker function from the controller
        """


#       if cards_in_hand(0) == cards_in_hand(1):
#           control.ask_double.down
#       if sum(cards_in_hand) > 8 and if sum(cards_in_hand) < 12:
#           control.ask_double_down
#       if val(showing_dealer_card) = (1, 11)
#           control.ask_insurance()
