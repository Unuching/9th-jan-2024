import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["unuching", "mrachingnu", "chengchengnu"]

chosen_name = random.choice(words)

display = []
for _ in range (len(chosen_name)):
        display += "_"


lives = 6
end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()


   

    for position in range(len(chosen_name)):
        letter = chosen_name[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_name:
         lives -= 1
         if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])