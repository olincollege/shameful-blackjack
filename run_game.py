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
    # print("I'll show you the deck, so you can see there's been no tampering.")
    deck = Cards()
    # print(deck)
    # print("Now, I'll shuffle the cards, and show you those too.")
    # deck.shuffle()
    # print(deck)
    # print("Ready to play? I'll shuffle the cards one final time.")
    deck.shuffle()
    list_deck = list(deck.available_deck.keys())
    # card = list_deck[0]
    # print(view.print_card(deck, card))
    print(view.show_bankroll(model.player_bankroll))
    bet = controller.ask_bet()
    model.set_bet(bet)
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
    if model.check_score(deck, model.player_hand)[0] == 21:
        print("Blackjack!")
        model.add_to_bank(bet * 3 / 2)
    if model.check_score(deck, model.player_hand)[1] == 21:
        print("Blackjack!")
        model.add_to_bank(bet * 3 / 2)
    else:
        while controller.ask_hit_or_stay():
            print("You hit, so you will be dealt another card")
            model.deal_player(list_deck, num_cards)
            num_cards += 1
            # print(model.player_hand)
            print("Your cards are:", view.show_cards(deck, model.player_hand))
            print(
                "Your current score is",
                model.un_double_score(
                    model.check_score(deck, model.player_hand)
                ),
            )
            if model.check_score(deck, model.player_hand)[0] == 21:
                print("21!")
                break
            if model.check_score(deck, model.player_hand)[1] == 21:
                print("21!")
                break
            if model.check_score(deck, model.player_hand)[0] >= 21:
                print("Bust...")
                break
    print("Now, it's my turn.")
    dealer_score = model.un_double_score(
        model.dealer_deal(list_deck, deck, num_cards)
    )
    # print("dealer score is", dealer_score)
    player_score = model.un_double_score(
        model.check_score(deck, model.player_hand)
    )
    # print("ur score is", player_score)
    if (
        dealer_score < 21
        and player_score < 21
        and 21 - dealer_score > 21 - player_score
    ):
        model.add_to_bank(bet)
    if 21 >= dealer_score and dealer_score > player_score:
        model.subtract_from_bank(bet)
    if dealer_score > 21 and 21 >= player_score:
        model.add_to_bank(bet)
    print("The dealer's final score is", dealer_score)
    print(view.show_bankroll(model.player_bankroll))


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
