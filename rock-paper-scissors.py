#The game will prompt the player to choose rock, paper, or scissors by typing 'r',
#'p', or 's'. The computer will randomly select its choice. The game will then display
#both choices using emojis and determine the winner based on the rules.
#Modify the game so that the first player (or computer) to win two out of three
#rounds is declared the overall winner.
#Keep a tally of how many times the player wins, loses, or ties with the
#computer
#Add an option for two players to play against each other, taking turns to input
#their choices

import random
import emoji

choices = {
    'r': emoji.emojize(':rock:'),
    'p': emoji.emojize(':roll_of_paper:'),
    's': emoji.emojize(':scissors:')
}

user_games = 0
computer_games = 0
tie_score = 0
user_score = 0
computer_score = 0

def define_winner(choice1, choice2, game_mode):
    
  if choice1 == choice2:
    print('It\'s a tie')
    return 'tie'

  elif (
    choice1 == 'r' and choice2 == 's'or 
    choice1 == 'p' and choice2 == 'r' or
    choice1 == 's' and choice2 == 'p'):
    if game_mode == '1':
      print('You win!')
      return 'user'
    else:
      print('Player 1 wins!')
      return 'user'	
  else:
    if game_mode == '2':
      print('Player 2 wins!')
      return 'computer'
    else:
      print('You lose!')
      return 'computer'  

def score_board (winner, game_mode):
  global user_score, computer_score, tie_score, user_games, computer_games

  if winner == 'tie':
    tie_score += 1
  elif winner == 'user':
    user_score += 1
  else:
    computer_score += 1
  if game_mode == '1':
    print(f'Your score: {user_score} and Computer score: {computer_score} and Ties: {tie_score}')
  else:
    print(f'Player1 score: {user_score} and Player2 score: {computer_score}')

  if user_score == 2 and game_mode == '1':
    print('You won the game! Congrats!')
    user_games+= 1
    user_score = 0
    computer_score = 0
    print(f'Your games: {user_games}, Computer games: {computer_games} and Ties: {tie_score}')
  
  elif computer_score == 2 and game_mode== '1':
    print('You lost the game!')
    computer_games+= 1
    computer_score = 0
    user_score = 0
    print(f'Your games: {user_games}, Computer games: {computer_games} and Ties: {tie_score}')

  elif user_score == 2 and game_mode == '2':
    print('Player1 won the game! Congrats!')
    user_games+= 1
    user_score = 0
    computer_score = 0
    print(f'Player1 games: {user_games}, Player2 games: {computer_games} and Ties: {tie_score}')
  elif computer_score == 2 and game_mode == '2':
    print('Player2 won the game!')
    computer_games+= 1
    computer_score = 0
    user_score = 0
    print(f'Player1 games: {user_games}, Player2 games: {computer_games} and Ties: {tie_score}')

game_mode = input(
  "Welcome to Rock, Paper, Scissors!.\n\
  Choose the game mode\n\
  1. Single player\n\
  2. Two players\n\
  Enter your choice: "
  )
if game_mode == '1':
  while True:
    print('-------------------------------------------------')
    try:
      user_choice = input('Best of 3 \nChoose rock(r), paper(p), or scissors(s): ')
    except ValueError:
      print('Invalid choice, please choose r, p, or s.')
      continue

    computer_choice = random.choice(list(choices.keys()))
    print(f'Your choice: {choices[user_choice]}  and Computer choice: {choices[computer_choice]}')
    winner = define_winner(user_choice, computer_choice, game_mode)

    score_board(winner, game_mode)

  
    if input('Continue playing?(Y/n):') == 'n':
      print('GAME OVER \nThanks for playing!')
      break
    
elif game_mode == '2':
  while True:
    print('-------------------------------------------------')
    try:
      player1_choice = input('Best of 3 \nPlayer 1 choose rock(r), paper(p), or scissors(s): ')
      player2_choice = input('Player 2 choose rock(r), paper(p), or scissors(s): ')
    except ValueError:
      print('Invalid choice, please choose r, p, or s.')
      continue
    print(f'Player 1 choice: {choices[player1_choice]}  and Player 2 choice: {choices[player2_choice]}')
    
    winner = define_winner(player1_choice, player2_choice, game_mode)

    score_board(winner, game_mode)
    
    if input('Continue playing?(Y/n):') == 'n':
      print('GAME OVER \nThanks for playing!')
      break