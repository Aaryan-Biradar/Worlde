import sys
from termcolor import colored
from random_words import RandomWords
import nltk
from nltk.corpus import words

nltk.download("words")
nltk_words = set(words.words())

def print_menu():
    print("Let's Play Wordle")
    print("Type 5 letters to guess the word\n")

#Random word generator
def generate_random_real_word():
  r = RandomWords()
  while True:
      word = r.random_word()
      if len(word) == 5 and word.isalpha():
          return word

#valid English word checker
def is_valid_english_word(word):
    if word in nltk_words:
        return True
    return False

#delets lines in terminal
def delete(x):
  for i in range(x):
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

#Visual display of guessed letters
def display_keybaord():
  for key in keyboard:
    if keyboard[key] == 3:
      print(colored(key, 'red'), end=' ')
    elif keyboard[key] == 2:
      print(colored(key, 'green'), end=' ')
    elif keyboard[key] == 1:
      print(colored(key, 'yellow'), end=' ')
    else:
      print(key,end=' ')
  print()

keyboard = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0,
            'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0,
            'w':0, 'x':0, 'y':0, 'z':0}

#Game loop
play_again = ""
while play_again != "q":

  print_menu()
  word = generate_random_real_word()
  #print(word) (for debugging)

  for attempt in range(1,7):
    guess = input().lower()

    while guess != word or len(guess) != 5:
      #Must be a valid English word and length of 5
      if not is_valid_english_word(guess) or len(guess) != 5:
        print(colored("Invalid Word!", "red"))
        guess = input().lower()
        delete(2)
      else:
        break

    # Deletes your input to show coloured letters + previos key board display
    
    if attempt == 1:
      delete(1)
    else:
      delete(2)

    word_new = list(word)
    #Colours Letters 
    for i in range(min(len(guess), 5)):
      if guess[i] == word_new[i]:
          print(colored(guess[i], "green"), end="")
          word_new[i] = ''  # Replace the character in word_new with an empty string
          keyboard[guess[i]] = 2
      elif guess[i] in word_new:
        if guess[word_new.index(guess[i])] != word_new[word_new.index(guess[i])]:
          keyboard[guess[i]] = 1
          print(colored(guess[i], "yellow"), end="")
          index = word_new.index(guess[i])  # Find the index of the character
        else:
          keyboard[guess[i]] = 3
          print(guess[i], end="")
          
      elif guess[i] not in word_new:
        keyboard[guess[i]] = 3
        print(guess[i], end="")
        
    # New line and Displays the keyboard
    print()
    display_keybaord()

    # Quit Program Condition: Win
    if guess == word:
      print(colored(f"\nYou guessed the word in {attempt} tries!", "green"))
      break

    # Quit Program Condition: Lose
    if attempt == 6:
      print("\nMaybe next time!")
      print(f"The word was: {colored(word, 'green')}")

  play_again = input("Press q to quit or any other key to play again\n")
