import random
from replit import clear
from art import logo

# Function to deal a random card from the deck
def deal_card():
 """Returns a random card from the deck."""
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 card = random.choice(cards)
 return card

# Function to calculate the score of a hand
def calculate_score(cards):
 # Check for blackjack (ace + 10)
 if len(cards) == 2 and sum(cards) == 21:
    return 0
 # Adjust score if it exceeds 21 and contains an ace
 if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
 return sum(cards)

# Function to compare scores and determine the game outcome
def compare(user_score, computer_score):
 if user_score == computer_score:
      return "It's a Draw"
 elif computer_score == 0:
      return "Computer wins with a blackjack!"
 elif user_score == 0:
      return " You win with a blackjack"
 elif user_score > 21:
      return "You went over. You lose!"
 elif computer_score > 21:
      return "Computer went over. You win!"
 elif user_score > computer_score:
      return "You win!"
 else:
      return "Computer wins!"

# Main game function
def play_game():
 print(logo)

 user_cards = []
 computer_cards = []
 is_game_over = False

 # Deal two cards to the user and computer
 for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

 # Game loop
 while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score is: {user_score}.")
    print(f" Computer's first card: {computer_cards[0]}.")

    # Check for game end conditions
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("\nType 'y' to get another card or 'n' to pass:").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

 # Computer's turn to draw cards until score is 17 or higher
 while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

 # Print final hands and scores
 print(f"\n Your final cards: {user_cards}, final score: {user_score}.")
 print(f" Computer's final cards: {computer_cards}, final score: {computer_score}.")
 print(compare(user_score, computer_score))

# Main game loop
while input("\nDo you want to play a game of Blackjack? Type 'y or 'n': ") == "y":
 clear()
 play_game()
