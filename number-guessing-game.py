#!/usr/bin/env python3
#the computer randomly select a number between 1 and
#100, and then prompt the player to guess the number. The program should give
#hints if the guess is too high or too low.
#Allow the user to specify the minimum and maximum values for the number
#range before the game starts.
#Implement a feature that limits the number of guesses a player can make. If
#the player runs out of attempts, the game should end, and the correct number
#should be revealed.
#Add a feature that keeps track of the fewest attempts it took to guess the
#number correctly. The program should display this "best score" at the end of
#each game.
import random
min = 0
max = 100

def basic_level(min, max, attempts_limit = None):
  best_score = 0
  attempts_counter = 0
  number = random.randint(min, max)
  while True :    
    attempts_counter += 1
    try:    
      guest = int(input(f'Guest the number between {min} and {max}: '))
      if guest < number:
        print('Too low, try again!')
      elif guest > number:
        print('Too high, try again!')
      else:
        print(f'You guessed the number, Congrats!!!: {number}')
        score = attempts_counter
        
        print(f'You have guessed the number in {score} attempts')
        if best_score <= score:
          best_score = score
          print(f'Your best score is: {best_score}')
        break
      if attempts_limit is not None and attempts_counter >= attempts_limit:
        print(f'Sorry, you have reached the maximum number of attempts and the correct number is: {number}')
        break
    except ValueError:
      print('Please input a valid number')

def medium_level(attemps=None):
 min = int(input('Choose a Minimum number: '))
 max = int(input('Choose a Maximum number: '))
 basic_level(min, max, attemps)

def hard_level():
  attemps = int(input('Input the max number of attemps to guest the number: '))
  medium_level(attemps)

while True:
  difficulty = int(input('Choose the difficulty of the game 1(Easy), 2(medium), 3(hard): '))
  if difficulty == 1:
    basic_level(min, max)
  elif difficulty == 2:
    medium_level()
  elif difficulty == 3:
    hard_level()
  play_again = input('Do you want to play again?(y/n): ').lower()
  if play_again == 'n':
    print('Thanks for playing, Bye!')
    break
  