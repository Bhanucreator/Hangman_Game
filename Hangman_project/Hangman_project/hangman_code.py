import random
from hangman_words import words_of_fruits, words_of_vegetables, words_of_animals, words_of_countries
from hangman_art import stages, logo

lives = 6
print(logo)
user_choice = int(input(
    "Enter the field \n 1.press for fruits \n 2.press for vegetables \n 3.press for animals \n 4.press for countries \n"))

# Choose the word based on user's choice
if user_choice == 1:
    chosen_word = random.choice(words_of_fruits)
elif user_choice == 2:
    chosen_word = random.choice(words_of_vegetables)
elif user_choice == 3:
    chosen_word = random.choice(words_of_animals)
elif user_choice == 4:
    chosen_word = random.choice(words_of_countries)
else:
    print("Please Enter The Valid choice")
    exit()  # Exit the program if the choice is not valid

# Initialize the placeholder for the word
word_length = len(chosen_word)
placeholder = ["_"] * word_length
print("Word to guess: " + " ".join(placeholder))

game_over = False
correct_letters = []

while not game_over:
    print(f"************ {lives}/6 LIVES LEFT ************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    correct_letters.append(guess)
    display = ""

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            placeholder[index] = letter

    display = " ".join(placeholder)
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"****************** IT WAS {chosen_word}! YOU LOSE ******************************")

    if "_" not in placeholder:
        game_over = True
        print("***************** YOU WIN **********************")

    print(stages[lives])