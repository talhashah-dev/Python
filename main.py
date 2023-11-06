import random

def choose_word():
    word_list = ["apple", "banana", "orange", "grape", "watermelon", "strawberry", "pineapple"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word_to_guess = choose_word()
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter. Try another one.")
            continue

        guessed.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
            if attempts == 0:
                print("You're out of attempts. The word was:", word_to_guess)
                break
        else:
            print("Good guess!")

        word_display = display_word(word_to_guess, guessed)
        print(word_display)

        if "_ " not in word_display:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
