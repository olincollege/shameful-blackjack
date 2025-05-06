from model import Cards, Model


def main():
    # Cards tests
    print("Cards class tests")
    cards_test = Cards()
    print("Unshuffled deck:", cards_test)  # should be in order
    cards_test.shuffle()
    print("Shuffled deck:", cards_test)  # should be in a random order
    list_deck = list(cards_test.available_deck.keys())
    # Model tests
    print("Model class tests")
    model_test = Model()
    test_bet = 30
    model_test.set_bet(test_bet)
    num = 0
    model_test.deal_player(list_deck, num)
    num += 1
    model_test.deal_player(list_deck, num)
    num += 1
    model_test.deal_dealer(list_deck, num)
    num += 1
    model_test.deal_dealer(list_deck, num)
    print(model_test)
    print(
        "Player's score:",
        model_test.un_double_score(
            model_test.check_score(cards_test, model_test.player_hand)
        ),
    )
    print(
        "Dealer's score:",
        model_test.un_double_score(
            model_test.check_score(cards_test, model_test.dealer_hand)
        ),
    )
    print("double down, split, and insurance tests")
    checks = model_test.checks(
        model_test.player_hand, model_test.dealer_hand, cards_test.deck
    )
    print(
        f"double down: {checks[0]}, split: {checks[1]}, insurance: {checks[2]}"
    )


if __name__ == "__main__":
    main()
