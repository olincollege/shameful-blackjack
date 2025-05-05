# Blackjack

This is a blackjack game that runs from the terminal, taking user input.

## Running the Game

Download the repo and run the command `python run_game.py`

## How to Play

A player will start off with $500 to bet. The player can bet any amount between 1 and their remaining amount. 
Two cards will be dealt to the player. To calculate the current score, add up the values of both cards. All face cards are 10, and aces can be either 1 or 11.  
If the total of the first two cards is 21, the player has blackjack and is paid 3-2 their bet. 
Two cards are then dealt to the dealer: one is face up and the other is face down.  
The player can then choose whether to hit (be dealt another card) or stay (end their turn). This will be entered into the terminal as either 'h' or 's'. If the player's score goes above 21, they "bust" and lose their bet immediately.  
There are two special cases that can happen.  
If the player gets two cards that are the same (two 7s or two Jacks, for example), they can choose to split their hand. This means that they will treat each card as the first card in two separate hands. A bet equal to the original bet is placed on the second hand, and the player can hit and stay as usual on each hand.  
If the player's original two cards total to 9, 10, or 11, the player can choose to double down. This means that they will be dealt one more card face down, and cannot get any more cards. This face down card is not revealed until all bets are settled at the end.
If the player is dealt two fives, they can choose to split or double down.  
After the player is done, the dealer reveals their second card. If they have blackjack, they will collect the bet from the player if the player has less than 21. If the dealer has less than 17, they must keep drawing until they have 17 or more.  
Once all cards have been dealt and revealed, the bets are settled. If the dealer goes bust, they pay the original bet to the player if the player stood and did not go bust. If the dealer has a higher amount than the player (while both are under 21), the player loses their bet. If the player has a higher amount than the dealer (but still under 21), the dealer pays the amount of the original bet to the player. If botht he dealer and player have the same amount, it is called a "push" and no money is exchanged.  

## Requirements

No requirements besides cloning the repo are necessary.
