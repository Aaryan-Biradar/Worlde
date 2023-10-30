import random
import sys
from termcolor import colored


def print_menu():
  print ("Let's Play Wordle")
  print ("Type 5 letters to guess the word\n")

#Selects Random Word
def read_random_word():
  with open("words.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)

#Checks list of Valid words
def read_valid_words():
  with open("words.txt") as f:
      words = f.read().splitlines()
      return set(words)
valid_words = read_valid_words()

#Game loop
play_again = ""
while play_again != "q":
  
  print_menu()
  word = read_random_word()
  #print(word) 
  
  for attempt in range(1,7):
    guess = input().lower()

    while guess != word or len(guess) != 5:
      #Must be in the word file
      if guess not in valid_words :
        print(colored("Invalid Word!", "red"))
        guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

      #Must be 5 letters
      if len(guess) != 5:
        print(colored("MUST BE 5 LETTERS!","red"))
        guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        
      else:
          break
      
    # Deletes your input to show coloured letters
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    word_new = list(word)
    #Colours Letters 
    for i in range(min(len(guess), 5)):
      if guess[i] == word_new[i]:
          print(colored(guess[i], "green"), end="")
          word_new[i] = ''  # Replace the character in word_new with an empty string

      elif guess[i] in word_new:
        if guess[word_new.index(guess[i])] != word_new[word_new.index(guess[i])]:
            print(colored(guess[i], "yellow"), end="")
            index = word_new.index(guess[i])  # Find the index of the character
        else:
          print(guess[i], end="")

      else:
          print(guess[i], end="")


    #print("",word_new)
  
    if attempt != 0:
      print()

    # Quit Program Condition: Win
    if guess == word:

      print(colored(f"\nYou guessed the word in {attempt} tries!", "green"))
      break
    
    # Quit Program Condition: Lose
    if attempt == 6:
      print("\nMaybe next time!")
      print(f"The word was: {colored(word, 'green')}")

  play_again = input("Press q to quit or any other key to play again\n")
