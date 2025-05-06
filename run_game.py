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
        self.dealer_deal(list_deck, deck, num_cards, model.dealer_hand)
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
    hand = OneHand()
    print(hand.eval_hand(model.dealer_hand, model.player_hand))


class OneHand:
    """
    Runs an individual hand of blackjack from start to finish
    """

    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller()
        self.deck = Cards()
        self.deck.shuffle()
        self.list_deck = list(self.deck.available_deck.keys())
        self.num_cards = 0
        self.is_insurance = False

    def deal_setup(self):
        """
        Deals two cards to the dealer and two cards to the player
        """
        print(f"Bankroll: {self.model.player_bankroll}")
        self.model.set_bet(
            self.controller.ask_bet  # important to not have this be adopted by the child class
        )
        self.model.deal_player(self.list_deck, self.num_cards)
        self.num_cards += 1
        self.model.deal_player(self.list_deck, self.num_cards)
        self.num_cards += 1
        self.model.deal_dealer(self.list_deck, self.num_cards)
        self.num_cards += 1
        self.model.deal_dealer(self.list_deck, self.num_cards)
        self.num_cards += 1
        print(f"Your cards: {self.model.player_hand}")
        print(f"My Card (That you can see): {self.model.dealer_hand[0]}")

    def player_goes(self, hand):
        """
        has the player play through a hand.

        Args:
            hand: The player's first two cards in a list, in the same notation
            as the keys in the Cards dictionary.

        Returns: An integer representing the value of the player's final hand.
        If their hand is blackjack, returns 100.
        """
        checks_post_deal = self.controller.ask_after_checks(
            self.model.checks(
                self.model.player_hand, self.model.dealer_hand, self.deck.deck
            )
        )

        if checks_post_deal[0]:  # Block for if the player doubles down
            self.model.set_bet(2 * self.model.player_bet)
            print("Your bet is doubled and you get one additional card")
            self.model.deal_player(self.list_deck, self.num_cards)
            self.num_cards += 1
            return self.model.check_score(
                self.deck.deck, self.model.player_hand
            )

        if checks_post_deal[2]:  # block for if the player takes insurance
            self.is_insurance = True

        draft_score, other_score = self.model.check_score(self.deck.deck, hand)
        player_score = self.model.un_double_score([draft_score, other_score])
        if player_score == 21:
            return 21
        while self.controller.ask_hit_or_stay:
            self.model.deal_player(self.deck.deck, self.num_cards)
            self.num_cards += 1
            print(
                "Your"
                f" cards:{self.view.show_cards(self.deck.deck, self.model.player_hand)}"
            )
            if (
                self.model.check_score(self.deck.deck, self.model.player_hand)
                == 21
            ):
                return 21
            if (
                self.model.check_score(self.deck.deck, self.model.player_hand)
                > 21
            ):
                return self.model.check_score(
                    self.deck.deck, self.model.player_hand
                )

    def dealer_deal(self, deck_list, deck, num, dealer_hand):
        """
        Plays the game from the dealers side.

        Args:
        deck_list: The shuffled deck
        deck: The whole deck dictionary
        num: the number of cards deep into the deck the hand is
        dealer_hand: the first two cards in the dealers hand.

        Returns: an integer representing the dealers final score, equivalent to
        the sum of the values of the cards in the dealer's hand.
        """
        print(f"My Cards: {dealer_hand}")
        while (
            self.model.check_score(deck, dealer_hand)[0] <= 16
            and self.model.check_score(deck, dealer_hand)[1] <= 16
        ):
            dealer_hand.append(deck_list[num])
            num += 1
            print(dealer_hand)
            if self.model.check_score(deck, dealer_hand)[0] == 21:
                print("21!")
                return 21
            if self.model.check_score(deck, dealer_hand)[1] == 21:
                print("21!")
                return 21
            if (
                self.model.check_score(deck, dealer_hand)[1] >= 17
                and self.model.check_score(deck, dealer_hand)[1] < 21
            ):
                print(
                    f"Staying at {self.model.check_score(deck, dealer_hand)[1]}"
                )
                return self.model.check_score(deck, dealer_hand)[1]
            if self.model.check_score(deck, dealer_hand)[0] > 21:
                print("Bust!")
                return self.model.check_score(deck, dealer_hand)[0]

    def eval_hand(self, dealer_hand, player_hand):
        """
        Takes two lists of strings and figures out who won the hand
        Args:
            dealer_hand: a list of strings representing the cards the dealer has
            player_hand: a list of strings representing the cards the player has
        Returns:
            a tuple with four strings and an integer
            take: a string representing that the dealer won
            push: a string representing a tie
            bj: a string representing a blackjack for either the dealer or player
            win: a string representing the player win
            payout: an integer representing what the original bet should be multiplied by to be added to the bankroll
        """
        take = False
        push = False
        bj = False
        win = False
        payout = 0
        player_bust = player_hand > 21
        dealer_bust = dealer_hand > 21
        if not dealer_bust and not player_bust and player_hand == dealer_hand:
            push = True
        if not dealer_bust and not player_bust and player_hand > dealer_hand:
            win = True
        if not dealer_bust and not player_bust and player_hand < dealer_hand:
            take = True
        if len(player_hand) == 2 and player_hand == 21:
            bj = True
            payout = 3 / 2  # the factor by which to multiply the bet
        if len(dealer_hand) == 2 and dealer_hand == 21:
            bj = True
            payout = -3 / 2
        if player_bust and not dealer_bust:
            take = True
            payout = -2
        if not player_bust and dealer_bust:
            win = True
            payout = 1
        return (take, push, bj, win, payout)

    def finish_hand(self, eval):
        """
        Takes the result of a hand, and prints a statement to represent it to
        the player. Pays the player out.

        Args:
            eval:
            a tuple with four strings and an integer
            take: a string representing that the dealer won
            push: a string representing a tie
            bj: a string representing a blackjack for either the dealer or player
            win: a string representing the player win
            payout: an integer representing what the original bet should be multiplied by to be added to the bankroll
        """
        self.model.add_to_bank(
            self.model.player_bet + eval[4] * self.model.player_bet
        )
        if eval[0]:
            print("Ha! Your bet is mine!!")
        if eval[1]:
            print("Ugh, push. Take your bet, dweeb.")
        if eval[2]:
            print("21 - well played! Here is your bet and some extra.")
        if eval[3]:
            print("I dislike you mildly.")
        print(f"Bankroll: {self.model.player_bankroll}")


class SplitHand(OneHand):
    """
    Modifies the OneHand class in the case of a hand needing to be split.
    """

    def __init__(self):
        """
        Establishes that one card is dealt, sets up variables.
        """
        self.num_cards = 1


if __name__ == "__main__":
    main()
