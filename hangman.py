import random
import os
start = ['Lets Begin']
hangman = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'
    WHITE = '\033[4m'

word_list = ["only","cat","dog","mouse","car","lion",
             "fruit","door","winner"]
chosen_word = random.choice(word_list)

os.system("clear")
print(bcolors.GREEN + f"\n{' '.join(start)}\n\n" + bcolors.END)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(bcolors.WHITE + f"{' '.join(alphabet)}\n" + bcolors.END)


screen = []
guessed = []
game_over = False
counter = 6

for _ in range(len(chosen_word)):
    screen += "_"
print(bcolors.BLUE+ f"\t\t{' '.join(screen)}" + bcolors.END)
print(bcolors.CYAN + hangman[0] + bcolors.END)
while not game_over:
    guess_a_word  = input("\nGuess a word: ").lower()

    os.system("clear")

    if guess_a_word in guessed:
        print(bcolors.RED + f"\t\tYou already guessed '{guess_a_word}'!" +  bcolors.END)
    elif guess_a_word not in guessed:
        if guess_a_word not in chosen_word:
            counter = counter - 1
        guessed += guess_a_word



    for point in range(len(chosen_word)):
        letter_in_word = chosen_word[point]
        if guess_a_word == letter_in_word:
            screen[point] = guess_a_word

    for position in range(len(alphabet)):
        letter_in_alphabet = alphabet[position]
        if guess_a_word == letter_in_alphabet:
            alphabet[position] = "-"

    guessed += guess_a_word

    print(bcolors.GREEN + f"\n{' '.join(start)}\n\n" + bcolors.END)
    print(bcolors.WHITE + f"{' '.join(alphabet)}\n" + bcolors.END)
    print(bcolors.BLUE + f"\t\t{' '.join(screen)}" + bcolors.END)

    if counter ==6:
        print(bcolors.CYAN + hangman[0] + bcolors.END)
    if counter==5:
        print(bcolors.CYAN + hangman[1] + bcolors.END)
    if counter==4:
        print(bcolors.CYAN + hangman[2] + bcolors.END)
    if counter==3:
        print(bcolors.CYAN + hangman[3] + bcolors.END)
    if counter==2:
        print(bcolors.CYAN + hangman[4] + bcolors.END)
    if counter == 1:
        print(bcolors.CYAN + hangman[5] + bcolors.END)

    if counter == 0:
        print(bcolors.CYAN + hangman[6] + bcolors.END)
        game_over = True
        print(bcolors.RED + f"\n\n-------YOU LOST!--------\n" + bcolors.END)
        print(bcolors.RED + f"The answer was --->  " + bcolors.END + bcolors.GREEN + f"{chosen_word}\n" + bcolors.END)

    if "_" not in screen:
        game_over = True
        print(bcolors.PINK+ "\n\nCongratulations!\nYOU WON THE GAME :)\n" + bcolors.END)