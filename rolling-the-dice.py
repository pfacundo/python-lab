#!/usr/bin/env python3

#rolling a pair of dice
#Each time the program runs, it
#should randomly generate two numbers between 1 and 6 (inclusive),
#representing the result of each die
#The program should then display the results and ask if the
#user would like to roll again.
import random

def roll_the_dice(dice: int) -> None:
  for i in range(dice):
    die: int = random.randint(1, 6)
    print(f'The result of the dice({i+1}) is: {die}')

while(True):
  choice = input('Rolling the dice?(y/n): ').lower()
  if choice == 'y':
    dice = int(input('How many dice do you want to use?: '))
    roll_the_dice(dice)
  elif choice == 'n':
    print('Thanks for play, Bye!')
    break
  else:
    print('There was an error, please select y or n')

